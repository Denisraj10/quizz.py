print("Welcome to Mark Antony computer quiz Game Maamee!!")

playing=input("Do you want to play?")

if playing.lower() !="yes":
    quit()
    
print("Ok!! Let's Start play :)")

score=0

answer=input("What does CPU stand for ")
if answer.lower()=="central processing unit":
     print('Correct$$')
     
     score=score+1
else:
    print("Incorrect :(")     
   
        
answer=input("What does GPU stand for ")
if answer.lower()=="graphics processing unit":
     print('Correct$$')
     
     
     score=score+1
else:
    print("Incorrect :(")  
   
    
answer=input("What does RAM stand for ")
if answer.lower()=="random access memory":
     print('Correct$$')
     
     score=score+1
else:
    print("Incorrect :(")  
    
    
    
answer=input("What does ROM stand for ")
if answer.lower()=="read only memory":
     print('Correct$$')
     
     score=score+1
else:
    print("Incorrect :(")  
    
    
 
print("Your score is:",score,"/4")    
  

print("You Got:",(score/4)*100," % correct")     
    
            