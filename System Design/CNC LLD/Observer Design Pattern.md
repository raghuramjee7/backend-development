# Observer Design Pattern

1. There are two objects, one is the subject (observable), and the other is the observer.
2. Whenever there is a state change in the subject, all the observers are notified.
3. There is an observable interface, and an observer interface.
4. In the observable interface, we have a list of observers, and methods to add, remove observers and notify observers and also to set data.
5. In the observer interface, we have a method to update the observer.
6. An observable has multiple observers, and when the state of the observable changes, all the observers are notified.
7. Subject is the observable, and the observer is the observer.
8. The add method is to add new observers, the remove method is to remove observers, and the notify method is to notify all the observers.
9. In the notify method, we iterate through the list of observers, and call the update method of each observer.
10. The update method of the observer is called by the notify method of the observable, and the update method of the observer is called with the data of the observable.
11. We have a set data and get data in observable, and the set data is called by the subject, and the get data is called by the observer.
12. We can have the object of observable in the observer, and the observer can call the get data method of the observable. 
13. We can call the notify method of the observable in the set data method of the observable when we call the set data method to update the data.