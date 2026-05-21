## Test task for TypeScript/Vue.js developer in Ecwid

## Goal

Write an application that contains three pages:

* A page with a list of categories and products
* product page
* shopping cart page

### Data

Store data must be accessed using [Ecwid REST API](https://api-docs.ecwid.com/reference/rest-api)

The easiest way is to use a demo store. It's access info is like this:

* StoreID: 108362264
* Token: public_RiNvjTVVzKLhFNWyzR5fNY68u1GMHLEs

### Page «products and categories list»

The page contains a list of products and categories in any convenient format: grid, list table.

Category page content:

* category name
* category image

Product page content:

* product name
* product price
* product image
* buy button

#### Opening category details

When you click on a category, the app takes you to a page with subcategories and products belonging to that category.

#### Opening product details

When you click on a product, the app goes to the Product Details page.

### «Product details» page

The page contains details about the product:

* product name
* product description
* product image
* product price
* buy button

### «Buy» button

The button adds an item to the "cart"
Shopping cart - any local storage with a list of added items.

### «Cart» icon

All pages display a cart icon with the number of items added to it. When you click on the icon, the application goes to the "Shopping cart" page

### «Cart» page

The page contains a list of added items and the "Place order" button.
Any item in the list can be deleted by clicking on the "Delete" button.

### Page navigation

The page state is displayed in the url. When you navigate to a url, the page that belongs to that url is displayed.

### «Place order» button

When you click on the button, a text congratulating you on your purchase is shown.

## Technologies

* Typescript
* VueJS
* HTML/CSS

## Design

Pages should look nice and readable. You can use any CSS framework.

## Code sharing platform

You can upload the code to your GitHub/Bitbucket or use the Web IDE: <https://codesandbox.io>.
