#!/bin/bash

#make sure it is up to date
sudo apt-get --upgrade
#for python libraries
sudo apt-get -y install python
sudo apt-get -y install pip
sudo apt-get -y install python-dev libxml2-dev libxslt-dev
sudo pip install django-adaptors
sudo pip install django
sudo pip install requests
sudo pip install csv
sudo pip install lxml
sudo pip install numpy

#for c++ libraries
sudo apt-get -y install gcc

#for R
sudo apt-get -y install r-base r-base-dev
mkdir ~/R ~/R/library 
echo 'R_LIBS_USER="~/R/library"' >  $HOME/.Renviron 
sudo cat<<EOF | Rscript -
install.packages(c("ggplot2","dplyr","reshape","grid","quantreg"),repos="http://cran.rstudio.com/")
EOF