from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

