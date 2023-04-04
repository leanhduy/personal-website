# Generated by Django 4.1.7 on 2023-04-03 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name="skill",
            old_name="profile",
            new_name="skill_owner",
        ),
        migrations.AddField(
            model_name="skill",
            name="description",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="facebook_profile",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="github_profile",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="linkedin_profile",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="website_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "featured_image",
                    models.ImageField(blank=True, null=True, upload_to=""),
                ),
                ("source_url", models.URLField(blank=True, null=True)),
                (
                    "project_type",
                    models.CharField(
                        choices=[(1, "Personal"), (2, "Commercial")], max_length=20
                    ),
                ),
                (
                    "project_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="projects", to="users.tag"
                    ),
                ),
            ],
        ),
    ]