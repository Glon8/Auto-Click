_OPERATIONS = {
    'gnr': {
        'name': 'General',
        'note': "Display is either 'emoji' or 'plain'",
        'key_display_change': 'c+o',
        'display': 'plain',
        '.settings': {
            '.positive_emoji': "U+2705",
            '.negative_emoji': "U+274C"
        },
    },
    'ks': {
        'name': 'Kill Switch',
        'note': 'Do not abuse Kill Switch! May lower performance!',
        'key_trigger': 'c+0',
        'stat': False,
    },
    'acc': {
        'name': 'Auto Click Clip',
        'note': 'Remember to set Kill Switch on before use!',
        'key_trigger': 'c+1',
        'stat': False,
        'trigger': False,
        'key_action': 'v',
        'count': 0,
        'key_clip_mode': 'c+[',
        'clip_mode': True,
        'key_use_mouse': 'c+]',
        'use_mouse': False,
        '.settings': {
            '.min_delay': 135,
            '.max_delay': 175,
            '.max_disturbance': 100,
            '.clicks_cap': 20,
        },
    },
}

_SEPERATOR = f"===========================<"

op = _OPERATIONS
