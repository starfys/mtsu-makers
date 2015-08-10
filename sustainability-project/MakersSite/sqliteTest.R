#clean the environment for memory sake
rm(list=ls())
#if not installed, install.packages("quantmod")
#library("quantmod")
#library("RSQLite") #you'd think this would be the one
library("dplyr")

# This is just a test case
setwd("/Users/stephenkinser/mtsu-makers/sustainability-project/MakersSite")
my_db<- src_sqlite("db.sqlite3", create= F)
tempHumidity<- tbl(my_db, "tempHumidity_temphumidity")

