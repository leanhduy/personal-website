from django.db import models
from django.contrib.auth.models import User
from .consts import PROJECT_TYPES, ACHIEVEMENT_TYPES


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    github_profile = models.URLField(max_length=200, blank=True, null=True)
    facebook_profile = models.URLField(max_length=200, blank=True, null=True)
    linkedin_profile = models.URLField(max_length=200, blank=True, null=True)
    website_url = models.URLField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    featured_image = models.ImageField(blank=True, null=True)
    source_url = models.URLField(max_length=200, blank=True, null=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    tags = models.ManyToManyField("Tag", blank=True, related_name="projects")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    achievement_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPES)
    source_url = models.URLField(max_length=200, blank=True, null=True)
