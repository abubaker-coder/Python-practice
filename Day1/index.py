class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def welcome(self):
        print("welcome", self.name)

    def get_marks(self):
        return self.marks
    
s1 = Student(str(input("enter name: ")), int(input("enter age: ")), int(input("enter marks: ")))

s1.welcome()
print("marks:", s1.get_marks())




class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg is", sum/len(self.marks))
             

s1 = Student("john", [80, 95, 67])
s1.get_avg()






class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("RS-", self.balance, "are deposit in your account")
        print("Total balance = ", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print("RS-", self.balance, "are withdraw in your account")
            print("Total Balance = ", amount)

    def get_balance(self):
        return self.balance
    
a1 = Account("john", 5000)
a1.deposit(2000)
a1.withdraw(1000)
