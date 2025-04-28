class Customer:
    name = ""
    credit = 0
    orders = {}

# data of the three customers are stored in multiple lists
name_list = ["Bill", "Mary", "Tom"]
credit_list = [10, 20, 15]
orders_list = [{"banana": 30, "apple": 20}, {"apple": 20, "pear": 15}, {"orange": 10, "banana": 20}]

# create a list of three customer objects
customer = []
for i in range(len(name_list)):
    customer.append(Customer())

for i in range(len(customer)):
    customer[i].name   = name_list[i]
    customer[i].credit = credit_list[i]
    customer[i].orders = orders_list[i]

# display the data of the three customer objects
for i in range(len(customer)):
    print("{:<5}\tcredit:{:>3}\n\torders: {}\n".format(customer[i].name,customer[i].credit,customer[i].orders))

customer_4 = Customer()
customer_4.name = "Alex"
customer_4.credit = 5
customer_4.orders = {'milk': 2, 'honey' : 3}
customer.append(customer_4)

for i in range(len(customer)):
    print("{:<5}\tcredit:{:>3}\n\torders: {}\n".format(customer[i].name,customer[i].credit,customer[i].orders))