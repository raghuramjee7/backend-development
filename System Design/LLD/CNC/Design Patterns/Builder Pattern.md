# Builder Pattern

1. This is a creational pattern.
2. This is used in classes where there are too many optional frields in the class, we need too many types of constructors and the signature of the constructors clash (constructor for just taking name as str - name can be name or mothername)
3. It is a step by step object creation pattern.
4. For a complex class, we create another class called builder class.
5. Builder class has all the optional fields of the complex class, we have setter methods for each of the optional fields.
6. Now, when we want to create an object of the complex class, we create an object of the builder class and set the optional fields using the setter methods, and then pass this object to complex class constructor.
7. We have a build() method in the builder class which returns the object of the complex class.
8. We have a director class which has a method which takes the builder object and calls the setter methods of the builder class and then calls the build() method of the builder class and returns the object of the complex class. This method has the order of setting the optional fields.