# OOP.py
#2-8 Lilia Brown, Audrey Chigarira, Brandon Gill, Peter Gardiner

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
#create Class o Instance Variables:  pet_name is of type string,  breed is of type string,  age is of type int,  appointment of type Appointment
class pet():

    def __init__ (self, pet_name, breed, iAge, owner): #def __init__ (self, pet_name, breed, iAge, appointment?):
        self.pet_name = pet_name
        self.breed = breed
        self.age = iAge
        #self.appointment = appointment(owner) #When calling the Appointment constructor you will want to pass the owner

   #  pet constructor  
    def pet (self, pet_name, breed, age, owner):
        self.appointment = appointment(owner) #When calling the Appointment constructor you will want to pass the owner

    #pet method    
        oCustomer.cust_pet = Pet(self.pet_name, self.breed, self.iAge, self.oCustomer)
        return(oCustomer.cust_pet)

    
