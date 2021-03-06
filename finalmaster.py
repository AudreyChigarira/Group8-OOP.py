#IS403 Section 2 Group 8 : Lilia Brown, Audrey Chigarira, Peter Gardiner, Brandon Gill
#Program Description:
# Using object-oriented programming to prompt users to enter their information then outputting results based on their information entered about themselves and their pet


    #customer class 

class customer():
    company_name = 'Critter Watch'

    def __init__ (self, first_name, last_name, address1, address2, city, state, sZip):
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.sZip = sZip
        self.balance = 0.0
        self.cust_id = self.gen_id(first_name, last_name, address1)
        self.cust_pet = []

    def gen_id(self,first_name,last_name,address1):
        cust_id = (self.first_name[0 : 3] + self.last_name[0 : 3] + self.address1[0 : 5])
        cust_id = cust_id.replace(' ', '')
        return(cust_id)

    def return_bill(self):
        return('Customer ' + self.cust_id + ' with name ' + self.first_name + ' ' + self.last_name + ' owes $' + str(self.balance) + ' for ' + self.cust_pet[0].pet_name + "'s stay from " + str(self.cust_pet[0].appointment[0].dBegin_date) + " to " + str(self.cust_pet[0].appointment[0].dEnd_date))

    def make_payment(self, fPayment):
        self.balance = self.balance - fPayment
        return(self.balance)
        
    #create Class o Instance Variables:  pet_name is of type string,  breed is of type string,  age is of type int,  appointment of type Appointment

class pet():

    def __init__ (self, pet_name, breed, iAge, owner): #def __init__ (self, pet_name, breed, iAge, appointment?):
        self.pet_name = pet_name
        self.breed = breed
        self.age = iAge
        self.appointment = []

    #appointment class
    
class Appointment():

    def __init__(self, owner):
        self.dBegin_date = None
        self.dEnd_date = None
        self.fDay_rate = 0.0
        self.iTotal_days = 0
        self.iTotal_cost = 0.0
        self.oOwner = owner

    def set_appointment(self, begin_date, end_date, day_rate):
        self.dBegin_date = begin_date
        self.dEnd_date = end_date
        self.fDay_rate = day_rate

        self.calc_days()                                                                   # calls calc_days() function

        self.oOwner.balance = self.iTotal_cost + self.oOwner.balance                       # updates the balance

    def calc_days(self):
        self.iTotal_days = (self.dEnd_date - self.dBegin_date).days                        # culates total_days (subtracting end_date from begin_date)
           
        if self.iTotal_days <= 0 :                                                         # checks if total_days is less than or equal to 0
            self.iTotal_days = 1                                                           # if yes, assigns a 1 to the total_days

        self.iTotal_cost = self.iTotal_days * self.fDay_rate                               # calculates the total_cost (multiplying total_days by day_rate)

        return self.iTotal_days                                                            # returns the days value

    #user prompts
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
address1 = input("What is your primary address? ")
address2 = input("What is your secondary address? ")
city = input("What city do you live in? ")
state = input("What state do you live in? ")
zip_code = input("What is your zip code? ")

oCustomer = customer(first_name, last_name, address1, address2, city, state, zip_code)

print(oCustomer.cust_id)

pet_name = input("What is your pet's name? ")
pet_breed = input("What is your pet's breed? ")
pet_age = int(input("What is your pet's age? "))

    #oCustomer.cust_pet = pet(pet_name, pet_breed, pet_age, oCustomer)
oCustomer.cust_pet.insert(0, pet(pet_name, pet_breed, pet_age, oCustomer))

from datetime import datetime

begin_date = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y")
end_date = datetime.strptime(input("Enter End date in the format m/d/y: "), "%m/%d/%Y")
day_rate = float(input("Enter the day rate: "))

    # Output
oCustomer.cust_pet[0].appointment.insert(0, Appointment(oCustomer))
oCustomer.cust_pet[0].appointment[0].set_appointment(begin_date, end_date, day_rate)
print(oCustomer.return_bill())
