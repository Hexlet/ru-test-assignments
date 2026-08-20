> Локальная копия. Источник: <https://github.com/matic-insurance/assignment-test-import>

## Customer Import Platform

### Hi, there

One of the biggest banks in America decided to share its customer information with your company. The bank’s manager is going to send you a CSV file that includes details of customers. This information will be used to contact the customers in order to sell them insurance policies. But before that, you need to process the file and save all valid customers to DB.

#### Simple user flow

1. Open the application
2. Click to add a new import
3. Fill in a title, add a CSV file, press the ‘Submit' button.
4. After the file is uploaded and a new import is created - click on the 'Start import’ button.
5. Refresh the page and see the results of the import.

#### Application requirements

1. Users should be able to Create, Read, Update, and Delete imports.
2. The main page of the application should show a list of all imports and provide a link to add a new import.
3. New Import page should show a form for creating an import model: upload CSV file and import title.
4. After creating an import record, the admin must be redirected to the import details page.
5. Import details should display:
    * count of successfully created customers from files.
    * count of customers that were not created due to validation errors.
    * import status - created, started, completed. by default - created.
    * created at - time when import was created.
    * started at - time when import was started.
    * completed_at - time when import was finished.
    * 'Start Import' button. The button has to start processing the import file and create customers.
    * 'Delete Import' button.
    * Progress of import in percentage - this is not required but nice to have. This field should show the progress of processing import files, how many customers are created/failed at the moment. For example, you uploaded a file with tons of records. Processing all user data can take more than an hour, would be good to see the progress of the import (e.g. 46%).
6. first_name, last_name, email, date_of_birth fields are required and should be validated as:
    * Names not shorter than 2 symbols
    * Correct email format
    * Customer should be older than 18 years and younger than 100 years

#### General recommendations

* More tests are better 🙂 We are expecting tests for controllers, models(if needed) and business logic. Feature tests are desirable. (please use RSpec)
* It is not critical how the UI looks like. You can use any preferable UI library.
* Please, follow ruby/rails style guides.

You can find examples of CSV files in the *'import'* folder of this project. There are 2 files: 500 users and 100_000 users. Make sure you utilize both of them.

If you have any questions don’t hesitate to ask!
Please push the final code to Github and send us a link to the repo.

## Good luck and looking forward to seeing a finished project
