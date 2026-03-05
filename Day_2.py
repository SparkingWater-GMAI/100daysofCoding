#print("Welcome to the tip calculator!")
#bill = float(input("What was the total bill? $"))
#tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#people = int(input("How many people to split the bill? "))

print("welcome to tip cal")
bill = float(input("enter bill: "))
tip = float(input("enter tip: "))
number_People = int(input("enter number of people: "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / number_People
final_amount = round(bill_per_person, 2)
print(f"Cost Per a Person = {final_amount}")
