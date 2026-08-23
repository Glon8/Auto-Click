from .helpers import switch, key_press, timeout, disturbance
from .values import op
from .visuals import render

from pynput.mouse import Controller as M, Button

m = M()


# ===================================< AUTO CLICK CLIP
def acc_switch():
    if not op['ks']['stat']:
        return

    acc = op['acc']

    switch(acc, 'stat')

    if not acc['use_mouse']:
        acc['trigger'] = False
    else:
        switch(acc, 'trigger')

    render()

    if acc['stat'] and acc['clip_mode']:
        acc['count'] = 0


def acc_handler():
    if not op['ks']['stat']:
        return

    acc = op['acc']

    if op['ks']['stat'] and acc['stat']:
        switch(acc, 'trigger')
        render()


def acc_prot():
    if not op['ks']['stat']:
        return

    acc = op['acc']

    if acc['stat'] and acc['trigger']:
        if not acc['use_mouse']:
            key_press(acc['key_action'],
                      int(acc['.settings']['.min_delay'] + disturbance(acc)),
                      int(acc['.settings']['.max_delay'] + disturbance(acc)))
        else:
            m.click(Button.left)

        if acc['clip_mode'] and acc['count'] < acc['.settings']['.clicks_cap']:
            acc['count'] += 1

    if acc['clip_mode'] and acc['trigger'] and acc['count'] >= acc['.settings']['.clicks_cap']:
        if acc['use_mouse']:
            switch(acc, 'stat')
        switch(acc, 'trigger')
        render()
        acc['count'] = 0
    else:
        timeout(int(acc['.settings']['.min_delay'] + disturbance(acc)), int(acc['.settings']['.max_delay'] + disturbance(acc)))
