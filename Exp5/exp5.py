import secrets
import hashlib

# Create a new wallet
def create_wallet():
    private_key = secrets.token_hex(32)  # 256-bit private key
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

# Ledger to store account balances
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
    # Create two wallets
    privA, addrA = create_wallet()
    privB, addrB = create_wallet()

    # Assign starting balance
    ledger[addrA] = 100

    print("Initial Balances:")
    print("A:", get_balance(addrA))
    print("B:", get_balance(addrB))

    # Perform transaction
    send_funds(addrA, addrB, 40)

    print("\nFinal Balances:")
    print("A:", get_balance(addrA))
    print("B:", get_balance(addrB))
