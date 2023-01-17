from tracemalloc import start
import iota_client
import json
import datetime


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

    for msg in message_list:
        payload = msg['payload']['indexation'][0]['data']
        pl_string = "".join(chr(char)for char in payload)
        json_list.append(json.loads(pl_string))

    return json_list

def check_consistency(data:list[dict]) -> bool:
    """
    A function to check for the consistency of the given data. 
    Checks whether the entries make sense chronologically and 
    whether there is an entry for check-in and check-out for each transport action.

    Args:
        data: The list of data to check for consistency.

    Returns:
        True if the data are consistent; False, if not.
    """


    check_chrono = False
    check_history = ''

    station_list = []

    for entry in data:
        if entry['transportstation'] not in station_list:
            station_list.append(entry['transportstation'])

    for entry in data:
        # check if every 'out' hast a 'in' on the same station
        if entry['direction'] == 'out':
            if not any(d['direction'] == 'in' and d['transportstation'] == entry['transportstation'] for d in data):
                return False, f"Missing check-in entry for transport station {entry['transportstation']}"
        # check if every 'out' tmestamp is after the matching 'in' timestamp
            elif not any(d['timestamp'] < entry['timestamp'] and d['transportstation'] == entry['transportstation'] for d in data):
                return False, f"Station {entry['transportstation']} check-out timestamp is before check-in timestamp" 
        # check if not more3 than one 'in' whithout 'out' is existing on the tangle
        elif entry['direction'] == 'in':
            if not any(d['direction'] == 'out' and d['transportstation'] == entry['transportstation'] for d in data):
                if check_history != '':
                    return False, f"More than one station has no check-out entry ({data['transportstation']} and {check_history})"

    return True, "Transport consistency OK"
    
def check_time_whithout_cooling(data:list[dict], max_time:int) -> bool:

    for i in range(1, len(data)):
        if data[i]['direction'] == 'in':
            in_ts = datetime.datetime.strptime(data[i]['timestamp'],"%d.%m.%Y %H:%M:%S")
            out_ts = datetime.datetime.strptime(data[i-1]['timestamp'], "%d.%m.%Y %H:%M:%S")

            time_diff = (in_ts - out_ts)

            if time_diff.seconds >= (max_time*60):
                return False, f"Max time whithout cooling exceeded between station '{data[i-1]['transportstation']}' and station '{data[i]['transportstation']}': {time_diff}"

    return True, "Maximum time whithout cooling OK"

def check_total_transport_time(data:list[dict], max_time:int):
    start_ts = datetime.datetime.strptime(data[0]['timestamp'],"%d.%m.%Y %H:%M:%S")
    end_ts = datetime.datetime.strptime(data[len(data)-1]['timestamp'],"%d.%m.%Y %H:%M:%S")

    duration = end_ts-start_ts

    if duration.seconds >= (max_time * 60 * 60):
        return False, f"Maximum total transport time exceeded: {duration}"

    return True, "Maximum transport time OK"


def check_data(entries:list[dict], transport_id:str):
    # list of data from the wanted transport id
    transport_data = []
    for entry in entries:
        if entry["transportid"] == transport_id:
            transport_data.append(entry)
    
    transport_data = sorted(transport_data, key=lambda x: x['timestamp'])
    print(check_consistency(transport_data))
    print(check_time_whithout_cooling(transport_data, 10))
    print(check_total_transport_time(transport_data, 48))
    

if __name__ == "__main__":
    tangle_data = fetch_data('https://api.lb-0.h.chrysalis-devnet.iota.cafe', 'Food Solution Hildesheim')

    while True:
        transport_id = input("Bitte Transport ID eingeben:")
        check_data(tangle_data, transport_id)