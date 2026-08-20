# Snowdog Front-end Recruitment test

> Локальная копия. Источник: <https://github.com/SnowdogApps/front-end-recruitment-test>

* Please use real Github accounts.
* We will not be responding to any questions about this test. All candidates will receive the same set of information for fairness.
* This test is not a representation of the tech stack we are using in real projects.

## Before you start

* Fork this repository; it needs to stay publicly available on Github.
* The test is based on [AdonisJS](https://adonisjs.com/), a full stack Node.js framework, but you don't need to write anything for the backend, nor have any experience with Adonis or similar frameworks.
* After installing the dependencies and running `npm run dev`, you should see a start page on <http://localhost:3333>. If something goes wrong, you are probably using the wrong version of Node.js.

---

### Task

Take a look at the [design](https://www.figma.com/file/ppND0SVAQm1A7H39jABzSp/Front-end-Recruitment-test). Your task is to:

* Recreate the checkout form and provide your own JS validation.
* Send validated form data to the `POST /order` endpoint and show a success / error message based on the REST API response.

### Hints

* Use any way of writing styles you are comfortable with.
* By default Adonis supports [PostCSS](https://docs.adonisjs.com/guides/assets-manager#setup-postcss), [SASS, Less and Stylus](https://docs.adonisjs.com/guides/assets-manager#setup-sass-less-and-stylus) and you need to enable one of them, but it's just Webpack under the hood, so feel free to hook whatever you like the most.
* Endpoint accepted data formats:
    * Postal code: 00000
    * Phone number: 000000000
    * Credit card: 0000000000000000
    * CVV: 000
    * Exp. date: 00/00

---

**Good luck 🤗**
