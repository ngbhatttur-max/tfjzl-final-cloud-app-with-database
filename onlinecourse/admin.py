from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Inline for Choice model (to add choices directly when editing a Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # number of empty choice fields shown by default

# Inline for Question model (to add questions directly when editing a Lesson)
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # number of empty question fields shown by default

# Custom admin for Question with Choice inline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Custom admin for Lesson with Question inline
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register all models with admin site
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
