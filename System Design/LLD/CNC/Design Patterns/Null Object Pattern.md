# NULL Pattern

We use this to handle null pointer exceptions. We create an abstract class specifying various operations to be done, concrete classes extending this class and a null object class providing do nothing implementation of this class and will be used seamlessly where we need to check null value.  

We need this to handle cases where null objects are passed, we cant keep writing if statements for every function to check if the sent object is null or not.

## Implementation
1. For each abstract class, we create all the concrete classes, also we create a null object class that extends the abstract class and provides do nothing implementation of the class.
2. 
