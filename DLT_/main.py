import iota_client

# create a client with a node
client = iota_client.Client(
    nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])

# print(client.get_info())

message = client.message(
 index="BZTG-Bio-Döner", data=[8]
)

msg_id = message["message_id"]

message = client.get_message_data(msg_id)
message_meta = client.get_message_metadata(msg_id)

print("Message meta data:")
print(message_meta)
print("Message data:")
print(message)
# print(message)
# print(msg_id)