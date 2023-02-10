#---------------------------------------------------------------------------------------------------#
#                                     Übungsaufgabe DLT Döner                                       #
#---------------------------------------------------------------------------------------------------#
# Klasse:       ETS21
# Bearbeiter:   Kevin, Eugen, Christian, Tim, Lars, Phillip
# Stand:        08.02.2023

#---------------------------------------------------------------------------------------------------#
#                                             Imports                                               #
#---------------------------------------------------------------------------------------------------#
import iota_client
import json
import datetime

#---------------------------------------------------------------------------------------------------#
#                                  Initialization of the methods                                    #
#---------------------------------------------------------------------------------------------------#
def fetch_data(node_url:str,index_key:str ) -> list[dict]:
    """
    A fuction to fetch all data of an index key from a given DLT
    
    Args:
        node_url: the url of the DLT node
        index_key: the key you want the node to fetch for

    Returns:
        a list of dicts with all entrys on the given Topic
    """
    # create node client
    client = iota_client.Client(nodes_name_password=[[node_url]])

    # find messages to the given indexation key

    message_list = client.find_messages(indexation_keys=[index_key])
    json_list = []

    # create a list of dicts from the messages strings
    for msg in message_list:
        payload = msg['payload']['indexation'][0]['data']
        pl_string = "".join(chr(char)for char in payload)
        json_list.append(json.loads(pl_string))

    return json_list

def check_consistency(data:list[dict]):
    """
    A function to check for the consistency of the given data. 
    Checks whether the entries make sense chronologically and 
    whether there is an entry for check-in and check-out for each transport action.

    Args:
        data: The list of data to check for consistency.

    Returns:
        True if the data are consistent; False, if not.
    """

    check_history = ''

    # check if 'in' and 'out' are always in canhge
    for i in range(len(data)-1):
        if data[i]['direction'] == 'in':
            if data[i+1]['direction'] == 'out':
                pass
            else:
                return False, f"Mehrere Check-In Einträge in Folge bei Station {data[i]['transportstation']}, {data[i]['timestamp']} und {data[i+1]['transportstation']}, {data[i+1]['timestamp']}"
        elif data[i]['direction'] == 'out':
            if data[i+1]['direction'] == 'in':
                pass
            else:
                return False, f"Mehrere Check-Out Einträge in Folge bei Station {data[i]['transportstation']}, {data[i]['timestamp']} und {data[i+1]['transportstation']}, {data[i]['timestamp']}"

    for entry in data:
        
        # check if every 'out' hast a 'in' on the same station
        if entry['direction'] == 'out':
            if not any(d['direction'] == 'in' and d['transportstation'] == entry['transportstation'] for d in data):
                return False, f"Kein Check-In Eintrag für Station {entry['transportstation']}"
        # check if every 'out' tmestamp is after the matching 'in' timestamp
            elif not any(d['timestamp'] < entry['timestamp'] and d['transportstation'] == entry['transportstation'] for d in data):
                return False, f"Station {entry['transportstation']} Check-Out ist vor Check-In" 
        # check if not more than one 'in' whithout 'out' is existing on the tangle
        elif entry['direction'] == 'in':
            if not any(d['direction'] == 'out' and d['transportstation'] == entry['transportstation'] for d in data):
                if check_history != '':
                    return False, f"Mehr als eine Station hat keinen Check-Out Eintrag ({data['transportstation']} und {check_history})"

    return True, "Konsistenz der Transportkette OK"


def check_time_whithout_cooling(data:list[dict], max_time:int):
    """
        Eine Funktion zum überprüfend der Transportdaten. 
        Prüft, ob eine maximale Zeit zwischen den Lieferstationen 
        ohne Kühlung überschritten wurde.

        Args:
            data: Liste der zu überprüfenden Daten.
            max_time: Maximale Zeit zwischen den Lieferstationen

        Returns:
            True, wenn die Maximale dauer eingehalten wurde.
    """

    for i in range(1, len(data)):
        if data[i]['direction'] == 'in':
            in_timestamp = datetime.datetime.strptime(data[i]['timestamp'],"%d.%m.%Y %H:%M:%S")
            out_timestamp = datetime.datetime.strptime(data[i-1]['timestamp'], "%d.%m.%Y %H:%M:%S")

            zeit_diff = (in_timestamp - out_timestamp)

            if zeit_diff.seconds >= (max_time*60):
                return False, f"Maximale Zeit ohne Kühlung überschritten zwischen Station '{data[i-1]['transportstation']}' und Station '{data[i]['transportstation']}': {zeit_diff}"

    return True, "Maximale Zeit ohne Kühlng OK"

