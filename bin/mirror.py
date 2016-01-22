#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This file is part of B{Domogik} project (U{http://www.domogik.org}).

License
=======

B{Domogik} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

B{Domogik} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Domogik. If not, see U{http://www.gnu.org/licenses}.

Plugin purpose
==============

mir:ror by Violet support

Implements
==========

- MirrorManager

@author: Fritz <fritz.smh@gmail.com>
@copyright: (C) 2007-2012 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

from domogik.xpl.common.xplmessage import XplMessage
from domogik.xpl.common.plugin import XplPlugin
from domogik_packages.plugin_mirror.lib.mirror import Mirror
from domogik_packages.plugin_mirror.lib.mirror import MirrorException
import threading


class MirrorManager(XplPlugin):
    """ Manage the Mir:ror device and connect it to xPL
    """

    def __init__(self):
        """ Init plugin
        """
        XplPlugin.__init__(self, name='mirror')

        ### get the devices list
        # for this plugin, if no devices are created we won't be able to use devices.
        # but.... if we stop the plugin right now, we won't be able to detect existing device and send events about them
        # so we don't stop the plugin if no devices are created
        self.devices = self.get_device_list(quit_if_no_device=False)

        # check if the plugin is configured. If not, this will stop the plugin and log an error
        if not self.check_configured():
            return

#        self._config = Query(self.myxpl, self.log)
        mirror_device = str(self.get_config('device'))

        # Init Mir:ror
        mirror  = Mirror(self.log, self.send_xpl)

        # Open Mir:ror
        try:
            mirror.open(mirror_device)
        except MirrorException as e:
            self.log.error(e.value)
            print(e.value)
            self.force_leave()
            return

        # Start reading Mir:ror
        mirror_process = threading.Thread(None,
                                   mirror.listen,
                                   "mirror-process-reader",
                                   (self.get_stop(),),
                                   {})
        self.register_thread(mirror_process)
        mirror_process.start()
        self.ready()


    def send_xpl(self, device, type, current):
        """ Send xPL message on network
        """
        print("device:%s, type:%s, current:%s" % (device, type, current))
        msg = XplMessage()
        msg.set_type("xpl-trig")
        msg.set_schema("sensor.basic")
        msg.add_data({"device" : device})
        msg.add_data({"type" : type})
        msg.add_data({"current" : current})
        self.myxpl.send(msg)
	print(msg)

if __name__ == "__main__":
    MirrorManager()
