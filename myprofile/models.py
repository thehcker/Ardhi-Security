from django.db import models

# Create your models here.
class myprofile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(max_length =120)
	location = models.TextField(max_length = 100, default = 'mylocationdefault')
	job = models.TextField(max_length = 120, blank = True)
	def __unicode__(self):
		return self.name

class titledeed(models.Model):
	owners_name = models.CharField(max_length=30)
	ref_no = models.CharField(max_length =25)
	demographic = models.CharField(max_length = 30)
	size = models.CharField(max_length = 20)

	def __str__(self):
		return self.owners_name