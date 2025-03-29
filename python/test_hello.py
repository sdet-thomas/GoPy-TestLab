import subprocess
from ssh_client import SSHClient
import pytest
from utils import ping  

# Function to be tested
def hello():
    return "Hello, World!"

# Test for the hello function
def test_hello():
    expected = "Hello, World!"
    actual = hello()
    assert actual == expected, "The hello function should return 'Hello, World!'"

@pytest.mark.parametrize(
    "ip_address, expected_success, expected_error",
    [
        ("9.9.9.9", True, None),  # Successful ping
        ("9.9.9.8", False, "Ping to 9.9.9.8 should return an error"),  # Unsuccessful ping
    ],
)
def test_ping(ip_address, expected_success, expected_error):
    success, error = ping(ip_address)
    assert success == expected_success, f"Ping to {ip_address} should {'succeed' if expected_success else 'fail'}"
    if expected_error:
        assert error is not None, f"Ping to {ip_address} should return an error"
    else:
        assert error is None, f"Ping to {ip_address} should not return an error"

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