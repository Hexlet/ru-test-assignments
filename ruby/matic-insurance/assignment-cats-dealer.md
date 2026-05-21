# Cats Dealer

==================

## Hi, there

You are going to create a simple service that allows finding the best cat with the best price for customer location.

There are cat shops that have pricelists accessible via REST API. What your service will do is just get prices from each shop, compare them and suggest the best deal for a customer!

We created 2 fake test shops for you.

1. "Cats Unlimited" API (JSON response) - [https://nh7b1g9g23.execute-api.us-west-2.amazonaws.com/dev/cats/json](https://nh7b1g9g23.execute-api.us-west-2.amazonaws.com/dev/cats/json)
2. "Happy Cats" API (XML response) - [https://nh7b1g9g23.execute-api.us-west-2.amazonaws.com/dev/cats/xml](https://nh7b1g9g23.execute-api.us-west-2.amazonaws.com/dev/cats/xml)  

As of now, service only supports "Cats Unlimited" integration. On top of that, existing code was written by Trainee Ruby developer and could use some refactoring.

### The task is the following

1. Implement "XML" integration, and improve business logic to find the best deal amongst two shops.
2. Make service an API-only. Let's remove FE implementation.
3. Refactor or rewrite the existing code. We wanna see a clean design, readable code, good test coverage.

#### Things to watch out for

* Right now our product supports only two cat shops. However, that can change in a future.
* As you know, 3rd-party integrations often behave unpredictably. Let's make sure that our product can handle errors from these services.

### Good luck and looking forward to seeing a finished project
