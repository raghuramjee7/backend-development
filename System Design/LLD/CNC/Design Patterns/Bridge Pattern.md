# Bridge Pattern

1. Bridge pattern decouples abstraction from implementation so that both can vary independently.
2. We have an interface that has a method.
3. Now, we can implement this interface in concrete classes, and each concrete class will have its own implementation of the method.
4. Now, lets say we need a new implementation of the method, we cannot do it unless we create a new concrete class.
5. To solve this problem, we create a new interface with the method and implement it in concrete classes, we have various implementations of the method for the bridge interface.
6. This bridge interface is a member of the original interface, and we can change the implementation of the method by changing the bridge interface.
7. Now, we can have mutliple implementations of the method, and we use whatever implementation we want in the original interface.