rent = int(input('Enter your flat rent= '))
food = int(input('Enter the amount of food ordered= '))
electricity_spend = int(input('Enter the total electricity amount spend= '))
charge_per_unit = int(input('Enter the charge per unit of electricity= '))
persons = int(input('Enter the number of persons living in flat= '))

total_electcity_bill = electricity_spend * charge_per_unit

per_person_expense = (rent + food + total_electcity_bill) // persons

print('Each person will pay = ', per_person_expense)