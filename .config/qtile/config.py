from libqtile import hook

from src.keys import mod, keys
from src.groups import groups
from src.layouts import layouts, floating_layout
from src.screens import screens
from src.mouse import mouse
from src.path import qtile_path

from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'qtile'
