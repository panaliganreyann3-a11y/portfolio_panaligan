from django.db import models


class Profile(models.Model):
    name         = models.CharField(max_length=100)
    tagline      = models.CharField(max_length=200)
    photo        = models.ImageField(upload_to='images/', blank=True, null=True)
    background   = models.TextField(help_text="Short personal background")
    career_goals = models.TextField(help_text="Career interests or goals")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Profile"
        verbose_name_plural = "Profile"


class Skill(models.Model):
    name  = models.CharField(max_length=100)
    icon  = models.CharField(max_length=100, blank=True,
                              help_text="Font Awesome class e.g. fab fa-python")
    level = models.PositiveIntegerField(default=80,
                                         help_text="Skill level 0–100")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    tools_used  = models.CharField(max_length=300,
                                    help_text="Space-separated e.g. Django Python MySQL")
    github_link = models.URLField(blank=True, null=True)
    order       = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class Education(models.Model):
    school        = models.CharField(max_length=200)
    degree        = models.CharField(max_length=200)
    year_attended = models.CharField(max_length=50, help_text="e.g. 2020 – 2024")
    order         = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.degree} — {self.school}"

    class Meta:
        ordering            = ['-order']
        verbose_name_plural = "Education"


class Contact(models.Model):
    email    = models.EmailField()
    github   = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name        = "Contact Info"
        verbose_name_plural = "Contact Info"
