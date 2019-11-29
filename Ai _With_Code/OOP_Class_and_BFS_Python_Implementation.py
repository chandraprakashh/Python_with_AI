"""
OOP-Class-and-BFS Python Implementation
#self represents the instance of the class. 

#By using the “self” keyword we can access the attributes and methods of the class in python.

#It binds the attributes with the given arguments.

"""

"""
The sole purpose of __init__ is to initialize the values of instance members for the new object.

In the init method, self refers to the newly created object; 

in other class methods, it refers to the instance whose method was called. 

Python doesn't force you on using "self".You can give it any name you want.

But remember the first argument in a method definition is a reference to the object.

"""

###################################################################

#Example of a class

#Class Ex-1

class demo(object):

    def __init__(self, a):

        self.a = a



    def change_a(self, new_a):

        self.a = new_a



obj1 = demo(10)      # will call the init fn of class and create a class level variable a = 10

print(obj1.a)         # will print 10 which is stored in class level variable for obj1



obj1.change_a(20)    # will call the fn and change the class level variable a = 20

print(obj1.a)        # will print 20 becuase class level variable a was changed

###################################################################

#Class Ex-2

class car(): 



    # init method or constructor 

    def __init__(self, model, color): 

        self.model = model 

        self.color = color 

    def show(self): 

        print("Model is", self.model ) 

        print("color is", self.color ) 



# both objects have different self which # contain their attributes 



tata = car("TATA Safari Storme", "White") 

fortuner = car("Fortuner MT 2694 ", "RED") 



tata.show()	 # same output as car.show(tata) 

fortuner.show() # same output as car.show(fortuner) 

###################################################################

#BFS implementation on Tree in Python

"""

        1

        /  \

       2    3

      / \     / \

     4   5  6  7

    """

class TNode:

  def __init__(self, data, left=None, right=None):

    self.data = data

    self.left = left

    self.right = right



class BST:

  def __init__(self, root):

    self._root = root



  def bfs(self):

    list = [self._root]

    while len(list) > 0:

        print([e.data for e in list])

        list = [e.left for e in list if e.left] + [e.right for e in list if e.right]

        

bst = BST(TNode(1, TNode(2, TNode(4), TNode(5)), TNode(3, TNode(6), TNode(7))))

bst.bfs()