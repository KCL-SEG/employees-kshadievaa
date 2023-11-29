"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.monthly_salary = 0
        self.hourly_wage = 0
        self.hours_worked = 0 
        self.fixed_bonus = 0
        self.contracts_landed = 0
        self.commission = 0
        self.pay = 0
    

    def get_pay(self):
        if self.monthly_salary > 0:
            if self.fixed_bonus:
                self.pay = self.monthly_salary + self.fixed_bonus
            elif self.contracts_landed and self.commission:
                self.pay = self.monthly_salary + self.contracts_landed * self.commission
            else:
                self.pay = self.monthly_salary 
        elif self.hourly_wage > 0 and self.hours_worked > 0:
            if self.fixed_bonus:
                self.pay = self.hourly_wage * self.hours_worked + self.fixed_bonus
            elif self.contracts_landed and self.commission:
                self.pay = self.hourly_wage * self.hours_worked + self.contracts_landed * self.commission
            else:
                self.pay = self.hourly_wage * self.hours_worked
        return self.pay

    def __str__(self):
        string = f"{self.name}"
        if self.monthly_salary > 0:
            string = string + f" works on a monthly salary of {self.monthly_salary}"
            if self.fixed_bonus:
                string = string + f" and receives a bonus commission of {self.fixed_bonus}."
            elif self.contracts_landed and self.commission:
                string = string + f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission}/contract."
            else:
                string = string + f"."
        else:
            string = string + f" works on a contract of {self.hourly_wage} hours at {self.hours_worked}/hour"
            if self.fixed_bonus:
                string = string + f" and receives a bonus commission of {self.fixed_bonus}."
            elif self.contracts_landed and self.commission:
                string = string + f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission}/contract."
            else:
                string = string+ f"."
        string = string + f" Their total pay is {self.pay}."
        return string

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.monthly_salary = 4000
print(billie.get_pay())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.hourly_wage = 100
charlie.hours_worked = 25 
print(charlie.get_pay())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.monthly_salary = 3000
renee.commission = 200
renee.contracts_landed = 4
print(renee.get_pay())
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.hourly_wage = 150
jan.hours_worked = 25 
jan.commission = 220
jan.contracts_landed = 3
print(jan.get_pay())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.monthly_salary = 2000
robbie.fixed_bonus = 1500
print(robbie.get_pay())

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.fixed_bonus = 600
ariel.hourly_wage = 120
ariel.hours_worked = 30 
print(ariel.get_pay())