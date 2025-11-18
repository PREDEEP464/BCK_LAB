# BCK_LAB - Blockchain and Cryptography Laboratory

This repository contains experiments and implementations related to blockchain technology and cryptographic concepts.

## Setup Instructions

### 1. Clone the Repository

Open VS Code → Terminal and run:

```powershell
git clone https://github.com/PREDEEP464/BCK_LAB.git
```

Open the cloned folder in VS Code:

```powershell
cd BCK_LAB
```

### 2. Remove Git Tracking and Verify

Delete the `.git` folder to remove all version control:

```powershell
Remove-Item -Recurse -Force .git
```

Verify Git has been removed:

```powershell
git status
```

**Expected output:**
```
fatal: not a git repository
```

### 3. Repository Structure

```
BCK_LAB/
├── Exp1/
│   └── exp1.py
├── Exp2/
│   └── exp2.py
├── Exp3/
│   └── exp3.py
├── Exp4/
│   └── exp4.py
├── Exp5/
│   └── exp5.py
├── Exp6/
│   └── exp6.py
├── sample_files/
│   ├── file2.txt
│   ├── file3.txt
│   └── file4.txt
```

## Experiments Overview

- **Exp1**: Merkle Tree implementation (SHA-256) 
- **Exp2**: Digital Signatures with ECDSA 
- **Exp3**: Blockchain implementation 
- **Exp4**: Proof of Work blockchain 
- **Exp5**: Cryptographic key generation 
- **Exp6**: Advanced blockchain features 
