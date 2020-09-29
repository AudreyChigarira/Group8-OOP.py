
from datetime import datetime

# class variable within customer class
company_name = "Critter Watch"

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
address1 = input("What is your primary address? ")
address2 = input("What is your secondary address? ")
city = input("What city do you live in? ")
state = input("What state do you live in? ")
zip_code = input("What is your zip code? ")

customer = Customer(first_name, last_name, address1, address2, city, state, zip_code)

pet_name = input("What is your pet's name? ")
pet_breed = input("What is your pet's breed? ")
pet_age = int(input("What is your pet's age? "))

pet = Pet(pet_name, pet_breed, pet_age, customer)

customer.cust_pet = pet

begin_date = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y")
end_date = datetime.strptime(input("Enter End date in the format m/d/y: "), "%m/%d/%Y")
day_rate = float(input("Enter the day rate: "))

appointment = Appointment(customer)
appointment.set_appointment(begin_date, end_date, day_rate)

customer.cust_pet.appointment = appointment

customer.return_bill()

customer.make_payment()

customer.return_bill()

class customer():
    company_name = 'Critter Watch'

    def __init__ (self,first_name, last_name, address1, address2, city, state, sZip):
        self.cust_id = self.gen_id()
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.sZip = sZip
        self.balance = 0.0
        self.cust_pet = None

    def gen_id(self,first_name,last_name,address1):
        cust_id = (self.first_name[0 : 3] + self.last_name[0 : 3] + self.address1[0 : 5])
        return(cust_id)

    def return_bill(self, cust_id, first_name, last_name, balance, cust_pet, Appointment.begin_date, Appointment.end_date):
        return('Customer ' + cust_id + 'with name ' + first_name + ' ' + last_name + ' owes $' + balance + ' for ' + cust_pet.pet_name + "'s stay from " + Appointment.begin_date + " to " + Appointment.end_date )

    def make_payment(self, fPayment):
        balance = balance - fPayment
        return(balance)

