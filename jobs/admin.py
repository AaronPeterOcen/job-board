from django.contrib import admin
from .models import Job, Company

# Register your models here.
class JobInline(admin.TabularInline):
    model = Job

class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        JobInline,
    ]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Job)