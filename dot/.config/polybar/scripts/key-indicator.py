#!/usr/bin/env python3
# ~/.config/polybar/scripts/key-indicator.py
import time
import subprocess
from pynput import keyboard

# Key state tracking
shift_pressed = False
ctrl_pressed = False
alt_pressed = False
super_pressed = False
tab_pressed = False

def on_press(key):
    global shift_pressed, ctrl_pressed, alt_pressed, super_pressed, tab_pressed
    
    if key in [keyboard.Key.shift_l, keyboard.Key.shift_r]:
        shift_pressed = True
        print_status()
    elif key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        ctrl_pressed = True
        print_status()
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        alt_pressed = True
        print_status()
    elif key in [keyboard.Key.cmd, keyboard.Key.cmd_l, keyboard.Key.cmd_r]:  # Super/Windows key
        super_pressed = True
        print_status()
    elif key == keyboard.Key.tab:
        tab_pressed = True
        print_status()

def on_release(key):
    global shift_pressed, ctrl_pressed, alt_pressed, super_pressed, tab_pressed
    
    if key in [keyboard.Key.shift_l, keyboard.Key.shift_r]:
        shift_pressed = False
        print_status()
    elif key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        ctrl_pressed = False
        print_status()
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        alt_pressed = False
        print_status()
    elif key in [keyboard.Key.cmd, keyboard.Key.cmd_l, keyboard.Key.cmd_r]:  # Super/Windows key
        super_pressed = False
        print_status()
    elif key == keyboard.Key.tab:
        tab_pressed = False
        print_status()

def print_status():
    output = ""
    
    # Tab indicator
    if tab_pressed:
        output += "%{B#b48ead}%{F#000000} 󰌒 %{F-}%{B-}"
    # Shift indicator
    elif shift_pressed:
        output += "%{B#d08770}%{F#000000} 󰜷 %{F-}%{B-}"
    # Ctrl indicator
    elif ctrl_pressed:
        output += "%{B#5e81ac}%{F#000000} 󰘴 %{F-}%{B-}"
    # Alt indicator 
    elif alt_pressed:
        output += "%{B#a3be8c}%{F#000000} 󰘵 %{F-}%{B-}"
    # Super indicator 
    elif super_pressed:
        output += "%{B#bf616a}%{F#000000} 󰘳 %{F-}%{B-}"
    else:
        output += "%{F#666666}  %{F-}"
    
    print(output, flush=True)

# Initial state
print_status()

# Start listener
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Script terminated by user")
except Exception as e:
    print(f"Error: {e}")
