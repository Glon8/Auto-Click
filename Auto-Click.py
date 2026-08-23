from data.helpers import config_parse, read_file
from data.values import op
from data.visuals import render
from data.killswitch import ks_switch
from data.display import display_switch
from data.auto_click import acc_prot, acc_switch, acc_handler
from data.settings import mode_switch, mouse_switch

from pynput.keyboard import Controller as K, Listener as kL, HotKey
from pynput.mouse import Controller as M, Listener as mL, Button

k = K()
m = M()


# ===================================< CONTROL PANNEL
def control_panel():
    while True:
        if op['ks']['stat']:
            acc_prot()


# ===================================< MAIN
def main():
    config_parse(read_file('config.json'))
    acc = op['acc']

    # \/===================================< HOTKEYS SETTINGS
    def mouse_click(x, y, button, pressed):
        if button == Button.left and pressed:
            if not acc['use_mouse']:
                acc_handler()

    hotkeys = [
        HotKey(HotKey.parse(op['gnr']['key_display_change']), display_switch),
        HotKey(HotKey.parse(op['ks']['key_trigger']), ks_switch),
        HotKey(HotKey.parse(acc['key_trigger']), acc_switch),
        HotKey(HotKey.parse(acc['key_clip_mode']), mode_switch),
        HotKey(HotKey.parse(acc['key_use_mouse']), mouse_switch),
    ]

    def on_press(key):
        for thing in hotkeys:
            thing.press(key)

    def on_release(key):
        for thing in hotkeys:
            thing.release(key)

    # /\===================================< HOTKEYS SETTINGS

    render()

    with kL(on_press=on_press, on_release=on_release), mL(on_click=mouse_click):
        control_panel()


# ===================================< MAIN START
if __name__ == '__main__':
    main()
