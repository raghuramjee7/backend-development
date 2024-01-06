# Flyweight Pattern

1. It is a structural pattern.
2. It helps in reducing the memory footprint of the application by sharing the common data across multiple objects.
3. This patern is used in creating text editors, IDEs, etc.
4. We use this pattern when memory is limited, when objects share the data, creation of object is expensive, and the identity of the object is not important.
5. Intrinsic Data: Data that is common and shared across multiple objects.
6. Extrinsic Data: Data that is unique to each object.
7. How flyweight pattern solves the issue steps:
    1. Remove all extrinsic data from the object and keep only intrinsic data in the class.
    2. Then the class we get after removing the extrinsic data is called flyweight class, and we make this class immutable.
    3. Extrinsic data is passed to the flyweight class when it is needed by a separate constructor
    4. Once the flyweight object is created, it can be cached and reused.
8. We build a factory class that will create the flyweight objects and cache them.
9. Basically, we make the flyweight class singleton and the extrinsic data is passed to the flyweight class when it is needed by a separate method.
10. 