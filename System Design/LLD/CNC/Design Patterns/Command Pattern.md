# Command Pattern

1. It is a behavioral pattern.
2. This is used in situations where there is lack of abstraction, there is no option to undo/redo, there is a need to support callbacks, and there is a need to support transactions.
3. Command pattern divides the application into three parts: the invoker, the receiver, and the command.
4. The invoker is the one that invokes the command.
5. The receiver is the one that receives the command.
6. The command is the one that encapsulates the action.
7. Each of these will be a different interface.
8. The command interface will have an execute method.
9. In the concrete class that implements the command interface, we will have a reference to the receiver.
10. The receiver will have the actual implementation of the action.
11. The invoker will have a reference to the command interface, and it will call the execute method on the command interface.
12. The command interface has an option to undo the action, which undoes the action that was done by the execute method.
13. We can have a command history, which will have a list of commands that were executed. This can be a stack or a DLL.
14. 