from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Project, Tag, Skill, Education, Experience, Award, Profile
from .serializer.serializers import (
    ProjectSerializer,
    TagSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    AwardSerializer,
    ProfileSerializer,
)

# Create your views here.


def index(request):
    """A view to return the index page"""
    profile = Profile.objects.first()
    return render(request, "users/index.html", {"profile": profile})


# * APIs
# ? Profile APIs (Since there is only one profile, we don't need to get profile by id)
@api_view(["GET"])
def get_admin(request):
    profile = Profile.objects.first()
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


# ? Project APIs
@api_view(["GET"])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# ? Tag APIs
@api_view(["GET"])
def get_tags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_tag_by_id(request, id):
    tag = Tag.objects.get(id=id)
    serializer = TagSerializer(tag, many=False)
    return Response(serializer.data)


# ? Skill APIs
@api_view(["GET"])
def get_skills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


# ? Experience APIs
@api_view(["GET"])
def get_experiences(request):
    experiences = Experience.objects.all()
    serializer = ExperienceSerializer(experiences, many=True)
    return Response(serializer.data)


# ? Education APIs
@api_view(["GET"])
def get_educations(request):
    educations = Education.objects.all()
    serializer = EducationSerializer(educations, many=True)
    return Response(serializer.data)


# ? Award APIs
@api_view(["GET"])
def get_awards(request):
    awards = Award.objects.all()
    serializer = AwardSerializer(awards, many=True)
    return Response(serializer.data)
