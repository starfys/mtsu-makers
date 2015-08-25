from django.db import models
#from userInfo.models import Human
#from django.userInfo.models import Human
from partList.models import part
#from multivalue import separateValues
# http://stackoverflow.com/questions/1110153/what-is-the-most-efficent-way-to-store-a-list-in-the-django-models

#class Human(models.Model):
#  name = models.TextField(default="")
#  def __unicode__(self):
#    return self.name


#should I reuse Human code and switch it to a generic name?
#class Parts(models.Model):
#  name = models.TextField(default="")
#  def __unicode__(self):
#    return self.name

class project(models.Model):
  projectName= models.CharField(max_length=64)
  #colaborators = models.ManyToManyField(Human, blank= True, related_name="Colab")
# partsList= models.ManyToManyField(part, blank= True, related_name="Part_List")
  start_date = models.DateTimeField('Start Date')
  finish_date= models.DateTimeField('Finish Date')



#don't use this
#proj1 = project(projectName= "Pi Cluster", colaborators=["Stephen Kinser", "Steven Sheffey"], partsList= ["Raspberry Pi", "Wires", "3d Printed Case"], pub_date= timezone.now())
#use this
#contr1= Human(name="Stephen Kinser")
#contr1.save()
#contr2= Human(name="Steven Sheffey")
#contr2.save()
#part1= Parts(name="Raspberry Pi")
#part1.save()
#part2= Parts(name="Wires")
#part2.save()
#part3= Parts(name="3D Printed Case")
#part3.save()
#proj= project(projectName = "Pi Cluster", pub_date= timezone.now())
#proj.save()
#proj.colaborators.add(contr1, contr2)
#proj.publications.add(part1,part2,part3)
#proj.save()
