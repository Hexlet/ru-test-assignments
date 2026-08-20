# Simple Form Builder

> Локальная копия. Источник: <https://github.com/onboardiq/test-tasks>

Congratulations! If you are reading this, we like you a lot and want to see if there's a possible fit between you and our team.
In this task, we ask you to build a simple form builder (i.e. a frontend UI to dynamically generate a form).

## Introduction

Imagine we have a project where users must fill in a survey to tell more about themselves: their job skills, general profile, etc. Managers can create a variety of forms the different type of users.

Your task is to implement the UI which allows the manager to design a new form using some predefined — and some custom fields. We will call it Form Builder.

Please look at the attached designs.

### Required features

Form Builder user interface has two main parts: a block with available form controls and a live preview of the form fields.

* Fields can be of a different type. Here is the exact list of possible field types: input, textarea, checkbox (multiple answers), radio (multiple answers), select and file (file upload control).
* Once field is added via the controls block, it should be visible in the preview section in live mode.
* User can also configure form fields in the preview section. Here a list of customizations to the field:
    * change the field name
    * mark field as "required"
    * rearrange fields order using drag-n-drop
    * ability to add, delete and edit option title for fields that have multiple answers
* Also, there should be a validation for the following types of errors:
    * field names should not be blank
    * field names should be unique
    * fields with multiple answers should have at least one option available

### Other requirements

* Use ReactJS (optionally with Redux)
* Use BEM style guide for CSS (<http://getbem.com/introduction/>)
* Ask questions
