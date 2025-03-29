import subprocess
from ssh_client import SSHClient

# Function to be tested
def hello():
    return "Hello, World!"

# Test for the hello function
def test_hello():
    expected = "Hello, World!"
    actual = hello()
    assert actual == expected, "The hello function should return 'Hello, World!'"

# Function to test pinging 9.9.9.9
def ping_test():
    try:
        # Execute the ping command and capture its output
        result = subprocess.run(
            ["ping", "-c", "1", "9.9.9.9"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        print("Command Output:", result.stdout)  # Print the output as a string
        return None  # No error
    except subprocess.CalledProcessError as e:
        print("Error Output:", e.stderr)  # Print the error output
        return e  # Return the error

# Test for the ping_test function
def test_ping():
    error = ping_test()
    assert error is None, "Ping to 9.9.9.9 should be successful"

def test_ssh_commands():
    # Define a single SSHClient instance
    client = SSHClient(
        host="test.rebex.net",
        port=22,
        username="demo",
        password="password"
    )

    # Parameterize the commands and expected outputs
    tests = [
        {"name": "Valid SSH Command", "command": "whoami", "expected": "demo"},
        {"name": "Invalid SSH Command", "command": "invalidcommand", "expected": "Command failed with exit status 127"},
        {"name": "Echo Command", "command": 'echo "Hello world!"', "expected": "Hello world!"},
    ]

    for test in tests:
        output, error = client.run_command(test["command"])
        print(f"Output: {output}")  # Debugging output
        print(f"Error: {error}")    # Debugging error

        if test["name"] == "Invalid SSH Command":
            assert error is not None, "Invalid SSH command should return an error"
            assert "exit status 127" in error, "Error message should indicate exit status 127"
        else:
            assert error is None, "SSH command should execute without errors"
            assert test["expected"] in output, "Output should contain expected result"