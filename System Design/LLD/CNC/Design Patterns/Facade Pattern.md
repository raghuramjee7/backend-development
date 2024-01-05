# Facade Pattern

1. We use facade to hide the complexity of the system.
2. We should not enforce the use of facade pattern, it should be optional.
3. DAO is used to interact with the database. It has methods like create, read, update, delete.
4. The facade class has a **has a** relationship with the DAO class.
5. We create a facade class that runs a sequence of methods of the DAO class for an event to happen. 