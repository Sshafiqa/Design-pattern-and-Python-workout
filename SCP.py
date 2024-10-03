from paramiko import SSHClient
from scp import SCPClient


def scp_example(host, port, username, password, local_file, remote_file):
    try:
        # Create an SSH client
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        # Use SCP to transfer files
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_file, remote_file)
            print(f"File {local_file} uploaded to {remote_file}")

        ssh.close()
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
scp_example('example.com', 22, 'username', 'password', 'local_file.txt', 'remote_file.txt')
