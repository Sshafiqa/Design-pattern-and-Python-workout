# Example 1
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('example.com', username='yourusername', password='yourpassword')

stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())
ssh.close()

# Example 2
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('example.com', username='yourusername', password='yourpassword')

sftp = ssh.open_sftp()
sftp.put('localfile.txt', '/remote/path/localfile.txt')
sftp.close()
ssh.close()
