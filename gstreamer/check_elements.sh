#!/usr/bin/env bash

while read -r el; do
    [ -z "$el" ] && continue
    if gst-inspect-1.0 "$el" >/dev/null 2>&1; then
        printf 'ok      %s\n' "$el"
    else
        printf 'miss    %s\n' "$el"
    fi
done <<'EOF'

avdec_h264
h264parse
openh264dec
openh264enc
x264enc

avdec_h265
h265parse
openh265dec
openh265enc
x265enc

EOF
