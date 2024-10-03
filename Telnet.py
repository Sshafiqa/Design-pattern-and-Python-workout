import telnetlib


def telnet_example(host, port, command):
    try:
        # Connect to the server
        tn = telnetlib.Telnet(host, port)

        # Send a command
        tn.write(command.encode('ascii') + b"\n")

        # Read the response
        response = tn.read_all().decode('ascii')

        print("Response from Telnet server:")
        print(response)

        tn.close()
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
telnet_example('example.com', 23, 'HELP')
