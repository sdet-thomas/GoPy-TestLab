package main

import (
	"bytes"
	"fmt"
	"golang.org/x/crypto/ssh"
	"time"
)

// SSHClient struct to hold SSH connection details
type SSHClient struct {
	Host     string
	Port     string
	Username string
	Password string
}

// RunCommand connects to the SSH server and runs the specified command
func (client *SSHClient) RunCommand(command string) (string, error) {
	config := &ssh.ClientConfig{
		User: client.Username,
		Auth: []ssh.AuthMethod{
			ssh.Password(client.Password),
		},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
		Timeout:         5 * time.Second,
	}

	// Connect to the SSH server
	connection, err := ssh.Dial("tcp", fmt.Sprintf("%s:%s", client.Host, client.Port), config)
	if err != nil {
		return "", fmt.Errorf("failed to connect to SSH server: %w", err)
	}
	defer connection.Close()

	// Create a session
	session, err := connection.NewSession()
	if err != nil {
		return "", fmt.Errorf("failed to create SSH session: %w", err)
	}
	defer session.Close()

	// Run the command and capture the output
	var outputBuffer bytes.Buffer
	session.Stdout = &outputBuffer
	if err := session.Run(command); err != nil {
		return "", fmt.Errorf("failed to run command: %w", err)
	}

	return outputBuffer.String(), nil
}