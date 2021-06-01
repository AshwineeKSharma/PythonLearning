#----------------------------Property Decorator-------------------------------------------------------



class Employee:
    company="Microsoft"
    subunit="Office365"
    salary=60000
    bonussalary=7000
    # totalsalary=67000
    # totalsalary= salary+bonussalary

    @property                # Also a getter Property used to get(return) data. syntax: @property
    def totalsalary(self):
        return self.salary+self.bonussalary


    @totalsalary.setter             # Setter property is used to set data. syntax: @name.setter
    def totalsalary(self,val):
        self.bonussalary=val-self.salary

e=Employee()
print(e.totalsalary)
e.totalsalary=68000
print(e.salary)
print(e.bonussalary)


