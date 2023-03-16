#!/bin/bash
if ! command -v unoconv &> /dev/null
then
    if [ "$(uname -s)" == "Linux" ]
    then
    if [ -x "$(command -v yum)" ]
    then
        echo "Redhat based system, using yum to install package"
        sudo yum -y install unoconv
    elif [ -x "$(command -v apt-get)" ]
    then
        echo "Debian based system, using apt-get to install package"
        sudo apt-get update
        sudo apt-get install unoconv
    else
        echo "Unknown package manager, exiting..."
        exit 1
    fi
    else
    echo "Not a Linux system, exiting..."
    exit 1
    fi
fi
