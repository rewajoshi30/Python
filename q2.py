class Customer:
    name = ""
    credit = 0
    orders = {}


   customer_1 = Customer()
   customer_1.name = "Bill"
   customer_1.credit = 10
   customer_1.orders={ 'banana':30, 'apple' : 20}
   
   
   customer_2= Customer()
   customer_2.name = "Mary"
   customer_2.credit = 20
   customer_2.orders = {'apple': 20 , 'pear': 15}

   customer_3 = Customer()
   customer_3.name= "Tom"
   customer_3.credit = 15
   customer_3.orders= {'orange' : 10, 'banana' : 20 }

   print('{<7}credit:{:>3}\norders:{:10}

