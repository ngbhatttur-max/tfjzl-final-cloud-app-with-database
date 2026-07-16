from django.contrib import admin
# Import all models including new ones
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Lesson inline for Course
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Choice inline for Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# Question inline for Course (optional if you want nested editing)
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Course admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

# Lesson admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
