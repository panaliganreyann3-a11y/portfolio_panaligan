from django.contrib import admin
from .models import Profile, Skill, Project, Education, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display        = ('name', 'level', 'order')
    list_editable       = ('level', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'tools_used', 'order')
    list_editable = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ('school', 'degree', 'year_attended', 'order')
    list_editable = ('order',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'github', 'linkedin')
