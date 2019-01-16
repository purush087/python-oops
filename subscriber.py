import sys
import zmq

port = "5556"
port1 = ""
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

topic_filter = "10001"
socket.setsockopt(zmq.SUBSCRIBE, topic_filter)

# Process 5 updates
total_value = 0
for update_nbr in range(5):
    string = socket.recv()
    topic, message_data = string.split()
    total_value += int(message_data)
    print(topic, message_data)
