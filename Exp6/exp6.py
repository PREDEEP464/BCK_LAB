# Smart Contract–Based Voting System

import hashlib
import json
import time

class VoteBlock:
    def __init__(self, voter_id, candidate, previous_hash):
        self.voter_id = voter_id
        self.candidate = candidate
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        data = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()


class VotingBlockchain:
    def __init__(self):
        self.chain = []
        self.voters = set()
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = VoteBlock("0", "Genesis", "0"*64)
        self.chain.append(genesis)

    def add_vote(self, voter_id, candidate):
        if voter_id in self.voters:
            print("Duplicate vote blocked:", voter_id)
            return
        
        prev_hash = self.chain[-1].hash
        block = VoteBlock(voter_id, candidate, prev_hash)
        self.chain.append(block)
        self.voters.add(voter_id)

        print(f"Vote added: {voter_id} → {candidate}")

    def tally_votes(self):
        result = {}
        for block in self.chain[1:]:
            result[block.candidate] = result.get(block.candidate, 0) + 1
        return result


if __name__ == "__main__":
    vc = VotingBlockchain()

    vc.add_vote("V001", "Alice")
    vc.add_vote("V002", "Bob")
    vc.add_vote("V003", "Alice")
    vc.add_vote("V001", "Alice") 

    print("\nFinal Tally:", vc.tally_votes())
    print("Blockchain length:", len(vc.chain))
