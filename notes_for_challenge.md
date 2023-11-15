
Describe the problem

As a user:
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

Design Function signature
```python
create a function that track my tasks 

def track_my_tasks ():
#Parameters:
# a string or text that have the #TODO 
#return 
# is the #todo present in the task or not 
pass


Create examples 
given a task that has not been done 
it returns the string with the #todo 

track_my_tasks("take the trash out") =>  #TODO

given a task that has been done
it return a message saying its been done

track_my_tasks("shopping grocerys) => "done"

given two tasks one being done and the other one pending 
it return the #todo in the one pending 

track_my_tasks ("take the trahs out: Done, shopping grocerys: #TODO)
 => ("shopping grocerys: #TODO)

Implement behaviour 
