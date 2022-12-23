#!/bin/sh

# set resolution
xrandr -s 1920x1200 &
# set wallpaper
./.fehbg &
# picom compositor
picom &
