Sometimes you want to make a complete copy of some object.

Something like this:

```java
ComplexObject obj = ...
ComplexObject copy = CopyUtils.deepCopy(obj);
```

The problem is that classes in Java can be of arbitrary complexity - the number of class fields and their types are not regulated in any way.
Moreover, the type system in Java is closed - elements of an array/list can be absolutely any data types, including arrays and lists.
And also there are recursive data structures - when an object somewhere in its depths contains a reference to itself (or to a part of itself).

You need to write a deepCopy() method that takes all these nuances into account and works on objects of arbitrary structure and size.

Some details:

* If you have any questions, feel free to write to <join-ecom@lightspeedhq.com>.
* First of all, the method should work correctly. Speed is also important, but not as much as correctness
* You can only use the features of the standard J2SE library
* Code should be written in Java (version 21 and above) or Kotlin.
* The assignment must have a working main() method, to demonstrate how it works
* The completed assignment should be posted on GitHub

P.S. I know about hacks with `java.io.Serializable` and `java.lang.Cloneable`, please don't use them

---

Before submitting, I recommend testing the solution on a class like this:

```java
class Man {
	private String name;
	private int age;
	private List<String> favoriteBooks;

	public Man(String name, int age, List<String> favoriteBooks) {
		this.name = name;
		this.age = age;
		this.favoriteBooks = favoriteBooks;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public List<String> getFavoriteBooks() {
		return favoriteBooks;
	}

	public void setFavoriteBooks(List<String> favoriteBooks) {
		this.favoriteBooks = favoriteBooks;
	}
	
}
```
