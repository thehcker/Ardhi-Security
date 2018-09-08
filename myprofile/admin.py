from django.contrib import admin
from . models import titledeed

# Register your models here.
from .models import myprofile
class profilesAdmin(admin.ModelAdmin):
	class Meta:
		model = myprofile
	
admin.site.register(myprofile)
admin.site.register(titledeed)
