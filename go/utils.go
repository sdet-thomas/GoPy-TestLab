package main

import (
    "fmt"
    "os/exec"
)

// Ping executes a ping command to the specified IP with the given count
// Returns true if ping was successful, false otherwise
func Ping(ip string, count ...int) (bool, error) {
    pingCount := 1
    if len(count) > 0 && count[0] > 0 {
        pingCount = count[0]
    }
    
    // Execute the ping command and capture its output
    cmd := exec.Command("ping", "-c", fmt.Sprintf("%d", pingCount), ip)
    out, err := cmd.CombinedOutput() // Captures both stdout and stderr
    fmt.Println(string(out))         // Print the output as a string
    
    // If there was no error, the ping was successful
    return err == nil, err
}