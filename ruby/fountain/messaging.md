# SMS messaging threads: an OnboardIQ Rails test task

> Локальная копия. Источник: <https://github.com/onboardiq/test-tasks>

## Intro

OnboardIQ automates all of the tasks necessary to screen and hire for a large hourly workforce. By streamlining processes like scheduling for interviews & orientations, background checks, document uploading, electronic document signing, and training — OnboardIQ is an all-in-one hiring solution. Today, OnboardIQ powers hundreds of companies across the globe and processes thousands of applicants each day.

One of our popular features is a messaging system between applicants and account users (recruiters). It does not require the applicant to be signed up in any way — all messaging is done via SMS. When our user wants to contact an applicant (for example, to move the meeting and make sure the applicant can make the session, or to notify applicants about a recent job opening), we send the applicant an SMS using one of the popular SMS gateways. If there is a notification due (a meeting reminder), we send it the same way. When the applicant replies, we collect the answer using the same SMS gateway. This way, all messaging is stored in our database: both SMS contents and metadata fields.

What we want is to build an easy-to-use communications dashboard, where our users can easily track applicant replies, keep in touch with them and search information quickly. Note that all account users are able to see all the account messages (not just from/to them). In other ways, it should look very similar to Apple's iMessage app. This communications dashboard must be able to:

* organize all messages in threads, with messages associated to each applicant by unique phone number.
* mark an entire messaging thread as "read" or "unread".
* display thousands of messages for thousands of applicants — and be very quick to do this even when working with a slow (Heroku Postgres) database.

<img style="width: 100%" src="http://i.imgur.com/KreojW5.png" alt="A screenshot of what does it look like in a live product" />

In this skeleton repo, we have already created a table with dummy table structure for you. There are dozens of different ways to build this feature, and we'd like to assess your approach.

## Tech Stack

* Ruby 2.3+
* Rails 4.2+ (we are not using Rails 5 or micro-frameworks at this time)
* PostgreSQL 9.5+
* RSpec 3.0+ (you can use `shoulda-matchers` and `factory_girl` when needed)

You can also use ElasticSearch, Redis, and Memcached if you can finish the task faster and/or better this way. Please note that there are too many messages and message threads to fit into memory, so you cannot store them in Redis. Is is _not_ allowed to introduce other databases such as MongoDB.

You can use Bootstrap and jQuery for the user interface.

Please note that the system must behave really fast when used by multiple users at once, with accounts having tens of thousands of messages and message threads — all of this while on a potentially slow database.

## Instructions

Before starting the task, please read everything carefully and email us an estimation: how many hours are you planning to invest in the task and when it is due (for example, _"8 hours, you'll get it by Friday morning"_).

Start by bootstrapping the application and checking out the models and specs.

At all times try to stick to the best code possible: code that can live on for years. Use the patterns and code organization as you see fit, and please don't forget to write tests and question performance at every step.

## Scaffold Application

Included is a simple Rails 4.2 application with 3 main models. They represent 3 models from our main application — of course, they are very simplified and stripped of most functionality.

Use the usual `rake db:create; rake db:seed` to bootstrap the application.

Account represents a company signed with OnboardIQ. Account has a name, and that is about it. Account is represented by its users.

User is what you usually expect from a User model in a Rails application. Since authentication and authorization are not important in this task, we have skipped all fields and logic related to that.

SmsMessage is the model used to store all SMS messages. This is where it gets a little bit tricky. Every SMS message belongs to a certain account.

If the SMS message was sent by a user in our system, it would have a `user_id` field set. If it was sent by the system itself (as a reminder), it would have the `outbound` set to `true`, but would lack `user_id`. This way, we know that the message originated in our system if `user_id` is set or `outbound` is true.

`from_number` and `to_number` represent SMS metadata (from and to), and can be used for organizing threads. Other fields are mostly what we had in the database before we started to implement our messaging functionality — long before threads and everything.

You are free to modify models in any way, write additional specs, change functionality, introduce new tables and other PostgreSQL database structures.

## Task Requirements

Implement a threaded system for messages. You can add as many new models as you like or modify existing models. But please note that there is external code that puts SMS messages into the existing table, so existing fields should not be changed: please use callbacks or additional models instead. Optionally, you can use additional systems as noted in _Tech Stack_.

1. Make sure that messages are displayed in threads. I should be able to click on a thread to see all the messages in that thread. The thread should be identified by applicant's phone number. All threaded messages should be in chronological order. As a user, I can view all messages in the account — not just the ones sent by me or to me.

2. Implement the mark as read/mark as unread system: as soon as I open the thread, it should be marked as read; I could also mark it as unread by pushing a certain button. Note that we are tracking the "read" status of the whole thread, and not single messages now.

3. Implement an "unread" counter in the layout: on every page of the app, a logged in user should be able to see the number of unread threads in his account. Take special attention to performance here.

4. Let's do the scaling test now. First, come up with a piece of code that can create a lot of fake threads with a lot of fake messages to test out the speed of our system and usefulness of the interface.

When there are lots and lots of messages, do they load really fast? Is there a way you can only load a certain amount of threads every time instead of loading them all? As a user, I would usually only like to see the latest threads, but I should also be able to navigate easily to older threads. What would be the best way for the user — and for system performance — to do this?

5. Let's do the performance testing now. Try to generate even more messages and check if the system can handle it. What is there to improve? Let's not forget that the system can run on a DBMS with really bad disks (IOPS), as opposed to your blazing fast laptop SSD.

### Optional tasks

6. Allow users to select multiple applicants and send out "broadcast messages." These broadcast messages should be grouped under a single thread, similar to how iMessage treats group messages. However, when an applicant responds, it should display the response in that particular applicant's individual thread.

7. Is there a way to check production-level performance of the application on public cloud? Bonus points if you can slow down your Postgres to simulate bad I/O without deploying to Heroku every time just to check.
