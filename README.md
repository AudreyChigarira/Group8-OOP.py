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
