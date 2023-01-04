#!/bin/sh

# set resolution
xrandr -s 3840x2160 &
# load xresources
xrdb -merge ~/Xresources &
# set wallpaper
./.fehbg &
# picom compositor
picom &
