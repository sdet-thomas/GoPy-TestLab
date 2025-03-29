import subprocess
from ssh_client import SSHClient
import pytest

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

@pytest.mark.parametrize(
    "name, command, expected, should_error",
    [
        ("Valid SSH Command", "whoami", "demo", False),
        ("Invalid SSH Command", "invalidcommand", "Command failed with exit status 127", True),
        ("Echo Command", 'echo "Hello world!"', "Hello world!", False),
    ],
)
def test_ssh_commands(name, command, expected, should_error):
    # Define a single SSHClient instance
    client = SSHClient(
        host="test.rebex.net",
        port=22,
        username="demo",
        password="password"
    )

    output, error = client.run_command(command)
    print(f"Test: {name}")
    print(f"Output: {output}")  # Debugging output
    print(f"Error: {error}")    # Debugging error

    if should_error:
        assert error is not None, f"{name} should return an error"
        assert "exit status 127" in error, f"{name} error message should indicate exit status 127"
    else:
        assert error is None, f"{name} should execute without errors"
        assert expected in output, f"{name} output should contain expected result"