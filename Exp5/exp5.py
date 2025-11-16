# Decentralized Cryptocurrency Wallet

import secrets
import hashlib

def create_wallet():
    private_key = secrets.token_hex(32)  
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

ledger = {}

def get_balance(address):
    return ledger.get(address, 0)

def send_funds(sender, receiver, amount):
    if ledger.get(sender, 0) < amount:
        print("Insufficient balance.")
        return False
    
    ledger[sender] -= amount
    ledger[receiver] = ledger.get(receiver, 0) + amount
    print(f"Transaction successful: {sender[:10]} → {receiver[:10]} | Amount: {amount}")
    return True


if __name__ == "__main__":
    privA, addrA = create_wallet()
    privB, addrB = create_wallet()

    ledger[addrA] = 100

    print("Initial Balances:")
    print("A:", get_balance(addrA))
    print("B:", get_balance(addrB))

    send_funds(addrA, addrB, 40)

    print("\nFinal Balances:")
    print("A:", get_balance(addrA))
    print("B:", get_balance(addrB))
