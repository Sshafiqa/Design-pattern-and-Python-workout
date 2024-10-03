from ftplib import FTP


def ftp_example(host, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(host)
        ftp.login(username, password)

        # List files in the current directory
        files = ftp.nlst()
        print("Files in FTP directory:")
        for file in files:
            print(file)

        # Upload a file
        with open('test.txt', 'rb') as file:
            ftp.storbinary('STOR test.txt', file)

        # Download a file
        with open('downloaded_test.txt', 'wb') as file:
            ftp.retrbinary('RETR test.txt', file.write)

        ftp.quit()
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
ftp_example('ftp.example.com', 'username', 'password')
