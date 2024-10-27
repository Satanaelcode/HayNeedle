#!/bin/bash

# Check if the file exists, if not create it
if [ ! -f ./urls.log ]; then
    touch ./urls.log
    echo "File 'urls.log' created."
fi

# Start logging
echo "START LOGGING"
tail -f ./urls.log
