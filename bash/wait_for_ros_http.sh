ROS_MASTER_URI="http://0.0.0.0:11311"

waitForRos() {
    # Expecting a 501 http code from roscore
    until wget -S $ROS_MASTER_URI -t 1 2>&1 | grep "ERROR 501" ; do
        echo "waiting for ROS at $ROS_MASTER_URI"
        sleep 1;
    done
    echo "Caught expected error! Found ROS at $ROS_MASTER_URI"
    sleep 1;
}
