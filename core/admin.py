from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Certificate


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'icon_emoji']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'featured']
    list_filter = ['featured']
    search_fields = ['title', 'tools_used']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_present']
    list_filter = ['is_present']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'date_issued']
    search_fields = ['name', 'issuer']
