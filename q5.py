import datetime

class Car:
    id = ""
    engine = "4-cylinder"
    mileage = 0
    year = datetime.datetime.today().year

    def upgrade_engine(self, new_engine):
        self.engine = new_engine

    def display_info(self):
        print("id: {}, engine: {}, mileage: {}, year: {}".format(self.id, self.engine, self.mileage, self.year))
    
    def drive(self, mileage):
        self.mileage += mileage 


##############################################################
# Task 1: define two car objects (car_1 and car_2), assign them
# with ids 1 and 2 (for car_1 and car_2 respectively), and then
# display the info of the two objects via the method display_info
##############################################################
car_1 = Car()
car_2 = Car()

car_1.id = 1 
car_2.id = 2

car_1.display_info()
car_2.display_info()



##############################################################
# Task 2: upgrade the engine of car_2 to be "8-cylinder", then
# display the info of the two objects via the method display_info
##############################################################

car_2.upgrade_engine("8-cylinder")
car_1.display_info()
car_2.display_info()




##############################################################
# Task 3: define a method drive(self, distance) in the class Car
# that will increase the mileague by distance 
##############################################################




### Testing - uncomment these statements after finishing Task 3
car_3 = Car()
car_3.id = "3"
car_3.display_info()   # should display "id: 3, engine: 4-cylinder, mileage: 0, year: 2024"
print("-"*50)

car_3.drive(100)
car_3.display_info()   # should display "id: 3, engine: 4-cylinder, mileage: 100, year: 2024"

car_3.upgrade_engine("8-cylinder")
car_3.display_info()   # should display "id: 3, engine: 8-cylinder, mileage: 100, year: 2024"
