# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:04:09 2024

@author: Madhumitha
"""

#importing
from queue import Queue

#initializing
q=Queue()

# put - function for enqueue operation (inserting),inserts 1st queue element 
q.put("hi")     
q.put(2)
print("inserting element to queue:",q)

#get - function for dequeue operation (deleting), removes 1st queue element
print("queue after deletion:",q.get())

#accesing
print("displaying 1st queue element:",q.queue[0])

#is empty
q.get()
print("checking whether the queue is empty:",q.empty())

#is full
q=Queue(maxsize=3)
q.put("hi")
q.put(2)
print("checking whether the queue is full:",q.full())

print("------------------------------------------------------------")
#-----------------------------------------------------------------

#initialization
queue=[]
print("queue with no elements:",queue)

#enqueue/inserting
queue.append(5)
queue.append(-1)
queue.append("name")
queue.append('a')
print("queue after insertion:",queue)

#dequeue/deleting
queue.pop(0)
print("queue after deletion:",queue)


#searching
print("checking whether the particular element exists or not:")
x=4
if(queue[-1]==x):
    print("True")
else:
    print("False")