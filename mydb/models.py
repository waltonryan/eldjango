from django.db import models
from django.forms import ModelForm

# Create your models here.

class Mysiteuser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    comments = models.CharField(max_length=1024)
    signup_date = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class MysiteuserForm(ModelForm):
	class Meta:
		model = Mysiteuser
