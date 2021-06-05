# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group
from django.forms import TextInput
from django.db import models
from import_export.admin import ImportExportModelAdmin

from .models import *
from .forms import Adaptingtextarea

admin.site.site_header = "QLever UI Administration"
admin.site.site_title = "QLever UI Administration"


class BackendAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '140'})},
        models.TextField: {'widget': Adaptingtextarea()},
    }
    fieldsets = (
        ("General", {
            'fields': ('name', 'slug', 'sortKey', 'baseUrl', 'isDefault')
        }),
        ('UI Suggestions', {
            'fields': ('maxDefault', 'fillPrefixes', 'filterEntities', 'filteredLanguage', 'supportedKeywords', 'supportedFunctions', 'suggestPrefixnamesForPredicates', 'supportedPredicateSuggestions', 'suggestedPrefixes'),
        }),
        ('Backend Suggestions', {
            'fields': ('suggestionEntityVariable', 'suggestionNameVariable', 'suggestionAltNameVariable', 'suggestionReversedVariable', 'suggestSubjects', 'suggestPredicates', 'suggestObjects', 'dynamicSuggestions', 'replacePredicates'),
        }),
        ('Showing names', {
            'fields': ('subjectName', 'alternativeSubjectName', 'predicateName', 'alternativePredicateName', 'objectName', 'alternativeObjectName'),
        }),
    )


class ExampleAdmin(ImportExportModelAdmin):
    list_display = ['backend', 'name']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'content']


admin.site.unregister(Group)

admin.site.register(Backend, BackendAdmin)
admin.site.register(Example, ExampleAdmin)
#admin.site.register(Link, LinkAdmin)
