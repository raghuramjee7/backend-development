# Template Method Pattern

1. It is a behavioral pattern.
2. We use this pattern when we want a bunch of classes to follow the same algorithm, but the implementation of the steps in the algorithm can be different.
3. We create an abstract class with a set of a abstract methods, and a template method.
4. These abstract methods are the steps to be implemented in an order in the template method.
5. Now all the child classes implement the abstract method with their own implementation.
6. Then when they call the template method, the template method calls the abstract methods in the order defined in the template method.
7. The child classes cannot override the template method.
