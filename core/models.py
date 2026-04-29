from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/', blank=True)
    cv_file = models.FileField(upload_to='cv/', blank=True)
    email = models.EmailField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
    instagram_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Database', 'Database'),
        ('Visualization', 'Visualization'),
        ('Statistics', 'Statistics'),
        ('Tools', 'Tools'),
        ('Soft Skills', 'Soft Skills'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    icon_emoji = models.CharField(max_length=10, blank=True)
    skill_image = models.ImageField(upload_to='skills/', blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    tools_used = models.CharField(max_length=500)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    date = models.DateField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

    def duration(self):
        end = timezone.now().date() if self.is_present else self.end_date
        if not end:
            return ''
        months = (end.year - self.start_date.year) * 12 + (end.month - self.start_date.month)
        years, rem = divmod(months, 12)
        parts = []
        if years:
            parts.append(f"{years} yr{'s' if years > 1 else ''}")
        if rem:
            parts.append(f"{rem} mo{'s' if rem > 1 else ''}")
        return ' '.join(parts) if parts else 'Less than a month'


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='certificates/', blank=True)
    date_issued = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-date_issued']

    def __str__(self):
        return self.name
