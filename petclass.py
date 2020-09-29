

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

    