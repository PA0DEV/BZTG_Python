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

    check_history = ''


    for entry in data:
        # check if every 'out' hast a 'in' on the same station
        if entry['direction'] == 'out':
            if not any(d['direction'] == 'in' and d['transportstation'] == entry['transportstation'] for d in data):
                return False, f"Missing check-in entry for transport station {entry['transportstation']}"
        # check if every 'out' tmestamp is after the matching 'in' timestamp
            elif not any(d['timestamp'] < entry['timestamp'] and d['transportstation'] == entry['transportstation'] for d in data):
                return False, f"Station {entry['transportstation']} check-out timestamp is before check-in timestamp" 
        # check if not more than one 'in' whithout 'out' is existing on the tangle
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
    
    if not transport_data == []:
        transport_data = sorted(transport_data, key=lambda x: x['timestamp'])
        c = check_consistency(transport_data) 
        if  c[0] == True:
            print("consistency: \u2714")
        else:
            print("consistency: \u274c")
            print(c[1])

        c = check_time_whithout_cooling(transport_data, 10)
        if c[0] == True:
            print("time whithout cooling: \u2714")
        else:
            print("time whithout cooling: \u274c")
            print(c[1])

        c = check_total_transport_time(transport_data, 48)
        if c[0] == True:
            print("total transport time: \u2714")
        else:
            print("total transport time: \u274c")
            print(c[1])

        print()
        return
    
    print("Transport ID not found!\n")

if __name__ == "__main__":
    tangle_data = fetch_data('https://api.lb-0.h.chrysalis-devnet.iota.cafe', 'Food Solution Hildesheim')

    # transport_id = input("Bitte Transport ID eingeben:")
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
        print(f"checking Transport id {e}...")

        check_data(tangle_data, str(e))
