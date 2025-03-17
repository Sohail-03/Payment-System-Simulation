from database.db_operations import add_user, get_user_balance, update_user_balance, record_transaction

def create_account(name, balance):
    add_user(name, balance)
    print(f"Account for {name} created successfully with a balance of {balance}.")

def check_balance(user_id):
    balance = get_user_balance(user_id)
    if balance is not None:
        print(f"User {user_id} has a balance of ${balance:.2f}")
    else:
        print(f"User {user_id} not found.")

def transfer_funds(from_user, to_user, amount):
    from_balance = get_user_balance(from_user)
    to_balance = get_user_balance(to_user)
    
    if from_balance is None or to_balance is None:
        print("One or both users not found.")
        return

    if from_balance < amount:
        print("Insufficient balance.")
        return

    new_from_balance = from_balance - amount
    new_to_balance = to_balance + amount
    
    # Update balances
    update_user_balance(from_user, new_from_balance)
    update_user_balance(to_user, new_to_balance)
    
    # Record the transaction
    record_transaction(from_user, to_user, amount)
    
    print(f"Transfer of ${amount} from User {from_user} to User {to_user} successful.")

def view_transaction_history():
    conn = sqlite3.connect('payment_system_simulation.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM transactions
    ORDER BY timestamp DESC
    ''')
    transactions = cursor.fetchall()
    conn.close()

    for transaction in transactions:
        print(f"Transaction ID: {transaction[0]}, From User: {transaction[1]}, To User: {transaction[2]}, Amount: ${transaction[3]:.2f}, Date: {transaction[4]}")
