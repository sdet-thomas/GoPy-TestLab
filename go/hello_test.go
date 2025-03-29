package main

import (
    "fmt"
    "os/exec"
    "testing"

    "github.com/stretchr/testify/assert"
)

// Function to be tested
func Hello() string {
    return "Hello, World!"
}

// Test using Testify
func TestHello(t *testing.T) {
    expected := "Hello, World!"
    actual := Hello()

    // Use Testify's assert to validate the result
    assert.Equal(t, expected, actual, "The Hello function should return 'Hello, World!'")
}

// Function to test pinging 9.9.9.9
func PingTest() error {
    // Execute the ping command and capture its output
    cmd := exec.Command("ping", "-c", "1", "9.9.9.9")
    out, err := cmd.CombinedOutput() // Captures both stdout and stderr
    fmt.Println(string(out))         // Print the output as a string
    return err                       // Return the error (if any)
}

// Test for PingTest
func TestPing(t *testing.T) {
    err := PingTest()

    // Assert that the ping command was successful
    assert.NoError(t, err, "Ping to 9.9.9.9 should be successful")
}

func TestSSHCommand(t *testing.T) {
    // Define a single SSHClient instance
    client := SSHClient{
        Host:     "test.rebex.net",
        Port:     "22",
        Username: "demo",
        Password: "password",
    }

    // Parameterize the commands and expected outputs
    tests := []struct {
        name     string
        command  string
        expected string
    }{
        {
            name:     "Valid SSH Command",
            command:  "whoami",
            expected: "demo",
        },
        {
            name:     "Invalid SSH Command",
            command:  "invalidcommand",
            expected: "",
        },
        {
            name:     "Echo Command",
            command:  `echo "Hello world!"`,
            expected: "Hello world!",
        },
        {
            name:     "ls Command",
            command:  "ls",
            expected: "readme.txt",
        },
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            output, err := client.RunCommand(tt.command)
            fmt.Printf("Output: %s\n", output) // Print the output for debugging
            fmt.Printf("Error: %v\n", err)      // Print the error for debugging
            if tt.name == "Invalid SSH Command" {
                assert.Error(t, err, "Invalid SSH command should return an error")
            } else {
                assert.NoError(t, err, "SSH command should execute without errors")
                assert.Contains(t, output, tt.expected, "Output should contain expected result")
            }
        })
    }
}