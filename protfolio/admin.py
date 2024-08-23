from django.contrib import admin
from .models import Project, WorkExperience, Education, Certification

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'image', 'link')
    search_fields = ('title', 'description')
    list_filter = ('user',)

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'user')
    search_fields = ('job_title', 'company', 'description')
    list_filter = ('user',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'user')
    search_fields = ('degree', 'institution')
    list_filter = ('user',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issued_by', 'issue_date', 'user')
    search_fields = ('name', 'issued_by')
    list_filter = ('user',)

