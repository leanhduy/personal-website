from django.contrib import admin
from .models import Project, Profile, Skill, Tag, Achievement


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["name", "project_owner", "project_type"]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["name", "username", "email"]


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ["name", "skill_owner"]


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ["name"]


class AchievementAdmin(admin.ModelAdmin):
    model = Achievement
    list_display = ["name", "achievement_owner", "achievement_type"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Achievement, AchievementAdmin)
