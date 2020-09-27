class Appointment():

    def __init__(self, owner):
        #I'm not sure if there's something special you need to do when declaring a date variable
        self.dBegin_date = None
        self.dEnd_date = None
        self.fDay_rate = 0.0
        self.iTotal_days = 0
        self.iTotal_cost = 0.0
        self.oOwner = owner

    def set_appointment(begin_date, end_date, day_rate):
        self.dBegin_date = begin_date
        self.dEnd_date = end_date
        self.fDay_rate = day_rate

        calc_days()                                                 # calls calc_days() function

        #why are we assigning values to iTotal_cost here AND down in calc_days()?
        self.iTotal_cost = self.owner.balance                       # updates the balance

    def calc_days():
        self.iTotal_days = (self.dEnd_date - self.dBegin_date).days # calculates total_days (subtracting end_date from begin_date)
           
        if self.iTotal_days <= 0 :                                  # checks if total_days is less than or equal to 0
            self.iTotal_days = 1                                    # if yes, assigns a 1 to the total_days

        self.iTotal_cost = self.iTotal_days * self.fDay_rate        # calculates the total_cost (multiplying total_days by day_rate)

        return self.iTotal_days                                     # returns the days value