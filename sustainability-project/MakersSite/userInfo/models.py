from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.
#http://www.tangowithdjango.com/book17/chapters/models.html
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
    
class CategoryForm(forms.ModelForm):
        name = forms.CharField(max_length=128, help_text="Please enter the category name.")
        views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        slug = forms.CharField(widget=forms.HiddenInput(), required=False)

        # An inline class to provide additional information on the form.
        class Meta:
            # Provide an association between the ModelForm and a model
            model = Category
            fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
            
#http://www.tangowithdjango.com/book17/chapters/login.html
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    githubURL = models.URLField(blank=True)
#    linkedinURL = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
