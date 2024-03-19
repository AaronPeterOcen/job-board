# from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse

from .models import Job

import datetime

# Create your views here.
start_date = datetime.date.today()

class JobListView():
    model = Job
    template_name = "all_jobs.html"
    queryset = Job.objects.filter(created_datetime__gte=datetime.date(2022, 1, 1))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsletter_form"] = NewsletterSignupForm
        return context
    