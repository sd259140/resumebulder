from django.contrib import admin
from resumeapp.models import Resume
@admin.register(Resume)
class Resumeadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']
# Register your models here.
