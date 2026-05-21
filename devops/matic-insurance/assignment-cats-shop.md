# Cats Shop

Small Sinatra application that returns information about cats available in the shop.

The application is a combination of plain text and JSON endpoints. Currently available endpoints

* `/` - hello page
* `/cats/info` - Read count of cats in database and presents info in readable text

## Assignment

Our company developed and released MVP of this application.
We envision a great potential for the app and would like to keep building it in a fast and reliable way.

In order to achieve stable and productive development, we rely on automated tests.
However, not all changes can be tested automatically so we would like to have a way to test merged code manually before it is pushed to production.

Help us build an automated pipeline for any pull requests that:

* Run automated tests on merged code with pull request target
* Deploy code to temporary server for manual testing
* Add comment to the pull request with link to the server
* Destroy server after pull request is closed

As you work on your solution you will inevitably have questions - please send all inquiries via slack. We are happy to assist and help

### Tools

You are free to use any tool, infrastructure, technology you would like. However, it would be nice to see how you can use **AWS** to solve the task.

### Requirements

We would like to see a solution that has following traits:

* Automation - who likes to perform manual steps?
* Configuration - how can we adopt a similar solution for other products/flows/technologies?
* Code - infrastructure/provision/pipelines as a code works the best to: be readable for all engineers, maintain a truth and avoid any hidden manual configurations.

### Setup and run application

#### Setup

Need ruby 2.7

* `bundle install` - install dependency
* Configure database in `config/database.yml` or pass configuration via `DATABASE_URL` (see section below)
* Specify `RACK_ENV` accordingly to the task you are running (see section below)
* `bundle exec rake db:create` - create db and run migrations
* `bundle exec rake db:migrate` - migrate db to latest version
* `bundle exec rake db:seed` - seed database with basic data

Then depending on what you want to do:

#### Run application

* `bundle exec rackup -p 1234` - Launch web application on port `1234`

#### Run tests

* `bundle exec rspec`

#### Environment variables

* `DATABASE_URL` - url to database e.g `postgres://{user}:{password}@{hostname}:{port}/{database-name}`
* `RACK_ENV` - environment for the app. possible values: `production`, `development`, `test`.
