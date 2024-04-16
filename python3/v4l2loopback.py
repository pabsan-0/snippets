import v4l2ctl

def find_v4l2loopback():
    DEV_RANGE = 6

    # Scan for possible loopback devices
    for ii in range(DEV_RANGE):
        device = v4l2ctl.V4l2Device(ii)
        if "v4l2loopback" in device.bus:
            dev_fd = "/dev/video%s" % ii
            print("Found loopback device at %s" % dev_fd)
            return dev_fd

    # If not found
    raise Exception("No loopback device found in range %d" % DEV_RANGE)
