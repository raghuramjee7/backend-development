# Proxy Pattern

Whenever we want to add some additional functionality to an existing class, we can use the proxy pattern. The proxy pattern creates a wrapper around the existing class and provides additional functionality, like logging, security, etc.

## Use cases
1. Internet Proxy
2. Caching
3. Preprocessing and Postprocessing

## Implementation
1. We have an interface with an implementaion, say employee interface and employee class.
2. For the same interface, we create a proxy class, which implements the same interface.
3. The proxy class has an instance of the employee class.
4. The proxy class has additional functionality, like logging, security, etc.
5. We implement all the functions of the interface in the proxy class, and add addtiona functionality to it.