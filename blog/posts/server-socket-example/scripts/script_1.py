import socket
import pickle

data_structure = {'key': 'value', 'numbers': [1, 2, 3]}

# Serialize the data structure
serialized_data = pickle.dumps(data_structure)

# Send the serialized data to script2.py
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345))
    s.sendall(serialized_data)

    # Receive the processed data from script2.py
    received_data = s.recv(4096)

# Deserialize and print the processed data
processed_data = pickle.loads(received_data)
print("Processed data received from script2.py:", processed_data)
