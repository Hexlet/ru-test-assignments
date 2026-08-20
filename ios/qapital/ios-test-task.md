# iOS Test Task

> Локальная копия. Источник: <https://github.com/qapital/ios-test-task>
The test task is to implement a simplified version of our activity feed. The feed should implement fetch as you scroll with a page size of two weeks at a time. If you don't receive any events within that time period you should fetch the next period until you get some events or you reach the oldest activity.

* A Figma file with the design can be found here: <https://www.figma.com/file/Wvk9u2tO788Z8tojrxSIGh/iOS-Task?node-id=0%3A32>
* The fonts to use can be found in the `Fonts` folder in this repo

## Important

When you receive this task please estimate how long you will need to complete the task and when you will hand it in to us and reply to us as soon as possible. These two times do not have to be the same. You could for example decide that you need 20 hours to complete the task but because you are busy during the next few days you will not hand it in until next week. While completing the assignment write down how long it took. If it took longer than expected please reflect a bit about why when handing it in. Also, please respect the final due date that you have set.

Apart from implementing the actual view, here are a few pointers on what we are looking for:

* Reusability and testability
* Attention to detail when it comes to design
* Some kind of tests

While we don't require the solution to be perfect, we do expect it to be written in a professional manner. You should use this opportunity to show us what kind of code you would write if we were to employ you. **Furthermore, please take care in implementing the provided design.**

## Submitting

Just send us your code along with a description on how to run the app and the tests. If there is anything that you have not had time to complete or intentionally left out please reason on how you would implement it or why it was left out.

## Implementation

We provide you with a simplified API to get the list of activities and information about them. The API does not require any login. How you implement this and what external libraries you use are entirely up to you. Whats important to us is that the app is smooth and that scrolling does not have any stuttering.

The following API is available:

### Endpoint

<http://qapital-ios-testtask.herokuapp.com>

#### Fetch activities

```text
http://qapital-ios-testtask.herokuapp.com/activities?from=<date>&to=<date>
```

Where the two dates should be of the format YYYY-MM-ddThh:mm:ss+00:00. This will fetch all activities that happened between from and to. The return format is a JSON object that holds the list of activities under the key "activities" and a date indicating what is the earliest date there is an activity for under the key "oldest". The activities contain a message that has a number of words marked with `<strong>` that should be emphasized. The amount is in dollars. The user id can be used to fetch a user from the users endpoint.

```json
{
	"oldest": : "2016-05-23T00:00:00+00:00",
	"activities": [
		{
			"message": "<strong>You</strong> didn't resist a guilty pleasure at <strong>Starbucks</strong>.",
			"amount": 2.5,
			"userId": 2,
			"timestamp": "2016-10-04T00:00:00+00:00"
		},
		{
			"message": "<strong>You</strong> made a roundup.",
			"amount": 0.32,
			"userId": 3,
			"timestamp": "2016-10-03T00:00:00+00:00"
		}
	]
}
```

#### Fetch a user

```text
http://qapital-ios-testtask.herokuapp.com/users/<id>
```

Returns the user with the specified id

```json
[
	{
		"userId": 1,
		"displayName": "Mikael",
		"avatarUrl": "http://qapital-ios-testtask.herokuapp.com/avatars/mikael.jpg"
	}
]
```
