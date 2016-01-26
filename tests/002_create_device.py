#!/usr/bin/python
#-*- coding: utf-8 -*-create_device.py

### configuration ######################################
DEVICE_NAME_MIRROR = "test_mirror"
ADDRESS = "mirror"


from domogik.tests.common.testdevice import TestDevice
from domogik.common.utils import get_sanitized_hostname

plugin = 'mirror'

def create_device():
    ### create the device, and if ok, get its id in device_id
    client_id  = "plugin-{0}.{1}".format(plugin, get_sanitized_hostname())
    print "Creating the Mirror device..."
    td = TestDevice()
    params = td.get_params(client_id, "mirror")
        # fill in the params
    params["device_type"] = "mirror"
    params["name"] = DEVICE_NAME_MIRROR
    params["address"] = ADDRESS
    for idx, val in enumerate(params['global']):
        if params['global'][idx]['key'] == 'name' :  params['global'][idx]['value'] = NAME
        if params['global'][idx]['key'] == 'address' :  params['global'][idx]['value'] = ADDRESS
    for idx, val in enumerate(params['xpl']):
        params['xpl'][idx]['value'] = TO

    # go and create
    td.create_device(params)
    print "Device Mirror {0} configured".format(DEVICE_NAME_KAROTZ)

    
if __name__ == "__main__":
    create_device()



