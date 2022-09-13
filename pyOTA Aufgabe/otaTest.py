import iota

api = iota.Iota('https://nodes.thetangle.org:443', local_pow=True)

print(api.get_node_info())