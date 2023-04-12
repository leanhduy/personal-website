import os
from dotenv import load_dotenv
from django.urls import path
from . import views

load_dotenv()

BASE_API_URL = os.getenv("API_BASE_URL")

urlpatterns = [
    path(f"{BASE_API_URL}/admin", views.get_admin, name="get-admin-profile"),
    path(
        f"{BASE_API_URL}/projects",
        views.get_projects,
        name="get-all-projects",
    ),
    path(f"{BASE_API_URL}/tags", views.get_tags, name="get-all-tags"),
    path(
        f"{BASE_API_URL}/tags/<int:id>",
        views.get_tag_by_id,
        name="get-tag-by-id",
    ),
    path(f"{BASE_API_URL}/skills", views.get_skills, name="get-all-skills"),
    path(
        f"{BASE_API_URL}/experiences",
        views.get_experiences,
        name="get-experiences",
    ),
    path(
        f"{BASE_API_URL}/educations",
        views.get_educations,
        name="get-educations",
    ),
    path(f"{BASE_API_URL}/awards", views.get_awards, name="get-awards"),
]
