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
        return(cust_id)

    def return_bill(self, cust_id, first_name, last_name, balance, cust_pet, Appointment.begin_date, Appointment.end_date):
        return('Customer ' + cust_id + 'with name ' + first_name + ' ' + last_name + ' owes $' + balance + ' for ' + cust_pet.pet_name + "'s stay from " + Appointment.begin_date + " to " + Appointment.end_date )

    def make_payment(self, fPayment):
        balance = balance - fPayment
        return(balance)