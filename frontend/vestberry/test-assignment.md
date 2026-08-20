# VESTBERRY Test Assignment

> Локальная копия. Источник: <https://github.com/VESTBERRY/Test-assignment>

## TASK

Your task is to create a simple page with a table of companies and a chart indicating the size of investments, based on the design created in photoshop.

You can start with the prepared project we have created and with our backend.

<img src="Assets/VB_Testovacie_Zadanie.png" width="45%" alt="Photoshop design" /> <img src="Assets/VB_Testovacie_Zadanie2.png" width="45%" alt="Photoshop design modal" />

## OBJECTIVES

* Try to get the template visual as close as possible to the design created in PSD, available also in Figma: (TODO: link)

* Make it possible to add a new company to the table (with its name, stage, sector and investment size)

* Adding new a company should also be reflected in the list of „companies by investment size pie chart“, and „companies by sectors statistics“

* Adding a new company should be done using a simple modal box (design included in PSD or Figma)

* Feel free to use any additional library you might need for completing this project, or to change the structure or anything

* We would like to see, how will you solve this task in terms of result precision, code quality & readability

## PROJECT STRUCTURE

```text
.
├── Assets                   # Assets and templates for this project
├── public                   # Static public assets (not imported anywhere in source code)
├── server                   # Express application that provides graphql backend
│   └── main.js              # Server application entry point
├── src                      # Application source code
```

## Requirements

* node `^12.0.0`
* yarn `^1.9.2` or npm `^6.2.0`

## Installation

After confirming that your environment meets the above [requirements](#requirements), clone `code` by following commands:

```bash
git clone git@github.com:VESTBERRY/Test-assignment.git <directory>
cd <directory>
```

When that's done, install the project dependencies.

```bash
yarn  # Install project dependencies (or `npm install`)
```

## Running the Project

After completing the [installation](#installation) step, you're ready to start the project!

```bash
yarn start  # Start the development server (or `npm start`)
```

While developing, you will probably rely mostly on `yarn start` or `npm start`; however, there are additional scripts at your disposal:

|`yarn <script>`        |Description|
|-----------------------|-----------|
|`start`                |Serves your app at `localhost:3000`|
|`dev-client`           |Starts the frontend part|
|`dev-server`           |Starts the backend part|
|`lint`                 |[Lints](http://stackoverflow.com/questions/8503559/what-is-linting) the project for potential errors|
|`lint:fix`             |Lints the project and [fixes all correctable errors](http://eslint.org/docs/user-guide/command-line-interface.html#fix)|
