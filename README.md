This is for the MTSU MAKERS sustainability project.

######### To login to web server ###########
Ask MTSU Makers for login credentials to our web server
######## For Raspberry Pi #######
coder login: pi
coder password: raspberry 

####### For information on sqlserver ######
for use in html, go over the Django templates
for use in R use the dplyr library, I will have a running R script soon

to add do python manage.py makemigrations <appname>
python manage.py sqlmigrate <appname> <four digit number of mostr recentupdate>
python manage.py migrate

check permissions if getting unusual errors:
change it to: sudo chown <yourname> <filename>
might have to do something to change that up
if still getting errors try doing chmod 776, just omething to enable write permissions

####### For running / booting up server #######
python manage.py runserver stevensheffey.me:9000 

####### For problems on runnning python manage.py #####
if you get
Traceback (most recent call last):
  File "manage.py", line 10, in <module>
      execute_from_command_line(sys.argv)
        File "/usr/lib/python2.7/dist-packages/django/core/management/__init__.py", line 385, in execute_from_command_line
	    utility.execute()
	      File "/usr/lib/python2.7/dist-packages/django/core/management/__init__.py", line 354, in execute
	          django.setup()
		    File "/usr/lib/python2.7/dist-packages/django/__init__.py", line 21, in setup
		        apps.populate(settings.INSTALLED_APPS)
			  File "/usr/lib/python2.7/dist-packages/django/apps/registry.py", line 108, in populate
			      app_config.import_models(all_models)
			        File "/usr/lib/python2.7/dist-packages/django/apps/config.py", line 202, in import_models
				    self.models_module = import_module(models_module_name)
				      File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
				          __import__(name)
					    File "/home/stephenk/mtsu-makers/sustainability-project/MakersSite/ongoingProjects/models.py", line 4, in <module>
					        from partList.models import part
						  File "/home/stephenk/mtsu-makers/sustainability-project/MakersSite/partList/models.py", line 4, in <module>
						      from adaptor.model import CsvDbModel

you will need to use :
################################
sudo pip install django-adaptors
################################
you will then probably get this error:
Traceback (most recent call last):
  File "manage.py", line 10, in <module>
      execute_from_command_line(sys.argv)
        File "/usr/lib/python2.7/dist-packages/django/core/management/__init__.py", line 385, in execute_from_command_line
	    utility.execute()
	      File "/usr/lib/python2.7/dist-packages/django/core/management/__init__.py", line 354, in execute
	          django.setup()
		    File "/usr/lib/python2.7/dist-packages/django/__init__.py", line 21, in setup
		        apps.populate(settings.INSTALLED_APPS)
			  File "/usr/lib/python2.7/dist-packages/django/apps/registry.py", line 108, in populate
			      app_config.import_models(all_models)
			        File "/usr/lib/python2.7/dist-packages/django/apps/config.py", line 202, in import_models
				    self.models_module = import_module(models_module_name)
				      File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
				          __import__(name)
					    File "/home/stephenk/mtsu-makers/sustainability-project/MakersSite/ongoingProjects/models.py", line 4, in <module>
					        from partList.models import part
						  File "/home/stephenk/mtsu-makers/sustainability-project/MakersSite/partList/models.py", line 4, in <module>
						      from adaptor.model import CsvDbModel
						        File "/usr/local/lib/python2.7/dist-packages/adaptor/model.py", line 8, in <module>
							    from adaptor.fields import Field, IgnoredField, ComposedKeyField, XMLRootField
							      File "/usr/local/lib/python2.7/dist-packages/adaptor/fields.py", line 3, in <module>
							          from lxml import etree
								  ImportError: No module named lxml
which probably will mean you will have to do:
######################
sudo pip install lxml
#####################
if you get this error:

 #include "pyconfig.h"

                      ^

compilation terminated.

error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

----------------------------------------
Cleaning up...
Command /usr/bin/python -c "import setuptools, tokenize;__file__='/tmp/pip-build-wZw7Ib/lxml/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-ELnhUk-record/install-record.txt --single-version-externally-managed --compile failed with error code 1 in /tmp/pip-build-wZw7Ib/lxml
Storing debug log for failure in /root/.pip/pip.log

then either do:
######################################################
sudo apt-get install python-dev libxml2-dev libxslt-dev
######################################################
or just:
################################
sudo apt-get install python-dev
################################
then retry:
#######################
sudo pip install lxml
######################



