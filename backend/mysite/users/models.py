from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from .consts import PROJECT_TYPES, ACHIEVEMENT_TYPES


# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    skill_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500, blank=True, null=True)
    svg_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Award(models.Model):
    ACHIEVEMENT_TYPES = (("award", "Award"), ("certification", "Certification"))
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    date_taken = models.DateField()
    featured_image = models.ImageField(blank=True, null=True)
    award_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPES)
    award_url = models.URLField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=100)
    responsibilities = models.TextField(max_length=500, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.organization}"
