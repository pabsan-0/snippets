#! /usr/bin/env bash
#
# Run from either the host or the docker image

if [ -f /.dockerenv ]; then
    bash -s
else
    docker compose run --rm --entrypoint bash CONTAINER -s
fi << 'EOF'

set -x
gst-inspect-1.0 mpegh3daenc
gst-inspect-1.0 mpegh3dadec
gst-inspect-1.0 mpegh3daparse
gst-inspect-1.0 audiomediaauthsigner
gst-inspect-1.0 audiomediaauthverifier
gst-inspect-1.0 dscsigner
gst-inspect-1.0 dscverifier

EOF
