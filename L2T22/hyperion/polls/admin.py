from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.StackedInline):
    model = Choice
    No_of_choice = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None, {'fields': ['question_text']}),
        ('Date information',{'field':['pub_date']}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)