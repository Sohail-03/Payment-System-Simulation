import unittest
from src.payment_system import create_account, check_balance, transfer_funds

class TestPaymentSystem(unittest.TestCase):

    def setUp(self):
        # Initialize the database (create tables)
        from database.db_operations import create_tables
        create_tables()

    def test_create_account(self):
        create_account("John Doe", 1000.0)
        check_balance(1)  # Check if account balance is correctly set

    def test_transfer_funds(self):
        create_account("Alice", 500.0)
        create_account("Bob", 300.0)
        transfer_funds(1, 2, 100.0)  # Transfer from Alice to Bob
        check_balance(1)  # Check Alice's new balance
        check_balance(2)  # Check Bob's new balance

    def test_insufficient_funds(self):
        create_account("Charlie", 50.0)
        create_account("Dave", 200.0)
        transfer_funds(1, 2, 100.0)  # Insufficient balance for the transfer

if __name__ == '__main__':
    unittest.main()
