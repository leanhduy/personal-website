from django.contrib import admin
from .models import Profile, Project, Tag, Skill, Award, Experience, Education


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["name", "username", "email"]


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["name", "project_owner", "project_type"]


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ["name"]


class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = ["school_name", "gpa"]


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = ["name", "organization", "position"]


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ["name", "skill_owner"]


class AwardAdmin(admin.ModelAdmin):
    model = Award
    list_display = ["name", "owner", "award_type"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Award, AwardAdmin)
