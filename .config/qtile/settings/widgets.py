from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='MesloLGS NF',
            fontsize=20,
            margin_y=2,
            margin_x=0,
            padding_y=8,
            padding_x=2,
            borderwidth=1,
            active=colors['color4'],
            inactive=colors['text'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['text'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='text'), fontsize=14, padding=2),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    separator(),

    # Layout
    widget.CurrentLayoutIcon(**base(bg="grey", fg="color3"), scale=0.65),
    widget.CurrentLayout(**base(bg='grey'), padding=5),

    # Wifi
    icon(bg="grey", fg="color4", text='  '),
    widget.Net(**base(bg='grey'), interface='enp0s3'),

    # Pacman updates
    icon(bg="grey", fg="color2", text='  '),
    widget.CheckUpdates(**base(bg='grey'), distro='arch'),

    # CPU usage
    icon(bg="grey", fg="color3", text=' 龍 '),
    widget.CPU(**base(bg='grey')),

    # Load
    icon(bg="grey", fg="color1", text=' 勒 '),
    widget.Load(**base(bg='grey')),

    # Memory
    icon(bg="grey", fg="color2", text='  '),
    widget.Memory(**base(bg='grey'), measure_mem="M"),

    # Battery
    # icon(bg="grey", fg="color4", text='  '),
    # widget.Battery(**base(bg='grey')),

    # Clock/calendar
    icon(bg="grey", fg="color3", fontsize=17, text='  '),
    widget.Clock(**base(bg='grey'), format='%H:%M '),

    # Tray
    widget.Systray(background=colors['dark'], padding=5),

    # Shutdown button
    widget.QuickExit(**base(bg='grey', fg="urgent"), countdown_start=9, default_text=" ⏻ Elo "),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    widget.CurrentLayoutIcon(**base(bg='grey'), scale=0.65),

    widget.CurrentLayout(**base(bg='grey'), padding=5),

    widget.Clock(**base(bg='grey'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'MesloLGS NF Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
