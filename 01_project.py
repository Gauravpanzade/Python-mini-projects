#  Rent calculator



rent = int(input("Enter your hostel rent = "))
food = int(input("ENter aount of food order = "))
electricity_spend = int(input("electricity charges = "))
charge_per_unit = int(input("charge per unit = "))
person = int(input("number of member of room = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // person
print("Each person will pay = ", output )
 