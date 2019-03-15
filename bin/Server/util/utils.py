import json
import time


# change data format from bytes to json obj
def data_parse(data_input):
    data_json_str = data_input.decode('utf8').replace("'", '"')
    data_json_obj = json.loads(data_json_str)
    # return json.dumps(data_json_obj, indent=4, sort_keys=True)
    return data_json_obj


# change data format from dic to json_bytes
def data_encode(dict_info):
    return json.dumps(dict_info, indent=4, sort_keys=True)


# get timestamp from local
def get_timestamp():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(round(time.time() * 1000)) / 1000))
