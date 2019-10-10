#Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """Returns the last value of the curent blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """Append a new value as well as the last blockchain value to the blockchain.
    :argument
        :transaction_amount: the amount that should be added.
        :last_transaction: the last blockchain transaction(default[1].)
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """Returns the input of the user (a new transaction amount) as a float. """
    user_input = float(input('Your transaction amout please:'))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    for block in blockchain:
        print('Outputting Block')
        print(block)

print('Done!')

