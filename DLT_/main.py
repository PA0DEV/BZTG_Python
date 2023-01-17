import iota_client
import json
# Knoten aus dem Chrysalis-Devnet
node_url = 'https://api.lb-0.h.chrysalis-devnet.iota.cafe'
# Cient mit einem Knoten verbinden
client = iota_client.Client(nodes_name_password=[[node_url]])
# Messages zu einem Inxex suchen
mlist = client.find_messages(indexation_keys=["Food Solution Hildesheim"])
for message in mlist: # Schleife über alle gefundenen Messages
    pl = message['payload']['indexation'][0]['data'] # Daten => Liste mit Dezimalwert der Einzelzeichen
s = ''.join(chr(val) for val in pl) # Dezimalwerte in String umwandeln
d = json.loads(s) # Dictionary aus JSON-String erzeugen
for key in d: # Alle Einträge des Dictionary durchgehen
    print(key + ': ' + str(d[key])) # Schlüssel und Schlüsselwert ausgeben
print('------------------------------------------')