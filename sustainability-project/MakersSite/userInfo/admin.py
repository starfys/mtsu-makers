from django.contrib import admin
from .models import UserName
#tempHumidity

class UserNameInline(admin.StackedInline):
	model = UserName
	extra = 3

class UserNameAdmin(admin.ModelAdmin):
	fieldsets = [
		('First Name', {'fields' : ['first_name']}),
		('Last Name', {'fields' : ['last_name']}),
		('gihub' ,{'fields' : ['github']}),
		('Date Registered' , {'fields' : ['join_date']})
	]
	inlines = [UserNameInline]
	

#class tempHumidityAdmin(admin.ModelAdmin):
#	fields = ['pi_num','temperature','humidity','date_rec']

admin.site.register(UserName)
#admin.site.register(tempHumidity)
# Register your models here.
