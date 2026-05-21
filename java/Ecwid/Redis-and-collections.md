First, some facts:

* There is key-value storage: [Redis](https://redis.io/).
* Java has interface java.util.Map

We like Redis a lot, but using it through a separate client library in Java doesn't really appeal to us. It works, it's convenient, but it's not fun.
Again, Java has a basic interface for implementing hash tables - Map. And Redis has a hash data structure.

We would like to work with hashes in Redis through this base interface. That is - I have some object that implements the Map interface,
I just pull its get/put/etc. methods, and the data is actually stored in Redis, not in my Java application.
Then I could pass that object anywhere the Map interface is expected and everything would just work.

All sorts of other thoughts:

* We have a lot of data and it just won't fit on a single Redis machine. It would be nice if the implementation itself could split the data across a cluster of Redis's, completely hiding details about the number of Redis instances and whatnot.
* Support for adding/removing Redis servers on the fly is very good. The key word is "on the fly".
* Redundancy of data storage in this cluster of redis is an interesting thought. Well, it's so that one redis goes down and its data doesn't go anywhere.
* In Java Collections Framework there are other interfaces besides Map - List, Set, SortedSet, Queue, Deque, SortedMap. Here we go.

Details:

* It will be quite enough to make only Map[String, Integer] support. You don't need a universal solution for any data types. For List, Set, etc. it will be enough to make List[Integer] or List[String]
* You can use any redis-solutions: standalone redis, sentinel or redis-cluster.
* You don't need to write your own library to work with Redis, you can use a ready-made one (for example, jedis).
* You should write in Java (version 21 and above) or Kotlin.
* The assignment must have a working main() method, to demonstrate how it works
* In general - do whatever you want, as long as it works.
* If you have any questions, feel free to write to <join-ecom@lightspeedhq.com>.
* The completed task should be placed on GitHub
