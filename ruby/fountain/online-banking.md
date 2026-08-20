# Online Banking

> Локальная копия. Источник: <https://github.com/onboardiq/test-tasks>

We would like you to try this short task and show us your Rails chops! If you are ready, please take a look at the following requirements carefully and feel free to start making ANY changes to the skeleton app. We expect the entire task to take about 1 hour. Make sure to read the document completely before starting. Feel free to leave comments in your code whenever necessary.

## Setup

```text
$ bundle install
$ bundle exec rake db:setup
$ rails s
```

### Your task

Spend an hour to make a service where users can transfer money to one another. We provide you with a skeleton app and below are the structure and list of `TODO` (hint: try global searching `TODO`) items for you. Your first goal should be making all the features work. Then, you can try to clean up and optimize your code during the remaining time.

#### Controllers

* MoneyTransfersController
      * TODO: MoneyTransfer#create:
          * Use `sender`, `receiver`, and `amount` as arguments
          * User A can send User B money iff User A has enough balance at the time User B accepts the transfer
      * `MoneyTransfers#index` should show all historical money transfers
* UsersController
      * TODO: `Users#show` should show the money transfers between `current_user` and the `User.find(params[:id])`)

#### Views

* TODO: fill in the `#TODO` items inside `views/users/show.html.erb`
* TODO: fill in the `#TODO` items inside `views/money_transfers/index.html.erb`

#### Models

* MoneyTransfer Model
      * TODO: optional
* User Model
      * TODO: optional

#### DB

* MoneyTransfers Table
    * `sender_id:integer`
    * `receiver_id:integer`
    * `amount:float`
    * TODO: optional
* Users Table
    * `email:string`
    * `password:string`
    * TODO: optional

#### Other considerations

* Expect thousands of requests / sec
* Write spec with RSpec (we encourage TDD)
* Feel free to modify the code as you see fit
      * Hint: do you have to modify the models and DB tables?

### How to submit

When you are done, please zip everything and send it to your point of contact.
We will review your submission and get back to you if there's a good fit!
