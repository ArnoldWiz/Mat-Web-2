from django.contrib import admin
from .models import Choice, Question

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
# Register your models here.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)