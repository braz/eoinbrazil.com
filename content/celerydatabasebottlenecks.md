Date: 2018-03-31
Title: Celery Database Bottlenecks
Tagline: The joys of performance whack-a-mole with distributed systems
Slug: celerydatabasebottlenecks
Category: Blog/Python
Tags: python, queues, celery, bottlenecks

I recently had to refactor some code which uses MongoDB and Celery to store results from a scraping process to a MongoDB collection. It involved a number of whack a mole type performance problems due to the distributed nature of the system, and indeed was leading to the [Linux out of memory (OOM) killer](https://linux-mm.org/OOM_Killer) being triggered against some of those workers. I wanted to write up some of the approaches I took as they may be helpful to others and indeed maybe there are better ways out there to handle the same situation (so any feedback would be much appreciated!).

The inspiration for writing this approach in a blog was another [blog post on handling memory intensive Celery workers](https://www.vinta.com.br/blog/2018/dealing-resource-consuming-tasks-celery/). This highlighted yet another Celery setting I wasn't using on [prefetch limits](http://docs.celeryproject.org/en/latest/userguide/optimizing.html#prefetch-limits) or indeed aware of. The approach from that blog used Celery's worker prefetch limiting to avoid running out of memory on the workers. The approach below was what I used to avoid running out of memory. It occurs at one step earlier by avoiding sending tasks to the Celery worker from the Python programme distributing the work than throttling the tasks once on the workers. I think either approach may work and I'm glad to have found the blog to both prompt future thinking and my writing of this post.

## 1. Limit task submission if Database queue is at or above the maximum threshold ##

This function implemented a simple limit and wait logic for the application calling the specific Celery Workers, the example below uses a trivialised example with a single Worker named 'celery1'. The Celery task inspection function, celery.task.control.inspect(), is queried in the calling Python programme and the running-threads value for the specific worker (which is only used for this one queue) is what determines whether this function will return. If there are too many existing tasks on the worker, the function will sleep until the number of tasks are less than the value set for the variable, message_queue_max.

    #!python
    def check_and_backoff_if_db_queue_at_max(self, **kwargs):
    message_queue_max = 15
    ins = inspect()
    try:
        while True:
            queue_over_max_length_for_worker_1 = False
            all_stats = ins.stats()
            if all_stats is None:
                msg = "No Celery Workers have been detected."
                logger.error(msg)
                raise RuntimeError(msg)
            for k in all_stats.keys():
                if k.startswith('celery1') and all_stats[k]['pool'].get('running-threads', 0) >= message_queue_max:
                    queue_over_max_length_for_worker_1 = True
            if queue_over_max_length_for_worker_1:
                logger.info("The DB queue is above %s pausing for 15 seconds.", message_queue_max)
                sleep(15)
            else:
                break
    except kombu.exceptions.OperationalError:
        msg = "Failed to connect to Celery Workers or to RabbitMQ at {}".format(self.celery_config.broker_url)
        logger.error(msg)
        raise RuntimeError(msg)

## 2. Setting appropriate task settings for this type of DB task ##
In order to better manage this type of task, I set three of Celery's Task setting. The results are ignored from the task, the task was configured for only acknowledged late rather than using the default of acknowledge on receipt rather than completion of the task (acks_late), and finally the time limits for this task was removed. The task is also configured to make two retry attempts if it fails.

    :::python
    max_retries=2, ignore_result=True, acks_late=True, soft_time_limit=None

## 3. Changing the database usage from a upsert to a insert and ignore approach ##

This step actually removed the need for the backoff for my particular usage where a large number of upserts operations (updates for existing documents or if not present then the document(s) are inserted) were the root cause of the Celery Worker having such a long queue. A change to a insert only approach, which was feasible for my application as it only required the document to be present once, provided close on two orders of magnitute improvement to the database operations and significantly reduced the Celery Worker queue as tasks were no longer backing up.

    :::python
    bulk_result = MongoClient(mongo_uri).DATABASE.COLLECTION.bulk_write(array_of_insert_one_operations, ordered=False)

## 4. Minor discoveries in a useful practical sense but not core to solving my problem ##

In the reading and research to address my queue growing too large and triggering the [Linux out of memory (OOM) killer](https://linux-mm.org/OOM_Killer), I found two useful Celery setting which I had not been aware of. Firstly, you can setup Celery Workers to receive events using the ("-E") option which allows for restarting worker pools directly through Celery Flower (the Management UI I use for Celery) when combined with the "worker_pool_restarts" setting.

A second aspect of our internal tooling using a scraper approach, specifically a number of the workers use tasks that are primarily focused on asychronous HTTP requests so these use the [Eventlet execution pool](http://docs.celeryproject.org/en/latest/userguide/concurrency/eventlet.html). The deployment uses a standard Celery/RabbitMQ configuration. RabbitMQ uses a default setting where 10 concurrent connections are kept open for the broker pool when used with Celery. The setting "broker_pool_limit" allows for this to be raised, in this example below it is set to 100 which is more suitable for this type of Celery Worker/Eventlet execution pool combination.

    :::python
    worker_pool_restarts = True
    broker_pool_limit = 100

## Future directions ##

The tooling currently uses [celery.bin.multi](http://docs.celeryproject.org/en/latest/reference/celery.bin.multi.html) with bash scripting as each node hosts multiple workers, however it is being containerized so I think my next blog will cover moving to [supervisord](http://supervisord.org/) with a Celery setup of multiple workers per node providing multiple queues.