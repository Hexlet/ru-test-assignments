# Flutter interview – test task

> Локальная копия. Источник: <https://github.com/smartlook/smartlook_flutter_interview_test_task>

## Element tree

The Flutter framework is rendering all application views directly to the GL layer, so it's hard to extract the application's elements tree directly.

Smartlook SDK heavily relies on the view tree "knowledge" so your "job" in this interview task is to obtain the view tree on Flutter.

## The solution

* Clone the project at <https://github.com/smartlook/smartlook_flutter_interview_test_task>
* In the file `movie_streaming_app/lib/main.dart` there is a method [_startServer()](https://github.com/smartlook/smartlook_flutter_interview_test_task/blob/936542713899508573c344ff3ce7136d08666d86/movie_streaming_app/lib/main.dart#L42) with a simple embedded `HTTP` server running on port `9000` and a mocked request handler returning a sample `JSON`
* Your task is to write a function that gets the elements tree of the currently rendered screen from Flutter and return it as `JSON` instead of the mocked one.

## Format

Each item of the list should correspond to one element currently visible on the screen and should contain these properties:

* `top` – the top coordinate of the element on the screen
* `left` – the left coordinate of the element on the screen
* `width` – the width of the element
* `height` – the height of the element
* `color` – color of the element, this should be for example, background color of plain view or text color of a text element

## Credits

The testing app is `movie_streaming_app` from the [awesome-flutter-ui](https://github.com/Chromicle/awesome-flutter-ui) project released under a MIT license.
