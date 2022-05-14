from django.contrib import admin
from .models import Question, Response


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ('title', )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
