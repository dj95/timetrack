#!/bin/bash
#
# timetrack
#
# (c) 2016 Daniel Jankowski

# create project path
echo "==> Creating installation path"
sudo mkdir -p /opt/Timetrack/.
echo "==> Copy everything to the installation path"
sudo cp -R * /opt/Timetrack/.

# create data directory
echo "==> Create the data directory in ~/Timetrack/"
mkdir -p "~/Timetrack/"
mkdir -p "~/Timetrack/data/"
cp ./src/modules/html/style.css ~/Timetrack/.

# copy the systemd-service
echo "==> Copy the systemd-service"
sudo cp timetrack.service /etc/systemd/system/.

# remove current directory
echo "==> Remove the current directory"
rm -r "../${PWD##*/}"

# move to the installation directory
echo "==> Move to the new installation directory"
mv /opt/Timetrack
