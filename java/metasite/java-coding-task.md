# Coding assignment for a Java developer position

> Локальная копия. Источник: <https://github.com/Metasiteorg/java-coding-task>

Develop a Java-based application using preferred frameworks and libraries. Add source code to a source control (e.g. GitHub, Bitbucket etc). Send an email with a link to the source control and the hosted application (if any) to the <jobs@metasite.net>.

## Description

Develop an application capable of:

1. Parsing several text input files at once.
2. Counting the frequencies of all valid normalized words across all input files.
3. Saving the results (word and frequency) into data structures or files based on the first letter of the word: A-G, H-N, O-U, V-Z. Words should be sorted alphabetically.
4. Presenting the results to the user. E.g. prints data structures or files to standard output or provides API to download files or see data.

NOTE:

* *Text input* files should contain only ASCII characters. Application is not expected to work correctly if non-ASCII characters are present.
* *Valid word* is any sequence of alphanumeric and special characters. Words are separated by whitespaces. Character sequences that contain only numeric and/or special characters are not considered words. Words: R2-D2, a, (house), H&M, 3D. Non-words: 2022, 1+2=3, 10$.
* *Word normalization* is a process of upper-casing and trimming special characters from the beginning and the end of the character sequence e.g. (house) → HOUSE, a → A, H&M → H&M.
* Application is not expected to work correctly if more than one user is using it at the same time.

See the expected input and output in the [sample files](samples).

## Requirements

Implement the requirements in an **ascending order**.

### Minimum requirements

1. All functional requirements are fulfilled and the application works as described.
2. Provided code is clean, readable and well-structured.
3. Code has appropriate unit test coverage.
4. Application employs concurrency.

### Preferred requirements

5. Application is a web-application and exposes RESTful API which allows to upload multiple files and retrieve results.
6. All checked exceptions are handled and appropriate errors are displayed.
7. Application exposes Swagger UI.

### Bonus requirements

8. Application is hosted (e.g. Heroku, AWS, etc).
9. Application is containerized (e.g. Docker)
