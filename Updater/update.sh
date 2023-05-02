#!/bin/bash
# notepad updater

# remove previous version
cd ~
rm -rf .c-notepad

# install new version
git clone https://github.com/FilthyMula/c-notepad


# install dependencies
cd c-notepad
chmod +x install.sh
./install.sh

# self delete
rm -rf ../update.sh
