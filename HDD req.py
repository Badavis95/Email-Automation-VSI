# Prompt user for input
store = input("Enter Store: ")
registerNum = input("Enter Register #: ")
numOfRegisters = input("Enter Number of Registers at the store: ")
typeOfRegister = input("Enter Type of Register: ")
nextTransactionNum = input("Enter Next Transaction #: ")
ezvTicket = input("Enter EZV Ticket #: ")
ipAddress = input("Enter IP Address: ")
tillFloat = input("Enter Till Float: ")
safeFloat = input("Enter Safe Float: ")

# Format the message
message = f"""
Good Afternoon,

Can you please image hard drives for Store {store}

• Register # : {registerNum}
• Number of Registers at the store: {numOfRegisters}
• Type of Register: {typeOfRegister}
• Next Transaction # : {nextTransactionNum}
• EZV Ticket #: {ezvTicket}
• IP Address: {ipAddress}
• Till Float: {tillFloat}
• Safe Float: {safeFloat}

Thank you,
"""

# Generate the filename
file_path = f"Store {store} Register {registerNum} New Hard Drive Request.txt"
with open(file_path, 'a') as file:
    file.write(message)

print("File updated successfully!")