def check_total_transport_time(data:list[dict], max_time:int):
    """
        Eine Funktion zur Überprüfung der gesamtlieferdauer der Kühlkette

        Args:
            data: Liste der zu überprüfenden Daten.
            max_time: Maximale Gesamtdauer der Lieferkette.

        Returns:
            True, wenn die maximale Dauer eingehalten wurde.
    """
    anfangszeit = datetime.datetime.strptime(data[0]['timestamp'],"%d.%m.%Y %H:%M:%S")
    endzeit = datetime.datetime.strptime(data[-1]['timestamp'],"%d.%m.%Y %H:%M:%S")

    dauer = endzeit-anfangszeit

    if dauer.seconds >= (max_time * 60 * 60):
        return False, f"Maximale Transportzeit überschritten: {dauer}"

    return True, "Maximale Transportdauer OK"


def check_data(entries:list[dict], transport_id:str) -> None:
    """
        A function to check the given trandport-id for multiple conditions

        Args:
            entries: all entries to all transport ids from the tangle
            transport_id: the transport-id to check for the conditions

        Returns:
            Nothing
    """

    print(f"Überprüfe Transport-ID {e}...")

    # list of data from the wanted transport id
    transport_data = []
    for entry in entries:
        if entry["transportid"] == transport_id:
            transport_data.append(entry)
    
    if not transport_data == []:
        transport_data = sorted(transport_data, key=lambda x: x['timestamp'])
        c = check_consistency(transport_data) 
        if  c[0] == True:
            print("Konsistenz der Lieferkette: \u2705")
        else:
            print("Konsistenz der Lieferkette: \u274c")
            print(c[1])

        c = check_time_whithout_cooling(transport_data, 10)
        if c[0] == True:
            print("Zeit ohne Kühlung: \u2705")
        else:
            print("Zeit ohne Kühlung: \u274c")
            print(c[1])

        c = check_total_transport_time(transport_data, 48)
        if c[0] == True:
            print("Gesamte Transportzeit: \u2705")
        else:
            print("Gesamte Transportzeit: \u274c")
            print(c[1])

        print()
        return
    
    print("Transport-ID nicht gefunden! \U0001F62D \n")

#---------------------------------------------------------------------------------------------------#
#                                           Main code                                               #
#---------------------------------------------------------------------------------------------------#
print()
print('################################################')
print('#       Überprüfung der Lieferkette            #')
print('################################################')
print('    * Laden der Lieferdaten')
tangle_data = fetch_data('https://api.lb-0.h.chrysalis-devnet.iota.cafe', 'Food Solution Hildesheim')
print('    * OK')
print()
"""
# for manual input of the transport ids
while True:     
    print()                                          
    transport_id = input("    * Bitte Transport ID eingeben:")      
    check_data(tangle_data, transport_id)
"""

# for automatic iteration of all given transport ids
transportIDs = [
    72359278599178561029675,
    15668407856331648336231,
    73491878556297128760578,
    99346757838434834886542,
    46204863139457546291334,
    77631003455214677542311,
    34778534098134729847267,
    64296734612883933474299,
    84356113249506843372979,
    23964376768701928340034,
    55638471099438572108556,
    84552276793340958450995,
    96853785349211053482893,
    68345254400506854834562,
    67424886737245693583645,
    85746762813849598680239,
    56993454245564893300000,
    95662334024905944384522,
    13456783852887496020345,
    76381745965049879836902]

for e in transportIDs:

    check_data(tangle_data, str(e))
