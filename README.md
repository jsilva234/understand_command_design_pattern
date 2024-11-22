The Command Design Pattern is a behavioral design pattern that encapsulates a request as an object, 
allowing you to parameterize clients with queues, requests, or operations. It decouples the sender 
(who initiates the request) from the receiver (who processes it). 
The core idea is to use command objects to encapsulate all details of a request: 
the method call, the method arguments, and the receiving object.

## Key Components:
**Command:** An interface or abstract class defining the execution method (execute()).  
**ConcreteCommand:** Implements the Command interface and defines the binding between a receiver and an action.  
**Receiver:** The object that knows how to perform the action.  
**Invoker:** Asks the command to carry out the request.  
**Client:** Creates and configures the command objects.  
 
## Main Advantages:
**Decoupling:**   
Separates the object that invokes the operation from the one that knows how to perform it.  
**Undo/Redo Operations:**  
Commands can be stored and executed later, making it easy to implement features like undo/redo.    
**Easier Extension:**  
New commands can be added without modifying existing code.  
**Macro Commands:**  
Supports assembling a set of commands to execute in sequence (like macros).
**Logging and Queuing:**  
Requests can be logged or queued for delayed execution or recovery.    