#clean the environment for memory sake
rm(list=ls())
#if not installed, install.packages("quantmod")
#library("quantmod")
#library("RSQLite") #you'd think this would be the one
#library("RMySQL")
library("dplyr")
library("ggplot2")
# This is just a test case
#4+4VoMZmmDQ=
#tempHumidity(pi_num=2, temperature=27.0, humidity=0, date_rec =datetime.datetime.fromtimestamp(float(time.time()))).save() 
#requests.post( "http://stevensheffey.me:9000/tempHumidity/submit", data={ 'pi_num':pi_id, 'temperature':temperature, 'humidity': humidity, 'date_rec':time.ctime()) } )
#c8115121@ranger.cs.mtsu.edu:/nfshome/zdong/public_html/4160/gitRepository/class
#setwd("/Users/stephenkinser/mtsu-makers/sustainability-project/MakersSite")
my_db<- src_sqlite("db.sqlite3", create= F)
tempHumidity<- tbl(my_db, "tempHumidity_temphumidity")
localtemp=tempHumidity%>%
  select( temperature, humidity, date_rec)%>%
  filter(date_rec >= Date("2015-08-24 20:00:23.220000"))%>%
  collect()
  
ggplot(aes(y=temperature, x=as.Date(date_rec)),data = localtemp)+geom_point()
ggplot(aes(y=humidity, x=as.Date(date_rec)),data = localtemp)+geom_point()
localtemp$time=strftime(localtemp$date_rec, format="%H:%M:%S") 
localtemp$date_rec=as.Date(localtemp$date_rec)
ggplot(aes(y=humidity, x=time),data = localtemp)+geom_point()+facet_wrap(~date_rec)
ggsave("humidity.png")
ggplot(aes(y=temperature, x=time),data = localtemp)+geom_point()+facet_wrap(~date_rec)
ggsave("temperature.png")
