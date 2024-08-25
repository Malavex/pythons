import csv

#main function
#getting cx order 
Pep = 10.99
cheese = 5.99
sas =11.99  

def get_pizza():
    while True:
        pizza = input("hello what pizza would you like options are 1-3 (1 = pep, 2 = cheese, 3 = sasuage)")
        if pizza.isdigit():
            pizza= int(pizza)
            if pizza == 1:
                pizza= Pep
               
                break 
            elif pizza == 2:
                 pizza = cheese
                
                 break
            elif pizza == 3:
                 pizza= sas
               
                 break
            else:
                    print("enter a number 1-3 ")
        else:
            print("please enter a number 1 - 3")
    return pizza
    

def get_quantity():
    while True:
        quant= input("How many would you like? ")
        if quant.isdigit():
            quant= int(quant)
            break
        else:
              print("please enter a number")
    return quant 



def get_order():

 pizzas= get_pizza()
 category= pizzas
 if category== Pep:
     category="Pepperoni"
 if category == sas:
     category = "sasuage"
 if category==cheese:
     category="cheese"
 quantity= get_quantity()
 subtotal = pizzas * quantity 
 tax_total=format(subtotal*1.07,".2f")
 print(f"you want {quantity} {category} subtotal: {subtotal},total: {tax_total}")
 

def main():
    start= True
    while start== True:
     menu=input("Do you wish to place an order? (type Y or N)")
     menu= menu.lower()
     if menu =='y':
         get_order()
     elif menu=='n':
         print("exiting program..")
         start= False

main()

         

