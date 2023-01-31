from libqtile import layout
from libqtile.config import Match
from .theme import colors
from colors import catppuccin

# Layouts and layout rules


bsp_conf = {
    'border_focus': catppuccin["Lavender"],
    'border_normal': catppuccin["Crust"],
    'border_width': 6,
    'border_on_single': True,
    'margin': 12,
    'grow_amount': 1,
    'lower_right': True,
    'fair': False,
    'ratio': 1.6,

}

zoomy_conf = {
    "margin": 10,
    "column_width": 250,
}

layouts = [
    layout.Bsp(**bsp_conf),
    layout.Zoomy(**zoomy_conf),
    layout.Max(),
    # layout.TreeTab(),
    # layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.VerticalTile(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["focus"][0]
)
