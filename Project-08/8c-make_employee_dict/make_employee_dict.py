# Author: Timur Guner
# Date: 2021-02-24
# Description: Project 8c creates a class Employee that has private data members _name, _ID_number, _salary, and
#              _email_address. It has for get methods for name, id, salary, and email. The other part of the code is a
#              make_employee_dic function that creates an employee object from a list of names, ids, salaries, and
#              emails. Through each iteration of creating a new employee object from elements of the list, that employee
#              object is added to an employee dictionary with the employee id as the key

class Employee:
    """class Employee that has private data members _name, _ID_number, _salary, and
        _email_address. It has for get methods for name, id, salary, and email."""

    def __init__(self, name, ID_number, salary, email_address):
        self._name = str(name)
        self._ID_number = str(ID_number)
        self._salary = int(salary)
        self._email_address = str(email_address)

    def get_name(self):
        """The get_name method returns the employee's name"""

        return self._name

    def get_ID_number(self):
        """The get_ID method returns the employee's id"""
        return self._ID_number

    def get_salary(self):
        """The get_salary method returns the employee's salary"""
        return self._salary

    def get_email_address(self):
        """The get_emial method returns the employee's email address"""
        return self._email_address


def make_employee_dict(names, id_numbers, salaries, emails):
    """make_employee_dic function creates an employee object from a list of names, ids, salaries, and
       mails. Through each iteration of creating a new employee object from elements of the lists, that employee
       object is added to an employee dictionary with the employee id as the key"""

    # create a blank dictionary and get the length of names list, which both are used for iteration in the for loop
    iterate = int(len(names))
    employee_dict = {}

    # For loop creates an Employee per each line of elements for the list and creates a new element in the list with
    # the key as the employee id and the Employee object assigned to it.
    for x in range(0, iterate):
        employee = Employee(names[x], id_numbers[x], salaries[x], emails[x])
        employee_dict[employee.get_ID_number()] = employee

    # return the employee dictionary
    return employee_dict

emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = [100, 101, 102]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result["100"].get_ID_number(), result["100"].get_name())