def decode_password(encoded_password=''):
    if encoded_password == '':
        return ''
    decoded_password = ""
    shift = int(encoded_password[-1])
    encoded_password = encoded_password[:-1]
    for i in range(0, len(encoded_password), 2):
        decoded_password += chr(int(encoded_password[i:i+2], 16) - shift)
    return decoded_password

def encode_password(s):
    shift = len(s) % 10
    hex_str = ""
    for c in s:
        hex_str += format(ord(c) + shift, "02x")
    hex_str += str(shift)
    return hex_str


with open("export_heidi.txt", "r") as f:
    settings = f.read()

# print(encode_password('prod_password'))
# print(encode_password('dev_password'))

connections = []
current_connection = {}

for line in settings.split("\n"):
    if line.startswith("Servers\\"):
        # A new connection setting
        subkeys = line.split("\\")
        conn_name = subkeys[1]
        line_details = subkeys[2].split("<|||>")

        ignoreLine = False
        try:
            key = line_details[0]
            value = line_details[2]
        except IndexError:
            ignoreLine = True
            continue

        if not current_connection or current_connection["name"] != conn_name:
            # Add the previous connection to the list
            if current_connection:
                connections.append(current_connection)
            # Start a new connection dictionary
            current_connection = {"name": conn_name}
        # Add the key-value pair to the current connection dictionary
        current_connection[key.strip()] = value.strip()

# Add the last connection to the list of connections
if current_connection:
    connections.append(current_connection)

# Print the list of connections and their settings
for conn in connections:

    print(f"Connection name: {conn.get('name', '')}")
    print(f"Host: {conn.get('Host', '')}")
    print(f"Port: {conn.get('Port', '')}")
    print(f"User: {conn.get('User', '')}")
    print(f"Password (encoded): {conn.get('Password', '')}")
    print(f"Password (decoded): {decode_password(conn.get('Password', ''))}")
    # just to have some more log data
    print(f"Library: {conn.get('Library', '')}")
    print(f"ServerVersion: {conn.get('ServerVersion', '')}")
    print(f"ServerVersionFull: {conn.get('ServerVersionFull', '')}")
    print()
