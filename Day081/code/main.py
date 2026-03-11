# Day 081: Object-Oriented Programming

class BankAccount:
    """Bank account class demonstrating OOP concepts"""
    
    # Class variable (shared by all instances)
    bank_name = "Python Bank"
    total_accounts = 0
    
    def __init__(self, owner, balance=0):
        """Initialize a new bank account"""
        self.owner = owner  # Instance variable
        self.balance = balance
        self.transactions = []
        BankAccount.total_accounts += 1
        print(f"✓ Account created for {owner}")
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"✓ Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("✗ Invalid deposit amount")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > self.balance:
            print("✗ Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"✓ Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("✗ Invalid withdrawal amount")
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def get_transaction_history(self):
        """Get transaction history"""
        return self.transactions
    
    def __str__(self):
        """String representation of account"""
        return f"Account({self.owner}, Balance: ${self.balance})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"
    
    @classmethod
    def get_total_accounts(cls):
        """Class method to get total accounts"""
        return cls.total_accounts
    
    @staticmethod
    def calculate_interest(principal, rate, time):
        """Static method for interest calculation"""
        return principal * (1 + rate) ** time

class SavingsAccount(BankAccount):
    """Savings account with interest"""
    
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        """Apply interest to balance"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest: +${interest:.2f}")
        print(f"✓ Interest applied: ${interest:.2f}")

def main():
    """Demonstrate OOP concepts"""
    print("=" * 50)
    print("Day 081: Object-Oriented Programming")
    print("=" * 50)
    
    # Creating objects
    print("\n=== Creating Objects ===")
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    
    # Instance methods
    print("\n=== Instance Methods ===")
    account1.deposit(500)
    account1.withdraw(200)
    print(f"Alice's balance: ${account1.get_balance()}")
    
    # String representation
    print("\n=== String Representation ===")
    print(str(account1))
    print(repr(account2))
    
    # Class method
    print("\n=== Class Method ===")
    print(f"Total accounts: {BankAccount.get_total_accounts()}")
    
    # Static method
    print("\n=== Static Method ===")
    future_value = BankAccount.calculate_interest(1000, 0.05, 5)
    print(f"Future value: ${future_value:.2f}")
    
    # Inheritance
    print("\n=== Inheritance ===")
    savings = SavingsAccount("Charlie", 2000, 0.03)
    savings.deposit(500)
    savings.apply_interest()
    print(f"Charlie's balance: ${savings.get_balance():.2f}")
    
    # Transaction history
    print("\n=== Transaction History ===")
    for transaction in savings.get_transaction_history():
        print(f"  - {transaction}")

if __name__ == "__main__":
    main()
