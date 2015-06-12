Date: 2015-06-13
Title: Recapping SRECon EU 2015
Tagline: Part 2
Slug: sreconeu2015recappart2
Category: Blog
Tags: sre, presentations, usenix, review

This is the second part of my notes and thoughts on [SRECon Europe 2015](https://www.usenix.org/conference/srecon15europe/program). The [first part](https://eoinbrazil.com/sreconeu2015recap.html) covers focuses on the workshops and some of the talks I attended.

### Talks

#### Opening Keynote - PostOps: Recovery from Operations
The tone of the conference was set by Todd Underwood who is the Director of Google's Site Reliability Engineering team. He neatly laid out and introduced SRE as the systems and software engineers who solve production problems with software. The concepts are inspired some what from Adrian Cockcroft's "NoOps" where there is no operations organisation and it is software developers supported by automation who are working directly with production. This isn't to say you shouldn't take the best of operations culture and apply it to your production engineering team. Site reliability engineering needs to be taken as a first-class responsibility / citizen. The talk was a good summary of the various concerns and history as to why the computing sector needs to move beyond the definitions of "Administration" and of "Operations".

#### Prometheus
[Prometheus](http://prometheus.io/) is a new monitoring system built by a number of engineers from SoundCloud and several former Google SREs. This [Soundcloud Developers post introduces](https://developers.soundcloud.com/blog/prometheus-monitoring-at-soundcloud) the system and how it has been designed to overcome issues they found with StatsD and Graphite. The four key features they highlighted during the talk where:
1. A multi-dimensional data model which allows pretty manuipulation of dimensions of the data
2. Simplicity to install and operate
3. Scalable data collection and decentralized architecture (time series collection via a pull model over HTTP)
4. A query language

It has a number of very useful features building on the work for systems like [OpenTSDB](http://opentsdb.net/) and it has pretty much the same data model and syntax as OpenTSDB. This is where time series is identified by a metric name and a set of key-value pairs. These can be queried by its expression browser and the data can be visualised on dashboard using their PromDash tool. It hooks into to the likes of PagerDuty and supports a Nagios plugin allowing Prometheus to 'bridge' to existing Nagios deployments.

A big change is that Prometheus requires you to instrument your own code directly. The rationale for this is that is will provide higher quality service based monitoring.n instrumentation is usually worth the price. There are a range of client libraries for most programming languages. These client libraries allow metrics to be exposed via HTTP using either the protocol buffers format or as a simpler text-based format.

The Prometheus servers scrape metrics from the instrumented applications directly or using a gateway. These samples then stored locally with rules executed over this data to generate new timeseries or to generate alerts. These streams of timestamped values all belong to the same metric with the same labeled dimesions. Timestamps are at a resolution of a millisecond resolution and the values are saved as 64-bit floats.

There are a range of blogs about it but I'd highly recommend my fellow programme committee member Brian Brazil's series monitoring on the [Boxever blog](http://www.boxever.com/tag/monitoring). He was key team player in helping to organising the conference and is a committer to Prometheus.

#### Signatures, Patterns, and Trends: Timeseries Data Mining at Etsy
I can well imagine one of the maxims at Etsy being, if it moves, measure it and even if it doesn't, measure it. They record a ton of metrics and now have over a million metrics. This means they're literally drowning in data and traditional approaches means that both alerting and graphicing are not cutting it. Graphs don't scale well to a million distinct metrics and alert thresholds become very prone to triggering due to false positives.

In order to manage this magnitude of metrics they have developed the [Kale stack](https://codeascraft.com/2013/06/11/introducing-kale/). It consists of [Skyline](https://github.com/etsy/skyline) and [Oculus](https://github.com/etsy/oculus), the first help detects anomalous metrics and the latter is used to correlate patterns between metrics. This stack helps them detect any issues and make better hyptotheses around their problems.

I definitely like the 'hack' with the shape description alphabet for a timeseries similarity. The Etsy stack is focused on their problem of lots of metrics and how to monitor the million+ interdependent time-series. It stores these time series in Redis and uses ElasticSearch for the search component. The next iteration of the stack, 'Thyme', was the latter end of the talk and looks pretty cool.

#### Upgrade Your Database without Losing Your Data, Your Perf, or Your Mind
Charity Majors as ever gave an excellent talk that helped open the minds of many to the dangers of database upgrades. There is a shorter and earlier version of [this online](https://speakerdeck.com/charity/upgrading-databases-without-losing-your-data-your-perf-or-your-mind). I have to say go [watch the video](https://www.usenix.org/conference/srecon15europe/program/presentation/majors) as it is one of the best talks but I'm a bit biased towards this topic these days!

It discusses the apprioriate levels of paranoia you should have, the need to balance effort against risk, and how to capture and replay production traffic to feed this the database. She talked a little bit about their [flashback tool for replaying MongoDB workloads](https://github.com/ParsePlatform/flashback). There is a more detailed blog on the Parse site covering [how to setup this tool](http://blog.parse.com/learn/engineering/mongodb-rocksdb-benchmark-setup-compression/).

#### Going Off the Rails: Infrastructure Outage Planning
There was a nice talk reviewing some of the aspects of a major incident in the London Underground with hardware upgrades, hardware failure and insufficent planning all contributing. It particularly highlighted how the failure to implement one element of the plan around managing the loading/offloading of trains meant chaos and massive queues for passengers. There was a nice section on lesson learnt and plans to prevent future incidents.

The talk summarised this [report from Network Rail on the incident](https://www.networkrail.co.uk/review-into-disruption-affecting-kings-cross-and-paddington-services-27-December-2014.pdf) and focused on what learnings SREs could take from it.

#### Bad Machinery— Managing Interrupts Under Load
One of the Google Storage SREs gave a very interesting talk on the personal side of how we (as individuals) manage interruptions in complex and busy production situations. In the case of SREs who both write code and work oncall it is important to really value keeping the engineering in the flow doing one thing well. It echos an earlier Velocity 2014 talk from Etsy who spoke about "[Mean Time to Sleep: Quantifying the On-Call Experience](https://www.youtube.com/watch?v=FLqucVb_et0)" which has [a blog post](https://codeascraft.com/2014/06/19/opsweekly-measuring-on-call-experience-with-alert-classification/) and their [opsweekly tool](https://github.com/etsy/opsweekly).

These talks are very valuable as understanding and measuring the interrupts can help in crafting better contextualised alerts or in not alerting the engineer unless it is necessary. As more companies deployer larger systems and services these practices will become more wide spread but in the meanwhile it's great to see how others are managing this issue.

### Aside regarding hiring and managing SREs
The latest ;login Usenix magazine (June 2015, Vol. 40, No. 3) has two great articles including one from Todd Underwood (opening keynote speaker). These are well worth a read to help understand the role and how to hire the calibre of people needed for this type of role.

  * ["Hiring Site Reliability Engineers" by Chris Jones, Todd Underwood, and Shyjala Nukala](https://www.usenix.org/publications/login/june15/hiring-site-reliability-engineers)
  * ["The Systems Engineering Side of Site Reliability Engineering" by David Hixson and Betsy Beyer](https://www.usenix.org/publications/login/june15/hixson)
