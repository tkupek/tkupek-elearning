from django.contrib import admin

from tkupek_elearning.elearning.models import Option, Setting, Question, UserAnswer, User


class OptionInline(admin.TabularInline):
    model = Option


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionInline,
    ]


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserAnswerInline,
    ]

    def get_readonly_fields(self, request, obj=None):

        return self.readonly_fields + ('token', 'last_seen')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Setting),
admin.site.register(User, UserAdmin)
