# KazanExpress test for Python developer 
Here lies the description and requirements of the test task for Python/Django Developer position applicants.

## Task goal
The goal of this test task is to develop a simple Django admin panel which purpose is to manage the content for an online store and to have multi-role support. 

## Domain description
The following image represents the class diagram that should be considered during development of your admin panel. This is the minimal requirements for classes and fields that we are expecting from you to add. You can make your own updates and add additional functional. All images fields should be represented as links on images. You are free to use any database, which seems suitable for you and for the project. 

![Class diagram](https://hb.bizmrg.com/kazanexpress/class_diagram.png)

## Requirements
### Shop admin
1. Navigate through the shops list.
2. Make a search by title.
3. Edit everything except shop id.
4. Upload image as shop pic. 

### Product admin
1. Navigate through product list.
2. Search by id or product title.
3. Edit everything except product id.
4. First image should be displayed as main image in both list view and product view.
5. Sort products in product list by number of orders and by price.
6. Filter list of products by active flag.
7. Filter by price range.
8. Attach product to one or more categories.

### Category admin
1. Navigate through categories list.
2. Search by product id, title and parent category.
3. Add one or more parent categories. 
4. Display all possible paths to chosen category. 

### Management
There should be at least two administrative roles for the following purposes:
1. Moderation for products. 
2. Moderation of all available pages. 

## Submission
Fork this repository, prepare your solution and make a pull request when you're done.
Don't forget to write docs :)

## Good luck!
