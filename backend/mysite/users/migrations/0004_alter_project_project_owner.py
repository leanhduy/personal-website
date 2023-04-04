# Generated by Django 4.1.7 on 2023-04-04 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_project_project_type_achievement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="project_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="users.profile",
            ),
        ),
    ]
