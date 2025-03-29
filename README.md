# GoPy-TestLab

## Project Description
GoPy-TestLab documents my journey of learning Golang while refreshing my Python skills, specifically for test automation as a Software Development Engineer in Test (SDET). This repository contains examples, tools, and resources focused on building robust test frameworks, automation scripts, and testing utilities that can be applied in real-world QA environments.

## Project Structure
```
├── .gitignore                # Gitignore file for Python, Go, and general patterns
├── README.md                 # This file
├── go/                       # Go code directory
│   ├── go.mod                # Go module definition
│   ├── go.sum                # Go module checksum file
│   ├── hello_test.go         # Go test file with Hello and ping examples
│   └── ssh_client.go         # SSH client implementation in Go
└── python/                   # Python code directory
    ├── ssh_client.py         # SSH client implementation in Python
    └── test_hello.py         # Python test file with hello and ping examples
```

## Features
The project currently implements and tests:

1. Basic "Hello, World!" functionality in both Go and Python
2. Network connectivity tests (ping to 9.9.9.9) in both languages
3. SSH client implementation in both languages with:
   - Connection to a test SSH server
   - Command execution and output capture
   - Error handling

## Getting Started

### Go Setup
1. Navigate to the Go directory:
   ```bash
   cd go
   ```
2. Run the tests:
   ```bash
   go test -v
   ```

### Python Setup
1. Navigate to the Python directory:
   ```bash
   cd python
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install paramiko pytest
   ```
5. Run the tests:
   ```bash
   pytest -v
   ```
6. When finished, deactivate the virtual environment:
   ```bash
   deactivate
   ```

## Dependencies

### Go
- Go 1.24.1
- github.com/stretchr/testify v1.10.0 (Assertion library)
- golang.org/x/crypto (For SSH functionality)

### Python
- paramiko (For SSH functionality)
- pytest (For testing)

## License
This project is licensed under the MIT License.

