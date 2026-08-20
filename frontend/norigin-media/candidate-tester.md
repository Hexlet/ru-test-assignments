> Локальная копия. Источник: <https://github.com/NoriginMedia/candidate-tester>

## Candidate-Tester

This Repo is intended to instruct new Frontend developer (Native & Web) candidates on the steps to follow for completing the Norigin Media testing task.

---

### What we want to assess

* Your coding skills.
* Intuition for design & UX.
* Multi Screen / Cross Browser allocations.
* Platform, Framework & Tooling knowledge.
* App packaging and production readiness.

#### Requirements

* Build a single screen web or native application (**EPG Screen**) using your choice of framework / tooling

  **NOTE:** For *Web Developers*: React, Vue.js, React-Native, Vanilla JS / Typescript, for example - No restrictions apply, however, try to avoid using project generators / starter-kits / sample projects where possible.

  **NOTE:** For *Native Developers*: Java, Kotlin, ObjectiveC - No restrictions to tooling or frameworks apply.

* Use the designs in the `./mockups` folder to guide your work.
* Use **Mock-Api** package included to supply the EPG data. See `package.json`. (Images URLs might be outdated, please find alternative channel images)
* For Web developers task submission is expected to be as a Github repo with simple steps to install and run. Pass the link to your contact with our management or your recruiter when you're done.

  **NOTE:** For *Native Developers*: Alternative methods of submission are acceptible for Android & iOS projects.

* Task is not expected to take any more than 2 days of your time.

* A base level of interactivity is expected regarding the progression of time and how this is reflected in the EPG. For example the yellow line indicating the current program should update and change, as well as a functional auto-scroll shortcut to be triggered when pressing on the "NOW" button.

#### Cool to have (But not required and wont negatively impact assessment)

* Add more interactions, animations or just nail the UX.
* Responsive layouts for multi-screen support.
* Make performance and optimization considerations.
* Additional screens using mock data api.
* Additional EPG showing an alternative layout.
* Use Spatial Navigation to enable remote control navigation through items

---

## Design Example

We have included some mockup designs to act as a guide. You can find them in the `./mockups` folder.

Example EPG design:

![alt text](https://raw.githubusercontent.com/NoriginMedia/candidate-tester/master/mockups/EPG_small.png "Logo Title Text 1")

NOTE: Additional screens are optional and only if you really want to impress us with your skillz (Yes.. with a Z) should you add them to your app.

---

## Mock-API

We have provided a basic mock api to supply EPG data for this task.

This is packaged as a standard Node NPM module. To install simply run: `-> npm install` from the project root directory.
Of course Node.JS should be installed beforehand. For Native Developers not familar with NPM here is the [NPM Documentation](https://docs.npmjs.com/getting-started/installing-node)

To run the update & run mock-api server execute the command below:

```text
-> npm run start
```

You should see the server start on port 1337.

```text
Mock service running at http://localhost:1337
```

You can now request data from the mock-api:
`Try It: http://localhost:1337/epg`

For additional information you can find the package and the documentation here: [Norigin Mock-API](https://github.com/NoriginMedia/mock-api/tree/cloudberry)

---
