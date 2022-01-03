class Employee():
    '''ερφαζωμενη μιας  εταιριας'''
    theEmployees = []
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.theEmployees.append(self)

# main programm
the_employeees = []
while True:
    name = input("ονομα:")
    if not name: break
    salary = input("Μισθός:")
    Employee(name,salary)

#print employee
for employee in sorted(Employee.theEmployees, key=lambda x: x.name):
    print(employee.name,employee.salary ,sep='\t')
