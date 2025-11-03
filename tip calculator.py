print("welcome to the tip calculator!")
bill=float(input("what was the total bill ? $"))
tip=int(input("how much tip woud you like to give ? 5 10 15 ?"))
people =int(input("how many people to split the bill ?"))
bill_with_tip=tip/100*bill+bill
print("total bill to be paid:",bill_with_tip)
bill_per_person=bill_with_tip/people
final_amount=round(bill_per_person,2)
print(f"each person shoud pay {final_amount}$")          
    
