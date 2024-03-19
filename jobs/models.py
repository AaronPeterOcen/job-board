from django.db import models
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    """class to handle the job app function"""
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now_add=True)

    job_title = models.CharField(max_length=100, unique=True)
    job_listing_url = models.URLField(unique=True)
    job_location = models.CharField(max_length=100, blank=True, null=True)
    job_salary = models.IntegerField(blank=True, null=True)

    company = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.company} {self.job_title}"
class Company(models.Model):
    """handles the company details"""
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now_add=True)

    company_name = models.CharField(max_length=100, unique=True)
    company_url = models.URLField(unique=True)
    company_logo = models.ImageField(
        upload_to="company_logo/"
    )
    company_email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.company_name}"
