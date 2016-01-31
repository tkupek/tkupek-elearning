from django.contrib import admin

from tkupek_elearning.elearning.models import Option, Setting, Question


class OptionInline(admin.TabularInline):
    model = Option


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionInline,
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Setting)