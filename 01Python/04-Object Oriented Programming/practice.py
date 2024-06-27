class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()


#_______________________________________________________________________________________________________________#


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)
    
c = Cylinder(2,3)


#_______________________________________________________________________________________________________________#


class Account:
     
     def __init__(self,owner ,balance):
             self.owner=owner
             self.balance=balance
     def deposist(self,dpamount):
          self.balance += dpamount
          return "balance after deposit is : "+str(self.balance)
         
     def withdraw(self,withAmt):
         if(self.balance<withAmt):
             return "Low balance"
         else:
             self.balance -= withAmt
             return "current balance is " + str(self.balance)     
                 
acc =  Account("tej",4000)
print(acc.deposist(300))
print(acc.withdraw(300))