# Kittens Store

Small Sinatra application that returns information about cats available in the store.

The application is a combination of plain text and JSON endpoints. Currently available endpoints

* `/` - hello page
* `/kittens/info` - Read count of kittens in database and presents info in readable text

## Assignment

Our company developed and released MVP of this application.
We envision a great potential for the app and would like to keep building it in a fast and reliable way.

In order to achieve stable and productive development, we rely on automated tests. However, not all changes can be tested automatically so we would like to have a way to test merged code manually before it is pushed to production.

Help us build an automated pipeline for any new code merge/commit that:

* Build application artifact by writing dockerfile(s) and store the image in container registry (e.g DockerHub)
* Using docker image, speenup temporary environment and run automated tests on merged code
* Deploy code to temporary server for manual testing

As you work on your solution you will inevitably have questions - please send all inquiries via Slack. We are happy to assist and help

### Tools

There are no limitations to using some particular technology or tools. However, it would be nice to see how you can use **AWS** and **Terraform** to solve the task.

### Requirements

We would like to see a solution that has following traits:

* Automation - who likes to perform manual steps?
* Configuration - how can we adopt a similar solution for other products/flows/technologies?
* Code - infrastructure/provision/pipelines as a code works the best to: be readable for all engineers, maintain a truth and avoid any hidden manual configurations.

### Setup and run application

#### Setup

Need ruby 2.4.9

* `bundle install` - install dependency
* Configure database in `config/database.yml` or pass configuraton via `DATABASE_URL` (see section below)
* `bundle exec rake db:create` - create db and run migrations
* `bundle exec rake db:migrate` - migrate db to latest version
* `bundle exec rake db:seed` - seed database with basic data

#### Run tests

* `bundle exec rspec`

#### Run application

* `bundle exec rackup --port 1234 --host 0.0.0.0` - Launch web application on port `1234`

#### Environment variables

* `DATABASE_URL` - url to database e.g `postgres://{user}:{password}@{hostname}:{port}/{database-name}`
* `RACK_ENV` - environment for the app. possible values: `production`, `development`, `test`
