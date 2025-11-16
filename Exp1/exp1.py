# Merkle Tree-Based Verification System

import os, hashlib, sys 

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def file_hash(path: str) -> str:
    with open(path, "rb") as f:
        return sha256_hex(f.read())

def merkle_layer(hashes):
    if len(hashes) % 2 == 1:
        hashes = hashes + [hashes[-1]]
    parent = []
    for i in range(0, len(hashes), 2):
        combined = bytes.fromhex(hashes[i]) + bytes.fromhex(hashes[i+1])
        parent.append(sha256_hex(combined))
    return parent

def build_merkle_tree(file_paths):
    leaves = [file_hash(p) for p in file_paths]
    tree = [leaves]
    layer = leaves
    while len(layer) > 1:
        layer = merkle_layer(layer)
        tree.append(layer)
    return tree 

def merkle_proof(tree, index):
    proof = []
    idx = index
    for layer in tree[:-1]:
        if idx % 2 == 0:
            sib = idx + 1 if idx + 1 < len(layer) else idx
        else:
            sib = idx - 1
        proof.append(layer[sib])
        idx = idx // 2
    return proof

def verify_proof(leaf_hash, proof, root, index):
    computed = leaf_hash
    idx = index
    for sib in proof:
        if idx % 2 == 0:
            combined = bytes.fromhex(computed) + bytes.fromhex(sib)
        else:
            combined = bytes.fromhex(sib) + bytes.fromhex(computed)
        computed = sha256_hex(combined)
        idx = idx // 2
    return computed == root

if __name__ == "__main__":
    folder = "sample_files"
    files = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".txt")])

    tree = build_merkle_tree(files)
    root = tree[-1][0]

    print("Files and leaf hashes:")
    for f, h in zip(files, tree[0]):
        print(f"{f} -> {h}")

    print("\nRoot hash:", root)

    proof = merkle_proof(tree, 1)
    print("\nProof for index 1:", proof)

    ok = verify_proof(tree[0][1], proof, root, 1)
    print("\nVerification result:", ok)
