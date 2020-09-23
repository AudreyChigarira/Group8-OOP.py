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