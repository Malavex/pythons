#making calculator
#setting up   user inputs
def get_operation():
   while True:
        op=input("please enter what you would like to do * for multiple / for divide, - for subtraction, + for addition ")
        if op=='+':
            break
        if op== '-':
         break
        if op=='*':
          break
        if op=='/':
         break
        else:
         print("please use  *,/, +, -  ")
   return op


def get_values():
    while True:
        n1 = input('please enter a number ')
        if n1.isdigit():
           n1=int(n1)
           break 
    return n1

def get_continue():
 while True:
  contin = input("Do you wish to continue type y or no ")
  contin= contin.lower()
  if contin == "n":
     break
  if contin == "y":
     break
  else: 
     print("please enter y for yes and n for no ")
 return contin
     
   

def main():
   cont= False
   while cont == False: 
      value1 = get_values()
      op = get_operation()
      value2 = get_values()
      if op =='*':
         results= value1 * value2    
      elif op == '/':
         results = value1/value2
      elif op == "-":
         results= value1 -value2
      else:
         results= value1 + value2
      print (f"your result is {results} ")
      yes=get_continue()
      if yes =="n":
         cont=True
      else:
         continue

         

main()

   
     
 
    
   
   
   
    
