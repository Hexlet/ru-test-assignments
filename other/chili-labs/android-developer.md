# Android developer

> Локальная копия. Источник: <https://github.com/ChiliLabs/test-tasks>

## The Task

Build a GIF search application using the Giphy API

## Primary Requirements

### Stack

* **Language**: Kotlin;
* **UI**: Compose;
* **Architecture:** MVVM or MVI;
* **Dependency Injection:** Hilt or Koin;
* **Network:** Retrofit or Ktor;
* **Async:** Coroutines.

You may use additional libraries at your own discretion, but the core technical stack should be based on the libraries listed above.

### Functional Requirements

* Auto search with debounce (e.g. 300–500ms after user stops typing);
* Pagination: load more results when scrolling;
* Support for vertical and horizontal orientation;
* At least 2 screens: search screen and gif details screen (opened on item click);
* GIFs must be rendered as animated images (not static previews/thumbnails);
* Results are displayed in a grid;
* Loading indicators (initial load and pagination);
* Error handling and display (e.g. API errors, no internet connection);
* Support for light and dark themes;
* Unit tests for core logic (as much as you see fit);
* Each screen must include at least one Jetpack Compose Preview (@Preview) for the screen.

## Bonus points

* Clean Architecture or similar approaches (reasonable abstraction, no overengineering);
* Use of a multi-module architecture;
* Network availability handling (e.g. offline state indication);
* Ability to produce optimized release build.

## Notes

* No time limit. Quality > Speed;
* Documentation (<https://developers.giphy.com/docs/api/>);
* UI is up to interpretation. Only the requirements listed above are mandatory;
* If any of the primary requirements cannot be completed, it must be commented what solutions were attempted and what problems were encountered.

## Contact

* Please reply either directly to the e-mail that was sent to you or to <studio@chililabs.io>. The task must be attached as a link to a repository with public access. If you haven’t done so previously, please also attach your CV.
