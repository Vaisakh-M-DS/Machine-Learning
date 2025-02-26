# Open and read the file
with open("common-http-ports.txt", "r") as file:
    ports = file.readlines()

# Remove extra spaces and newlines
ports = [port.strip() for port in ports]

# Print first few ports
print("Common HTTP Ports:", ports[:10])  # Display first 10 ports
