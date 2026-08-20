# Back-end developer

> Локальная копия. Источник: <https://github.com/ChiliLabs/test-tasks>

## Main task

Create a RESTful service with the following functionality:

* Registration with identifier and password. Nickname, email or phone can be used as a user identifier, confirmation is not required. Auth token(s) must be returned on success.
* Login with identifier and password. Auth token(s) must be returned on success.
* Profile retrieval, returning current users information.
* Avatar upload (requires auth). Uploaded image URL must be returned on success.
* WebSocket connection endpoint (requires auth). After connecting to it client must receive messages when the avatar is changed.
* User deletion (requires auth). Success must be returned if a user is fully deleted (registration and avatar). All socket connections must stop, the user must not be able to log in with any previously issued auth tokens.
* Use stateless authentication (JWT).
* Use [JSend](https://github.com/omniti-labs/jsend) for response format.
* Generate an easy-to-use and understand documentation for the API (Swagger UI, Apiary and the like).

### API expectations

The API is expected to have the following endpoints accepting an returning _at least_ values with the specified names:

* `POST /api/register` accepting an `identifier` and `password`, returning an `accessToken` and `refreshToken` (if implemented).
* `POST /api/login` accepting an `identifier` and `password`, returning an `accessToken` and `refreshToken` (if implemented).
* `GET /api/user` returning `identifier`, `avatarUrl` and `registeredAt`
* `POST /api/user/avatar` accepting an `avatar` file, returning an `avatarUrl`
* `DELETE /api/user`
* `ws://{host}/ws` accepting websocket connections
* (optional): `POST /api/refresh` returning an `accessToken` and `refreshToken`
* (optional): `GET /{avatarUrl}` returning the image

### Tech stack

Java / Kotlin, Spring Boot, SpringDoc is a good baseline if you don't know what to pick, since this is what we use the most. Any Relational or NoSQL database will do.

Can use other OO, strongly typed languages or other frameworks if you are more familiar with them but please do not choose something exotic. While your fully-featured COBOL webservice might be extremely impressive, we probably will not enjoy reviewing your code 🫠

### Time limit

There is no time limitation for the task, we favour quality over speed.

### Bonus points

* Dockerfile / Docker compose file & ability to run the service in 1 command on a machine with nothing but docker and docker-compose installed
* [OAuth 2.0](https://oauth.net/2/) compliant authentication (access / refresh token pair)
* Unit tests (we don't expect 100% coverage but rather see how do you approach testing)
* Integration tests against an in-memory database
* Some way to access the uploaded user avatar image (without authentication)

### Notes

Some requirement points can be skipped if you feel like they are too complex at the time. Please provide a comment in the code about what has been skipped. We do expect all or most of the requirements implemented if applying for a more senior position.

⚠️ **Important**: It is ok to re-use parts of code from other sources. But it is crucial to understand it and to be able to explain what it does, as well as to attribute the original author (human or otherwise).

## Contact

Please reply either directly to the e-mail that was sent to you or to <studio@chililabs.io>. The task can be attached as a link to a repository or an archive. If you haven’t done so previously, please also attach your CV.
