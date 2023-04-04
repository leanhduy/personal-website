from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("projects/<int:id>", views.single_project, name="single-project"),
    path("projects/personal", views.personal_projects, name="personal-projects"),
    path("projects/commercial", views.commercial_projects, name="commercial-projects"),
    path("contact/", views.contact_me, name="contact-me"),
    # path("about/", views.index, name="about-me"),
]
