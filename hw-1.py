class node:
        x=[]
        y=[]
        parent_cost=[]
        index=[]
        def __init__(self,x,y,parent_cost,index):
             self.x = x
             self.y = y
             self.parent_cost=parent_cost
             self.index=index

gan=node(1,2,3,4)
print(gan.x)