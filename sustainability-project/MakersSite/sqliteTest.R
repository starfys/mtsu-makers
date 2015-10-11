#clean the environment for memory sake
rm(list=ls())
#if not installed, install.packages("quantmod")
#library("quantmod")
#library("RSQLite") #you'd think this would be the one
#library("RMySQL")
library("dplyr")
library("ggplot2")
library("quantreg")
# This is just a test case
#4+4VoMZmmDQ=
#tempHumidity(pi_num=2, temperature=27.0, humidity=0, date_rec =datetime.datetime.fromtimestamp(float(time.time()))).save() 
#requests.post( "http://stevensheffey.me:9000/tempHumidity/submit", data={ 'pi_num':pi_id, 'temperature':temperature, 'humidity': humidity, 'date_rec':time.ctime()) } )
#c8115121@ranger.cs.mtsu.edu:/nfshome/zdong/public_html/4160/gitRepository/class
setwd("/Users/stephenkinser/mtsu-makers/sustainability-project/MakersSite")
my_db<- src_sqlite("db.sqlite3", create= F)
my_db
tempHumidity<- tbl(my_db, "tempHumidity_temphumidity")
localtemp=tempHumidity%>%
  select( temperature, humidity, date_rec)%>%
  filter(date_rec >= Date("2015-08-24 20:00:23.220000"))%>%
  collect()


ggplot(aes(y=temperature, x=as.Date(date_rec)),data = localtemp)+geom_point()
ggplot(aes(y=humidity, x=as.Date(date_rec)),data = localtemp)+geom_point()
localtemp$time=strftime(localtemp$date_rec, format="%H:%M:%S") 
localtemp$appx_time=format(round(strptime(paste("2001-01-01", localtemp$time), format="%Y-%m-%d %H:%M") , units="hours"), format="%H:%M")
localtemp$date_rec=as.Date(localtemp$date_rec)
ggplot(aes(y=humidity, x=time),data = localtemp)+geom_point()+facet_wrap(~date_rec)
ggsave("humidity.png")
ggplot(aes(y=temperature, x=time),data = localtemp)+geom_point()+facet_wrap(~date_rec)
ggsave("temperature.png")

localtemp$temperature=round(localtemp$temperature)
expectedValue<- function(numlist, probslist){
  return(sum(numlist*probslist));
}
expectedVariance<- function(numlist, probslist){
  return( sum(((numlist-expectedValue(numlist, probslist))^2)*probslist));
}

temperaturetotals=table(localtemp$temperature)
problist=temperaturetotals/sum(temperaturetotals)
#summarise(group_by(localtemp, date_rec) , expectedValue(temperature,problist ))
expectedValue(18:25, problist)
expectedVariance(18:25, problist)

groups=group_by(localtemp , date_rec)
#as.data.frame(table(localtemp$temperature))$Var1
#as.numeric(rownames(table(localtemp$temperature)))
full=summarise(groups, mean(temperature),
          expectedValue(as.numeric(rownames(table(temperature))), table(temperature)/sum(table(temperature))),
          expectedVariance(as.numeric(rownames(table(temperature))), table(temperature)/sum(table(temperature))))


groupsother=group_by(sample_n(localtemp,100) , date_rec)
samplesummary=summarise(groupsother, mean(temperature),
          expectedValue(as.numeric(rownames(table(temperature))), table(temperature)/sum(table(temperature))),
          expectedVariance(as.numeric(rownames(table(temperature))), table(temperature)/sum(table(temperature))))


ggplot()+geom_point(data = samplesummary,aes(date_rec, `expectedValue(as.numeric(rownames(tab...`),color="blue")+
          geom_point(data = full,aes(date_rec, `expectedValue(as.numeric(rownames(tab...`),color="red")

ggplot()+geom_quantile(data = localtemp,aes(date_rec, temperature))
ggplot(data = localtemp,aes(appx_time, temperature))+geom_boxplot()+facet_wrap(~date_rec)

