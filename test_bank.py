import pytest
from datetime import datetime
from bank_exercise import BankAccount

@pytest.fixture
def new_account():
    return BankAccount("Ahmed", 100)

@pytest.fixture
def new_correctly_account():
    return BankAccount("Mohammed")

@pytest.fixture
def success_deposit_amount():
    return BankAccount("Ahmed", 100)

@pytest.fixture
def negative_deposit_amount():
    return BankAccount("Jasim", 100)

@pytest.fixture
def success_withdraw_amount_more_than_balance():
    return BankAccount ("Bob", float(500))

@pytest.fixture
def withdraw_amount_negative():
    return BankAccount ("Bob", float(500))

@pytest.fixture
def setup_accounts():
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    return account1, account2



def testing_create_new_account(new_account):
    new_account.account_holder == "Ahmed"
    new_account.balance == 100
    assert new_account.account_holder == "Ahmed"

def testing_create_new_negative_account():
    with pytest.raises(ValueError, match= "Initial balance cannot be negative"):
        account1 = BankAccount("Khaled", -1000)
        

def testing_account_correctly_stored(new_correctly_account):
    assert new_correctly_account.account_holder == "Mohammed"

def testing_success_deposit_amount(success_deposit_amount):
    assert success_deposit_amount.deposit(100)

def testing_zero_deposit_amount():
        account= BankAccount("Ahmed", 1000)
        assert account.deposit(0)

def testing_negative_deposit_amount(negative_deposit_amount):
    with pytest.raises(ValueError, match= "Deposit amount must be positive"):
        negative_deposit_amount.deposit(-100)

def testing_success_withdraw():
        account = BankAccount("Ahmed", 1000)
        assert account.withdraw(50)

def testing_success_withdraw_more_than_balance(success_withdraw_amount_more_than_balance):
    with pytest.raises(ValueError, match= "Insufficient funds"):
        wd = success_withdraw_amount_more_than_balance.withdraw(550)
        success_withdraw_amount_more_than_balance < wd

def testing_success_withdraw_negative(withdraw_amount_negative):
    with pytest.raises(ValueError, match= "Withdrawal amount must be positive"):
        withdraw_amount_negative.withdraw(-550)

def testing_success_transfar():
    account1=BankAccount("Ahmed", 1000)
    account2=BankAccount("Omar", 500)
    account1.transfer(account2, 300)

def testing_transfar_more_than_balance():
    with pytest.raises(ValueError, match= "Insufficient funds"):
        account1=BankAccount("Ahmed", 1000)
        account2=BankAccount("Omar", 500)
        account1.transfer(account2, 3000)

def testing_transfar_non_BankAccount():
    with pytest.raises(TypeError, match= "Recipient must be a BankAccount instance"):
        account1=BankAccount("Ahmed", 1000)
        account2=""
        account1.transfer(account2, 30)        


def test_transactions_are_recorded_correctly(setup_accounts):
    account1, account2 = setup_accounts

    account1.deposit(500)

    txn1 = account1.get_transaction_history()[1]  

    assert txn1['type'] == "Deposit"
    assert txn1['amount'] == 500

def test_transaction_history_contains_correct_details(setup_accounts):
    account1, account2 = setup_accounts

    account1.deposit(500)
    account1.withdraw(200)

    txn = account1.get_transaction_history()[1]  

    assert txn['type'] == 'Deposit'
    assert txn['amount'] == 500
    assert txn['balance_after'] == 1500 
    assert isinstance(txn['timestamp'], datetime) 

def test_transaction_timestamps_are_present(setup_accounts):
    account1, account2 = setup_accounts

    account1.deposit(500)
    account1.withdraw(200)

    txn = account1.get_transaction_history()[1] 

    assert txn['timestamp'] is not None
    assert isinstance(txn['timestamp'], datetime)













    

