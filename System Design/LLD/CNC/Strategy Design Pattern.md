# Strategy Pattern

1. When child classes have similar implementations, we can use the strategy pattern to avoid code duplication.
2. The strategy pattern is a behavioral design pattern that enables selecting an algorithm at runtime.
3. If we have a common function between two or more child classes, instead of code duplcation, we can create a common interface and implement it in the child classes.
4. Now, we create an interface, and then have various implementaions of the interface. We can then pass the implementation to the child class, and the child class can call the interface method. This interface can be a variable in the child class.
5. This way, we can have different implementations of the interface, and the child class can call the interface method, and the interface method will call the implementation of the interface.

