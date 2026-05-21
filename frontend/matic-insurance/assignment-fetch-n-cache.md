# Matic Test assignment

​
Our intent is to get a feel for your thought process as well as your source code organization and testability.

​
It's not required that you solve all of the problems / tasks in this document. We value your time and efforts. Feel free to skip any part of this assignment while still giving us a chance to enjoy the results of your work that best demonstrate your skills and code style.

​
We would like to know the approximate time you spent on the solution. We do not take time of submission into account in our overall evaluation.

​
We expect to see source code as a git repository with instructions on how to use it. The test task has to be public for easy access.

_Please let us know if you have any questions._
​

## Task: Fetch ‘n’ Cache application

* The user should be able to fetch Rick and Morty character by entering a numeric value into the search field and clicking on the Search button.
* Disable the button and search field when there are network requests in progress
* If the character was fetched before, it should be loaded instantly from the cache (no redundant AJAX requests).
* Show a list of cached characters on the right side of the page
* If a user clicks on an image of the character, display the character on the screen
* Highlight the selected character in the cached list if that character is currently on the screen
* Allow the user to clear the cache entirely by clicking on the Clear All button
​

### BONUS tasks

* Allow the user to clear certain characters from the cache by clicking on the X button
* When the input field contains an id of the character that is on the cache, instantaneously display the cached data on the screen
* Cache all data in the browser memory (so that it persists after reload)
* Experiment with automatic cache invalidation after some period of time
* The code is covered with automation tests

[Figma Mockups](https://www.figma.com/file/UeAY9vlFmBAqUoMb6H3n77/Matic-Test-Assignment%3A-Fetch-and-Cache?node-id=0%3A1)

<code>GET [https://rickandmortyapi.com/api/character/:id](https://rickandmortyapi.com/documentation/#character)</code>
