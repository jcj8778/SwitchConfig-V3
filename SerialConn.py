import serial
import time

# Define the serial connection parameters
port = 'COM5'  # Replace with the appropriate serial port
baudrate = 9600
timeout = 5

# Establish the serial connection
ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

# Wait for the connection to stabilize
time.sleep(2)

# Read the welcome message
welcome_message = ser.read_until(b'\r\n').decode('utf-8')
print(welcome_message)
# ser.write(b'admin\r\n')
time.sleep(1)
#
# # Send the password
# ser.write(b'switch\r\n')
# time.sleep(1)

# Read the command prompt
prompt = ser.read_until(b'#').decode('utf-8')
print(prompt)

# Define the commands to check for each setting
commands = {
    'Switch hostname': 'show run | include hostname',
    'IP IGMP Snooping': 'show ip igmp snooping',
    # Add more commands here
}

# Define the expected values for each setting
expected_values = {
    'Switch hostname': 'hostname FSH-NCC2-B',
    'IP IGMP Snooping': 'Disabled',
    # Add expected values here
}

# Send commands and compare the expected values with the actual output
for setting, command in commands.items():
    ser.write(command.encode('utf-8') + b'\r\n')
    ser.read_until(b'#')  # Wait for the prompt

    output = ser.read_until(b'#').decode('utf-8')
    # Compare the expected value with the actual output
    if expected_values[setting] in output:
        print(f'{setting}: Passed')
    else:
        print(f'{setting}: Failed')
        print(f'Expected: {expected_values[setting]}')
        print(f'Actual: {output}')
    print("=" * 50)
# Close the serial connection
ser.close()