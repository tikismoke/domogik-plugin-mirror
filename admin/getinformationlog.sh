#!/bin/bash

ERROR=$(egrep 'Unknow device with address' /var/log/domogik/plugin_mirror.log |sort -rnk1,2 | head -10)
if [ -z "$ERROR" ]
then
	echo "No unknow Ztamp or Mirror."
else
	echo "$ERROR"
fi
