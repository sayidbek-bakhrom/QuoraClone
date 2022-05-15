from django.contrib import admin
from .models import Question, Response, Profile


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
admin.site.register(Profile)
