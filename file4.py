class Company:
    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_departments(self):
        self.departments['IT'] = []
        self.departments['Administration'] = []
        self.departments['Service'] = []


class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def add_employee(self, department):
        comp.departments[department].append((self.name, self.lastname))


comp = Company('Hoole')
comp.add_departments()
p = Employee('Hari', 'Zak')
p.add_employee('IT')
t= Employee('Kai', 'Rak')
t.add_employee('Administration')
n = Employee('Nik', 'Bob')
n.add_employee('Service')

print(comp.departments)