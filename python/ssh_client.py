import paramiko

class SSHClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def run_command(self, command):
        try:
            # Create an SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Insecure, for testing only

            # Connect to the SSH server
            client.connect(
                hostname=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                timeout=5
            )

            # Execute the command
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            # Get the exit status
            exit_status = stdout.channel.recv_exit_status()

            # Close the connection
            client.close()

            if exit_status != 0:
                return output, f"Command failed with exit status {exit_status}: {error}"
            return output, None
        except Exception as e:
            return "", str(e)