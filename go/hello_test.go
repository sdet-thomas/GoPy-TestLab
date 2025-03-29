package main

import (
    "fmt"
    "os"
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

// Test for PingTest
func TestPing(t *testing.T) {
    // Skip test only when running in GitHub Actions
    if os.Getenv("GITHUB_ACTIONS") == "true" {
        t.Skip("Skipping TestPing in GitHub Action workflow")
    }

    tests := []struct {
        name          string
        ip            string
        count         int
        expectNoError bool
    }{
        {
            name:          "Valid Ping",
            ip:            "9.9.9.9",
            count:         1,
            expectNoError: true,
        },
        {
            name:          "Invalid Ping",
            ip:            "9.9.9.8",
            count:         1,
            expectNoError: false,
        },
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            success, err := Ping(tt.ip, tt.count)
            if tt.expectNoError {
                assert.NoError(t, err, "Ping to %s should be successful", tt.ip)
                assert.True(t, success, "Ping to %s should return true", tt.ip)
            } else {
                assert.Error(t, err, "Ping to %s should fail", tt.ip)
                assert.False(t, success, "Ping to %s should return false", tt.ip)
            }
        })
    }
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