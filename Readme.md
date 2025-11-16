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

### 3. Execute Files

Navigate to the experiment folder:

```powershell
cd ExperimentX
```

Run the Python file:

```powershell
python experimentX.py
```

*(Replace X with the experiment number you want to execute.)*

### 4. Install Dependencies

Make sure dependencies are installed:

```powershell
pip install ecdsa
```

## Repository Structure

```
BCK_LAB/
├── Exp1/
│   ├── exp1.py
│   └── sample_files/
│       ├── file2.txt
│       ├── file3.txt
│       └── file4.txt
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
└── README.md
```

## Experiments Overview

- **Exp1**: Merkle Tree implementation with SHA-256 hashing
- **Exp2**: [Add description]
- **Exp3**: [Add description]
- **Exp4**: [Add description]
- **Exp5**: [Add description]
- **Exp6**: [Add description]

## Requirements

- Python 3.x
- Required packages:
  - `ecdsa`
  - `hashlib` (built-in)
  - `os` (built-in)

## Usage

1. Follow the setup instructions above
2. Navigate to the desired experiment folder
3. Run the corresponding Python file
4. Follow any additional instructions provided in the experiment

## Notes

- Ensure you have Python installed on your system
- Install any missing dependencies using `pip install <package-name>`
- Each experiment folder contains its own implementation and test files