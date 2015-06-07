Date: 2015-06-07
Title: Recapping SRECon EU 2015
Tagline: Site Reliablity Engineering from a European Perspective
Slug: sreconeu2015recap
Category: Blog
Tags: sre, presentations, usenix, review

I had the pleasure of helping to organise as well as attending [SRECon Europe 2015](https://www.usenix.org/conference/srecon15europe/program). I have pulled together a few of my notes and links of interest to recap what was an excellent conference. It was focused on operations engineering and on site reliability topics with speakers from many of the big names (e.g. Google, Facebook, Yelp, Spotify amongst others).

My personal goals outside of my programme committee role for the conference where to find out what counterparts where doing in similar or larger organisations. My current role with MongoDB involves a lot of customer facing work and troubleshooting so I was very interested in the Postmortem and Large Scale Abstract Design workshops. I've presented a lot of work to the Dublin R Usergroup on machine learning so I took the opportunity to attend a similar session from Splunk. I dipped in and out of the other sessions at the conference. In the reminder of this blog post, I'll firstly cover my notes from the three workshops then move to my notes from the various talks and finally add some useful tools / pointers from other attendees.

As an aside, the last topic and most scary talk was on EU data protection, specifically the view / thinking of the European Court of Justice (ECJ) and the US Safe Harbour agreements. It was given by Simon McGarr, a well known Irish socilitor who's been a great advocate of Digital Rights in Ireland. It painted a scary picture that the EU and USA may end with two distinct Internets before 2015 is finished once the ECJ makes a ruling (expected in Oct/Nov). I'm not a legal expert so instead I'll refer you to a [recent summary](http://eulawanalysis.blogspot.ie/2015/03/does-facebook-and-usa-violate-eu-data.html) by Simon himself.

### Workshops

#### Postmortems
I think I can safely say this session changed my thinking around Postmortems. I cannot recommend the work of Etsy and John Allspaw highly enough in this regard. He was fantastic and brought us on a journey of understanding helping us to evolve a more nuanced and mature sense of investigation as well providing links to a larger toolkit to facilitate such sessions. I think these two bullet points encapsulate John's teaching
 * "Key goal of postmortems is to LEARN rather than bring list of TODOs away"
 * "Goal of workshop on Postmortems is to help you ask better questions not give a magic process"

In order to facilitate their Postmortem process Etsy have developed their own tool [Morgue](https://github.com/etsy/morgue/blob/master/README.md) that allows them to tag, annotation and extract/link to specific issues in their Jira ticketing system. There's a great talk by [Bethany Macri on the Morgue tool](http://www.slideshare.net/devopsdays/morgue-helping-better-understand-events-by-building-a-post-mortem-tool-bethany-macri) that explains it in more depth.

One of the reference for improving communications that John mentioned in his talk is the book "Crucial Conversations" and having recently bought a copy, I'd also concur. I also got a pointer to another excellent post from Lara Hogan (also at Etsy) on [giving presentation feedback](http://larahogan.me/blog/giving-presentation-feedback/). Etsy really impressed me at SRECon and looking forward to more of their talks in the future.

This work and thinking are influenced on the five steps (see below) based on Dekker's methodology. As such it very useful to read ["Reconstructing human contributions to accidents- the new view on error and performance" by Sidney W.A. Dekker](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.411.4985&rep=rep1&type=pdf) to help understand this "new thinking" and the rationale behind it.

Five steps for a postmortem create a concept-depentant account from the context-specific event data:
1. outline the sequence of events in context-specific language
2. if necessary, break the sequence of events into episodes, if necessary (avoiding the global singular timeline)
3. determine how the world changed during each episode
4. identify what the focus of attention, the goals of people and what knowledge was active at that point in time
5. work up to a conceptual description

This thinking and John's talk put forward the view that Reductionism is false that outcomes can be foreseen in complex systems, that time is reversible (you can't rewind the buffer to reconstruct), and likewise that complete knowledge is not attainable. It underlined that "Why" is a terrible question to ask and immediately translated to "Who is responsible". In a postmortem, when you ask "How" it translate to "What is responsbile". Once you ask "Why" you lose context and it means that at least half of the key context and details are lost. One of the worst methods for a postmortem is the "Five Whys" as not only does it lose context but it also further loses complexity as it linear sequential. It is much better to ask "Why else" and better again to ask "How". A key point was that "Why" is often used as a technique to shutdown conversations. At this point, there was recommendation to read the book "Crucial Conversations: Tools for Talking When Stakes Are High" and it's definitely well worth it.

There is so much useful stuff that John covered that a full blog series could be dedicated to it and my recommendation is that you view one of his many videos online if you're interested in learning more.


#### Large Scale Abstract Design
This was a great half day small team classroom event where a real-world large scale engineering problem was presented. Each team had to come up with as much of the following as time allowed:

* A high-level design that scales horizontally
* Initial SLIs, SLOs
* Estimates for hardware required to run each component
* If time permits, monitoring design and disaster testing scenarios

It was a great exercise and I'll refain from saying too much more as we where asked to avoiding sharing the content as they will reuse it. However I can provide a few links to relevant talks/slides:

1. [Software Engineering Advice from building Large Scale Systems by Jeff Dean](http://static.googleusercontent.com/media/research.google.com/en//people/jeff/stanford-295-talk.pdf)
2. [Notes on Distributed Systems for Young Bloods by Jeff Hodges](http://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)
3. [Distributed Consensus Algorithms for Extreme Reliability by Laura Nolan](https://www.usenix.org/sites/default/files/conference/protected-files/srecon15europe_slides_nolan.pdf)

#### Machine Learning on Machine Data
There was a great series on statistical and machine learning talks, I attended the latter but I'll include links to both for those who might want to refresh their statisticial skills:
1. [Statistics Tutorial for SREs by Heinrich Hartmann](https://github.com/HeinrichHartmann/StatisticsTutorial)
2. [Machine Learning for Machine Data](https://docs.google.com/presentation/d/1JsanuUB8_6ae2mWEWyCzxhgcoe68G8EzaDgrgKUOopA/edit#slide=id.g9bd6a2176_2_87)

The machine learning workshop was fast paced and required Splunk so if you're interested in following the slides you'll need to install it first. I learnt a few new tricks and enjoyed somebody else giving a talk on that topic (I've done a similar talk but with R recently). It was particularly nice to see how to structure the introduction and Splunk is a very powerful tool that I'll definitely be learning/using more.

### Talks
There was so many excellent talks that I can't list them all. The standards where high and presentations excellent. I'll include a few that cover the spectrum of topics covered:

### Operational Software Design
Theo Schlossnagle gave an excellent talk on [Operational Software Design](https://www.usenix.org/conference/srecon15europe/program/presentation/schlossnagle) with the [full slides online](http://www.slideshare.net/postwait/operational-software-design). It covered many tools such as DTrace, [backtrace.io](http://backtrace.io/), and their own [fq](https://github.com/circonus-labs/fq). He wrote fq to replace RabbitMq due to a number of issues where it was unable to work for their monitoring needs. fq is a brokered message queue using a publish subscribe model. It has been designed for performance and large number of connected clients.

Russia's Yandex (2nd search engine in Russia) talks about the types of load tests that they use and presented 
[Yandex Tank](https://github.com/yandex/yandex-tank) their tool for this. The [slides](https://www.usenix.org/sites/default/files/conference/protected-files/srecon15europe_slides_lavrenuke.pdf) and [abstract](https://www.usenix.org/conference/srecon15europe/program/presentation/lavrenuke) covered the full depth of this talk.

I'm tied as which was my best talk as to whether it was from Susan Coghlan on improving infrastructure performance using root cause analysis (+2.5x MTTF) or Avleen Vig on [remote working](https://www.usenix.org/conference/srecon15europe/program/presentation/vig). Susan's talk was from the Argonne HPC National Lab and showed how over the last five years, their process has contributed to improved reliability (e.g. 5x improvement MTTI), utilization (10% increase), and changed the problem priortisation approach. I think Avleen Vig wins out on how Etsy manages the challenges faced by engineers, management, and organizations, and ways to address the issues to successfully build distributed teams.


### Useful Tools/Links
Here's a list of tools and links I got from the talks.

#### Nagios related
  * [nagios-herald](https://github.com/etsy/nagios-herald)
  * [Use the use_large_installation_tweaks configuration option in Nagios](http://nagios.sourceforge.net/docs/3_0/largeinstalltweaks.html)

#### Zookeeper related
  * [zktraffic, iptraf / top monitor for ZooKeeper](https://github.com/twitter/zktraffic)

#### Kafka related
  * [Kafkacat, a generic command line non-JVM Apache Kafka producer and consumer](https://github.com/edenhill/kafkacat)
  * [PyKafka is a cluster-aware Kafka protocol client for python](https://github.com/Parsely/pykafka). It includes python implementations of Kafka producers and consumers
  * [Apache Kafka load testing weapon](https://github.com/jamiealquiza/sangrenel)
  * [Apache Kafka Test Framework for Producer and Consumers for Compatibility Testing](https://github.com/stealthly/gauntlet)
  * [Go library for Kafka](https://github.com/stealthly/go_kafka_client)
