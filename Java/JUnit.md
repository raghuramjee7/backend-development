# JUnit

1. JUnit5 is the latest version of JUnit. It is completely different from JUnit4.
2. JUnit5 is composed of three modules: JUnit Platform, JUnit Jupiter, and JUnit Vintage.
3. JUnit Platform is the foundation for launching testing frameworks on the JVM.
4. JUnit Jupiter is the combination of new programming model and extension model for writing tests and extensions in JUnit5.
5. JUnit Vintage provides a test engine for running JUnit3 and JUnit4 based tests on the JUnit Platform.

## Basics
1. Create a maven project and add the following dependencies in the `pom.xml` file.
2. Good convention is to create a test class with the same name as the class under test and append `Test` to it. All functions inside it can have the same name as the functions in the class under test with the word test as their prefix.
3. We use `@Test` annotation to mark a method as a test method.
4. We use different annotations like `@BeforeEach`, `@AfterEach`, `@BeforeAll`, `@AfterAll` to run code before and after each test method or all test methods.
5. We use `Assertions` class to perform assertions in JUnit5.
6. We use different types of assertions like `assertEquals`, `assertNotEquals`, `assertTrue`, `assertFalse`, `assertNull`, `assertNotNull`, `assertArrayEquals`, `assertIterableEquals`, `assertLinesMatch`, `assertTimeout`, `assertTimeoutPreemptively`, `assertThrows`, `assertAll`, `assertThat`, `fail`.
7. We can group assertions using `assertAll` method. We can write asserts in one test method and group them using `assertAll` method.
8. We can use maven surefile plugin to get a detailed stack trace of all the errors, to use this, simply add the dependency to the `pom.xml` file.
9. `assertEquals` takes a third parameter which is used as a descprtion when a test case fails
10. We can use lambda exp as third parameter which returns the desc string, but in this case, the lambda fn will only run when the test case fails, earlier, the string ran no matter what the result is, so this is optimal.
11. `assertEquals` checks the reference variable, for stuff like arrays, use `assertArrayEquals`
12. We can check if the flow of logic raises certain exceptions using `assertThrows` method. 
13. We can use `assertTimeout` method to check if a method runs within a certain time limit.
14. For assets like timeout and throws the parameters is of type (exception/time, ()-> functon to test)
15. We can use `@DisplayName` annotation to give a custom name to the test method.
16. We have annotations like `@BeforeEach`, `@AfterEach`, `@BeforeAll`, `@AfterAll` to run code before and after each test method or all test methods. `@BeforeAll` and `@AfterAll` methods must be static.
17. If there are n tests in a class, n instances of the class are created. If we want to create only one instance to run all the tests, we can use `@TestInstance(Lifecycle.PER_CLASS)` annotation. The default value is `Lifecycle.PER_METHOD`. If per class is used, `@BeforeAll` and `@AfterAll` methods can be non-static.