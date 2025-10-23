initial_balance = float(input("Enter initial balance (₹): "))
deposit = float(input("Enter deposit amount (₹): "))
new_balance = initial_balance + deposit
withdraw = float(input("enter withdrawal amount:"))
final_balance = new_balance - withdraw
print("\nInitial Balance: ₹", initial_balance)
print("Deposit: ₹", deposit)
print("New Balance after deposit: ₹", new_balance)
print("withdraw:",withdraw)
print("final balance :",final_balance)