import socket
import pickle

# Setup a socket to listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 12345))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        # Receive the serialized data from script1.py
        serialized_data = conn.recv(4096)

        # Deserialize the data structure
        received_data = pickle.loads(serialized_data)

        # Process the data (for example, add 1 to each number in the list)
        processed_data = {'key': 'processed', 'numbers': [x + 1 for x in received_data['numbers']]}

        # Serialize and send the processed data back to script1.py
        serialized_processed_data = pickle.dumps(processed_data)
        conn.sendall(serialized_processed_data)
