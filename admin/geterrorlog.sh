#!/bin/bash

ERROR=$(egrep 'WARNING|ERROR' /var/log/domogik/plugin_mirror.log |sort -rnk1,2 | head -10)
if [ -z "$ERROR" ]
then
	echo "No error."
else
	echo "$ERROR"
fi
