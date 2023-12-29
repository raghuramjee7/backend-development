# Decorator Pattern

1. The decorator pattern is used to add new functionality to an existing object without changing its structure.
2. Decorator pattern is used to solve the problem of class explosion.
3. In decorator pattern, we have a base class, and we have a decorator class, both of which are abstract.
4. The decorator class has a reference to the base class and it also implements the base class. 
5. Decorator implements the base class because, at the end even this is a base class object and it can be decorated over and over
6. We have a reference to the base class because we need to pass the base class object to the decorator class so that it can upgrade it
7. This way, we can recursively upgrade the base class object
8. Decorator pattern is also called as wrapper pattern
9. Decorator pattern has both is-a and has-a relationship