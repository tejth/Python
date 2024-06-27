try:
    for i in ['a','b','c']:
     print(i**2)
except:
    print("Error")
    
#_________________________________________________________________________________________________________#    

x = 5
y = 0
try: 
 z = x/y
except:
    print("Error")
finally:
    print("All done") 
    
#________________________________________________________________________________________________________________#

def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)
    

#________________________________________________________________________________________________________________#


   
