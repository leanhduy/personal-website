from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("api/v1/admin", views.get_admin, name="get-admin-profile"),
    path("api/v1/projects", views.get_projects, name="get-all-projects"),
    path("api/v1/tags", views.get_tags, name="get-all-tags"),
    path("api/v1/tags/<uuid:id>", views.get_tag_by_id, name="get-tag-by-id"),
    path("api/v1/skills", views.get_skills, name="get-all-skills"),
    path("api/v1/experiences", views.get_experiences, name="get-experiences"),
    path("api/v1/educations", views.get_educations, name="get-educations"),
    path("api/v1/awards", views.get_awards, name="get-awards"),
]
