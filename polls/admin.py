from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['question_text']}),
    ('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  list_display = ('question_text', 'published_date', 'was_published_recently')
  list_filter = ['published_date']
  search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('choice_text', 'question')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
