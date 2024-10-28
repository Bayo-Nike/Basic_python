# =========== Creating a list============================
fruits = ["apple", "banana", "cherry",123]

# Accessing elements
print (fruits[0])
print (fruits[-4])

 # Adding elements
fruits.append("orange") 

fruits.insert(1, "kiwi") # Inserts "kiwi" at index 1

 # Removing elements
fruits.remove("banana") # Removes "banana"

    
 

# Accessing elements
print (fruits)
print (fruits[1:3])
    

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Initializing a list of transactions
transactions = [100,50, 200,-20, 30] # positive for deposits, negative for withdrawals
 # Adding a new transaction
transactions.append(10)
 # Removing a transaction (first instance of50)
transactions.remove(50)
 # Accessing transactions 

print("Last transaction:", transactions) # 100, 200,-20, 30,10


# -----==============Tuples =================Immutable==========
customer_info = ("Bayisa", 123456, "Savings")
# Accessing data
name = customer_info[0]
account_no = customer_info[1]
account_type = customer_info[2]
print(f"Customer Name: {name}")
print(f"Customer Acct: {account_no}")
print(f"Account Type: {account_type}")


# ========================Dictionary ================
customer_balances = {
123456: 1500.0, # account number: balance
789012: 300.0,
345678: 0.0
}
# Accessing balance
account_number = 123456
print("Balance:", customer_balances.get(account_number,"Account not found"))
# Updating balance after a deposit
customer_balances[123456] += 500.0 # adds $500 to the balance
print("Updated Balance:", customer_balances[123456])
print("is Avail:", customer_balances.get("rtrt","Not Available"))

# ================Set of unique transaction types==============
transaction_types = {"deposit", "withdrawal", "transfer"}
# Adding a new type
transaction_types.add("loan payment")
# Checking for a transaction type
print("Has 'deposit' been made?", "deposit" in transaction_types)
# Union with another set (additional types)
all_types = transaction_types - {"fee", "interest"}
print("All transaction types:", all_types)

list_transaction_types = ["A2A", "A2B", "A2C","A2A"]
set_transaction_types=set(list_transaction_types)
print("Avoid Dup transaction types:", set_transaction_types)
