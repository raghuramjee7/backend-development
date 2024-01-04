# Vending Machine

1. We use the State design pattern for this.
2. We create the flow of the system, and each step in the flow can be considered as a state.
3. We can move from one state to another state, we will drw this flow as well.
4. We will create a State interface, and each state will implement this interface.
5. We will then implement this state interface into different classes, each state is implemented by one class, in this class, we will implement the logic of that state from the total states, the rest states will give error or default value.
6. We will create a VendingMachine class, which will have a state variable, and we will create a constructor which will take the initial state, and set it to the state variable.
7. We will create a method, which will take the input, and based on the input, it will change the state of the vending machine.
9. We have methods to get which state the machine is in, and update its state from one to another.