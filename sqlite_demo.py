import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')
c =  conn.cursor()

def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emp_by_name(lastname):
	with conn:
		c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
		return c.fetchall()

def update_pay(emp, pay):
	with conn:
		c.execute("UPDATE employees SET pay=:pay WHERE first = :first AND last = :last",
			{'first': emp.first, 'last': emp.last, 'pay': pay})

def delete_emp(emp):
	with conn:
		c.execute("DELETE from employees WHERE first = :first AND last = :last", 
			{'first': emp.first, 'last': emp.last})



emp_1 = Employee('Bill', 'Gates', 80000)
emp_2 = Employee('Steve', 'Jobs', 83000)

insert_emp(emp_1)
insert_emp(emp_2)

gates = get_emp_by_name('Gates')
jobs = get_emp_by_name('Jobs')

update_pay(emp_1, 80000)
update_pay(emp_2, 90000)

emp_3 = Employee('Prince', 'Rios', 100000)

prince = get_emp_by_name('Rios')

print(prince)
print(gates)
print(jobs)


conn.commit()
