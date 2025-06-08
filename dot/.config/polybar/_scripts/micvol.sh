#!/bin/bash

get_mic_status() {
    # Get default source (microphone)
    local source=$(pactl get-default-source)
    local muted=$(pactl get-source-mute "$source" | grep -o "yes\|no")
    
    if [ "$muted" = "yes" ]; then
        echo " 󰍭 "  # or "MIC OFF" or whatever indicator you prefer
    else
        echo "%{B#e60000} 󰍬 %{B-}"  # or "MIC ON"
    fi
}

# Initial status
get_mic_status

# Listen for PulseAudio events
pactl subscribe | while read -r event; do
    if echo "$event" | grep -q "source"; then
        get_mic_status
    fi
done
