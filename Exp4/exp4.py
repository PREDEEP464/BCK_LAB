# Blockchain With Consensus Mechanism

import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce, self.hash = self.mine_block()

    def compute_hash(self, nonce):
        data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": nonce
        }, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty="000"):
        nonce = 0
        while True:
            h = self.compute_hash(nonce)
            if h.startswith(difficulty):   
                return nonce, h
            nonce += 1


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, ["Genesis Block"], "0"*64)
        self.chain.append(genesis)

    def add_block(self, transactions):
        prev_hash = self.chain[-1].hash
        block = Block(len(self.chain), transactions, prev_hash)
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            prev = self.chain[i-1]
            curr = self.chain[i]

            if curr.previous_hash != prev.hash:
                return False
            
            if curr.hash != curr.compute_hash(curr.nonce):
                return False
        
        return True


def consensus(chains):
    longest = max(chains, key=lambda bc: len(bc.chain))
    for bc in chains:
        bc.chain = list(longest.chain)
    return longest.chain


if __name__ == "__main__":

    node1 = Blockchain()
    node2 = Blockchain()
    node3 = Blockchain()

    node1.add_block(["A pays B 5"])
    node1.add_block(["C pays D 7"])

    node2.add_block(["X pays Y 10"])

    node3.add_block(["M pays N 2"])
    node3.add_block(["N pays O 4"])

    print("\nBefore Consensus:")
    print("Node1 chain length:", len(node1.chain))
    print("Node2 chain length:", len(node2.chain))
    print("Node3 chain length:", len(node3.chain))

    consensus([node1, node2, node3])

    print("\nAfter Consensus:")
    print("Node1 chain length:", len(node1.chain))
    print("Node2 chain length:", len(node2.chain))
    print("Node3 chain length:", len(node3.chain))
