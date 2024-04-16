RTSP_SERVER_HOST=0.0.0.0
RTSP_SERVER_PORT=8554  ## TCP port

waitForRtsp() {
    # Expecting a connection stablished to a fake http rtsp uri
    until wget -S "http://$RTSP_SERVER_HOST:$RTSP_SERVER_PORT" -t 1 2>&1 | grep "connected" ; do
        echo "waiting for RTSP server at $RTSP_SERVER_URI"
        sleep 1;
    done
    echo "Caught expected error! Found RTSP at $RTSP_SERVER_HOST:$RTSP_SERVER_PORT"
    sleep 1;
}

