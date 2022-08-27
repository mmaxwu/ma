# AP Vocabulary Quiz | FRQ - MC

def q_and_a(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg
    
questions = 3
correct = 0

print("Hello, you will be taking the vocabulary test.")
print("Do you wish to proceed?(y/n)")

msg = input()

while (msg!="y") :  
    print("ERROR, YOU HAVE TO SAY YES, DON'T HAVE A CHOICE")
    msg = input()
  
print("You may now proceed")
      
rsp = q_and_a("Does static text change? (yes/no)")
if rsp == "no":
    print(rsp +" is correct")
    correct += 1
else:
    print(rsp +" is wrong :(")
    
rsp = q_and_a("At least how many lines are required to form a sequence of code?(1-4)")
if rsp == "2":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = q_and_a("Is Input and Output in jupyter notebooks in line with Output?(yes/no)")
if rsp == "no":
    print(rsp + " is correct!!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(" you scored " + str(correct) +"/" + str(questions))


   



