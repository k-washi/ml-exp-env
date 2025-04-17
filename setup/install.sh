#!/bin/bash

wget https://developer.download.nvidia.com/compute/cusparselt/0.7.1/local_installers/cusparselt-local-repo-ubuntu2404-0.7.1_1.0-1_amd64.deb
sudo dpkg -i cusparselt-local-repo-ubuntu2404-0.7.1_1.0-1_amd64.deb
sudo cp /var/cusparselt-local-repo-ubuntu2404-0.7.1/cusparselt-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install libcusparselt0 libcusparselt-dev
