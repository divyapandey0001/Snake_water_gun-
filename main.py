import random 
'''
1 for sanke 
-1 for water 
0 for gun
'''
Computer = random.choice([-1,0,1])
youstr = input("Enter your choice :")
youDict = {"s":1,"w": -1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you =youDict[youstr] 

print(f"you chose {reverseDict[you]}\nComputer chose{reverseDict[Computer]}")
if(Computer ==you ):
    print("its draw")

else:
     if(Computer ==-1 and you==1 ):
       print("you win")

     elif(Computer==-1 and you == 0):    
       print("you loss")
    
     elif(Computer== 1 and you == -1):
       print("you lose")

     elif(Computer==-1 and you==0) :    
       print("you win")   

     elif(Computer==0 and you ==1):    
      print("you loss") 

     elif(Computer==0 and you == 1):    
       print("you loss") 


     else:
        ("somthing went wrong")   

    