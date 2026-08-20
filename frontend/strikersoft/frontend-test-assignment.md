> Локальная копия. Источник: <https://github.com/Strikersoft/strikersoft-frontend-test-assignment>

### Demo app is available [демо приложения](http://strikersoft.github.io/strikersoft-frontend-test-assignment/)

## Initial setup

1. Fork this repo & clone to a local machine;
2. Make sure you have node & npm installed;
3. Install Node packages: `npm install`;
4. Run the dev server: `npm start`.

## Data

You have an JSON-formatted input data, which should be downloaded from the server using an AJAX request.
The data is an array of uniform objects, which look like this:

```javascript
{
    "id": 0,
    "name": "Chad Snyder",
    "age": 28,
    "phone": "(629) 653-9041",
    "image": "owl",
    "phrase": "Owmeco jen be tezpoksim vojuz..."
}
```

Every object describes a person: his internal id in the system, the name, the phone number, his age, his profile pic and a catchphrase. The dataset’s length could vary - you should be ready to process an array from 1 to 200 objects. Here you’re in control of the JSON file, but remeber, that a real application could have a dynamic set of data.
You’ll also need the thumbnails for each person, the proposed set could be found here.

## Displaying the data

After the data is fetched, the table should be formed. Each row should represent a single person - his thumbnail, his name, an age and a phone number. The table data should be sortable and searchable. Besides the table, the sidebar should be implemented, which should display more detailed data for the selected user - all of the data from the table plus a catchphrase. The first row is selected by default. Clicking a row makes the row selected.

## Searching

Searching by `name` field should be implemented. Search field is a normal text input. On input to a search field the table should be automatically updated, showing people, whose name contains the entered substring. Sidebar should be updated dynamically to point to the new user at the last position.
Please check the behavior validity for erasing the characters. The table should still be sorted.

## Sorting

User table should be sortable by name or by age. For achieving this, a small toolbar with two dedicated buttons is present. Sorting should be available for both ascending and descending order.
Important: the sorting should be applied to a currently used data set - only the displayed data should be affected.
Another thing to remember is that applying sorting should refresh the displayed user in the sidebar.

## Proposed technology stack

The assignment does not impose any specific requirements to the technology stack, however, it is recommended to use ReactJS/Webpack. Using ES2015 /w Babel would be a huge plus.
This repo is a nice starting point for all.

## Source code

Make a pull request to this repo.

## Deployment

Any hosting of your choosing. GitHub Pages is a reasonable choice if you're using GitHub.
This repo contains a helper script to simplify deployment to GitHub Pages - just run `npm run deploy`, and ensure your app is up & running at <your-username>.github.io/strikersoft-frontend-test-assignment/.

## Summary

1. Download the data via an AJAX request;
2. Draw the table from the data. Draw the sidebar with the current person;
3. Add the search by name;
4. Add the toolbar for sorting.

That’s it!
