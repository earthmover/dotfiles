from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and layout rules


bsp_conf = {
    'border_focus': colors['focus'][0],
    'border_normal': colors['grey'][0],
    'border_width': 4,
    'border_on_single': True,
    'margin': 8,
    'grow_amount': 4,
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
