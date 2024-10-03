import paramiko


def ssh_example(host, port, username, password, command):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh.connect(host, port, username, password)

        # Execute a command
        stdin, stdout, stderr = ssh.exec_command(command)
        response = stdout.read().decode()
        print("Response from SSH server:")
        print(response)

        ssh.close()
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
ssh_example('example.com', 22, 'username', 'password', 'ls -l')
