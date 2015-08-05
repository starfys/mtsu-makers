from django.db import models
import csv
#from adaptor.model import CsvModel
from adaptor.model import CsvDbModel
# Create your models here.
class part(models.Model):
    name = models.TextField(default="")
    brand = models.TextField(default="")
    cost = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    storage = models.TextField(default="")
    #inProject = models.TextField(default="")
    inProject = models.BooleanField(default="")
    quantity = models.IntegerField(default=0)
    serialNumber = models.TextField(default="")
    #http://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
    #depreciated
    #from partList.models import part
    #other= part()
    #other.csv_read("/Users/stephenkinser/mtsu-makers/sustainability-project/MakersSite/partList/inventory.csv")

    def __unicode__(self):
        #return "Part Name: " + self.name + " Brand: " + self.brand + " Cost: " + str(self.cost) +" Location" + self.storage
        return self.name

#not exactly what I wanted
class mycsvModel(CsvDbModel):
    #from partList.models import part,mycsvModel
    #my_csv_list = mycsvModel.import_data(data = open("/Users/stephenkinser/mtsu-makers/sustainability-project/MakersSite/partList/inventory.csv"))

    class Meta:
        #has header is buggy
        #has_header= True

        dbModel = part
        delimiter = ","
#csv_read("/Users/stephenkinser/mtsu-makers/sustainability-project/MakersSite/partList/inventory.csv")
def csv_read(filename):
        with open(filename) as csvfile:
            inventoryinit = csv.reader(csvfile)
            for row in inventoryinit:
                #print row
                #unclear how get_or_create works
               #  _, created = part.objects.get_or_create(
               #      name=row[0],
               #      brand=row[1],
               #      cost=float(row[2]),
               #      storage=row[3],
               #      inProject= True if row[4] == "TRUE" else False,
               #      quantity=int(row[5]),
               #      serialNumber=row[6]
               # )
                created = part()
                created.name=row[0]
                created.brand=row[1]
                created.cost=float(row[2])
                created.storage=row[3]
                created.inProject=True if row[4] == "TRUE" else False
                created.quantity=int(row[5])
                created.serialNumber=row[6]
                created.save()

