import copy
import os
import sys
import json
import time
import random

from pathlib import Path
from pynput.keyboard import Controller as K

from .values import op

k = K()


# ===================================< SWITCH
# dic - dictionary to use
# key - from the dictionary to flip
def switch(dic, key):
    if not dic or not isinstance(dic, dict):
        return

    item = dic.get(key)

    if item is None or not isinstance(item, bool):
        return

    dic[key] = not dic[key]


# ===================================< KEY PRESS
# key - to press
# delay - between press and release
def key_press(key, min_delay, max_delay):
    if not isinstance(min_delay, int) or not isinstance(max_delay, int):
        return

    if min_delay > max_delay:
        min_delay, max_t = max_delay, min_delay

    k.press(key)

    timeout(min_delay, max_delay)

    k.release(key)


# ===================================< FILES COUNT
def files_count(file_path):
    return sum(len(files) for _, _, files in os.walk(file_path))


# ===================================< GET DIRECTORY
def getDir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))

    return str(Path(__file__).resolve().parent.parent)


# ===================================< WRITE FILE
def write_file(file_path, file_name, data):
    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return None

    with open(f'{file_path}/{file_name}', 'w') as file:
        json.dump(data, file, indent=4)


# ===================================< READ FILE
# file_path - to read from
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


# ===================================< CONFIG PARSER
# string - to pars in to config
def config_parse(string):
    if string == '' or string is None:
        write_file(getDir(), 'config.json', op)
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    for name, value in config_pack.items():
        for key, val in value.items():
            if key != 'name' and name != 'ks':
                op[name][key] = val


# ===================================< CONFIG PARSER ON REREAD
# string - to pars in to config
def config_parse_reread(string):
    if string == '' or string is None:
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    valid_keys = ['display', '.settings', 'key_trigger', 'key_action',
                  'mouse', 'mode', 'key_mode', 'key_mouse']

    for name, value in config_pack.items():
        for key, val in value.items():
            if key in valid_keys and op[name][key] != val and name != 'ks':
                op[name][key] = val


# ===================================< UNICODE CONVERT

def unicode_convert(unicode):
    return chr(int(unicode[2:], 16))


# ===================================< TIMEOUT (acc)
def timeout(min_t, max_t):
    if not isinstance(min_t, int) or not isinstance(max_t, int):
        return

    if min_t > max_t:
        min_t, max_t = max_t, min_t

    timeout = random.randint(min_t, max_t) / 1000
    time.sleep(timeout)


# ===================================< DISTURBANCE (acc)
def disturbance(host):
    if not host or not isinstance(host, dict):
        return

    sett = host.get('.settings')

    if not sett:
        print('disturbance func error: host not contain .settings')
        return

    if not isinstance(sett.get('.max_disturbance'), int):
        sett['.max_disturbance'] = 50

    return random.randint(0, sett['.max_disturbance'])
