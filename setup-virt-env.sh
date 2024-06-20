#!/bin/sh
#Generic way to setup a virtualenv if required in current directory
#better to have virtualenv per project/application
#to use: source setup-virt-env.sh
if command -v deactivate &> /dev/null; then
    echo "Virtualenv will be deactivated."
    deactivate
else
    echo "Virtualenv is not activated, continue."
fi
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
echo "env installed"