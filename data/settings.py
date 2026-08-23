from .values import op
from .helpers import switch
from .visuals import render


def mode_switch():
    if not op['ks']['stat']:
        return

    switch(op['acc'], 'clip_mode')

    render()


def mouse_switch():
    if not op['ks']['stat']:
        return

    op['acc']['stat'] = False

    switch(op['acc'], 'use_mouse')

    render()
