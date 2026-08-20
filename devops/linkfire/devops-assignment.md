> Локальная копия. Источник: <https://github.com/GetLinkfire/devops-assignment>

# Linkfire DevOps assignment

================

## What to do?

===========

First of all, clone this repository:

```text
git clone git@github.com:getlinkfire/devops-assignment.git
```

Now, given [this Docker Compose file](./docker-compose.yml), stand up a [Druid](http://druid.io) cluster.

The compose file is going to launch :

* 1 zookeeper node
* 1 MySQL database
* 1 Kafka message broker

and the following druid services :

* 1 broker
* 1 middlemanager
* 1 historical
* 1 coordinator/overlord

This will take a couple of minutes, but once it is up, you will have:  

* The Druid cluster dashboard on: [http://localhost:3001/#/](http://localhost:3001/#/)
* The Druid indexing console on: [http://localhost:3001/console.html](http://localhost:3001/console.html)

Now that you have a running cluster, [ingest](wikiticker-index.json) the data found in [data/wikiticker-2015-09-12-sampled.json.gz](data/wikiticker-2015-09-12-sampled.json.gz).  
Once your ingestion job has succesfully executed, perform [a simple query](wikiticker-top-pages.json) on the freshly created *datasource*.

The dataset is kindly borrowed from the [Druid quickstart tutorial](http://druid.io/docs/0.12.1/tutorials/quickstart.html), you may find some inspiration there.  
Read a little about the [Druid indexing service](http://druid.io/docs/0.12.1/design/indexing-service.html) if you like ;)

### Extra assignments

Piece of cake was it?  
Alright, while the above should get us off the ground talking about troubleshooting skills and JVM heap configuration (hint), if you feel courageous; go ahead and setup [realtime ingestion through Kafka](http://druid.io/docs/0.12.1/development/extensions-core/kafka-ingestion.html), into the *wikiticker* datasource, and query your data back out again with a [select query](http://druid.io/docs/0.12.1/querying/select-query.html).  

Also, the attentive ones will notice that we have configured Druid to emit metrics into Kafka. Now create a new *Druid datasource*, and ingest those metrics back into Druid where we can query them. You may find a bit of inspiration in [this blog post](https://metamarkets.com/2015/dogfooding-with-druid-samza-and-kafka-metametrics-at-metamarkets/).

#### Came here by accident?

Well a good puzzle is hard to resist isn't it?  
If you found your way through our little builtin quirks and gotchas out of pure curiosity, we would absolutely love to hear from you. Please write us an email on [devops@linkfire.com](mailto:devops@linkfire.com), tell us what we misconfigured and what you did to make this setup shine.
