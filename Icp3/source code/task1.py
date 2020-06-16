"class createtion"
class Employee:
    count_employees = 0
    "created an empty list"
    salary_total = []
    "defined the init methode and passed the argruments"
    def __init__(self, n, f, s, d):
        self.name = n
        self.family =f
        self.salary = s
        self.salary_total.append(s)
        self.department =d
        Employee.count_employees = Employee.count_employees+1
        "method to calculates the avg salary of employess"
    def avg_sum(self):
        sum =0
        for i in self.salary_total:
            sum = sum +i
        avg = sum/len(self.salary_total)
        return avg
    "created the child class and inherted the base class employee"
class Fulltime_employee(Employee):
        pass
        "created the instances of the class "

p1 = Fulltime_employee("sai","patchala",50," database")
p2 = Employee("chand","patchala",70,"data base")
Fulltime_employee("raj","patchala",72,"data base")
"print the data attribute"
print(p1.avg_sum())
" print the class attribute"
print(p2.name)
print(p2.salary_total)
print(p1.count_employees)
