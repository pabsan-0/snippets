# Heartbeat: beats as long as files are being updated in a dir
HEARTBEAT_URL=""
DIRECTORY=""
if [[ -n "$HEARTBEAT_URL" ]]; then
    START_TIME="$(date "+%F %R")"
    while sleep 3600; do
        [[ -n $(find "$DIRECTORY" -type f -mmin -10 -print -quit 2>/dev/null) ]] || break
        curl -s -X POST -H 'Content-type: application/json' \
            -d "{\"text\":\"isid-nvr @ $HOSTNAME | $START_TIME | Heartbeat for $DIRECTORY\"}" \
            "$HEARTBEAT_URL"
    done &
fi
