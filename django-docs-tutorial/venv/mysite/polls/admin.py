from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  # or admin.StackedInline
  # embed Choices within Questions instead of separately
    model = Choice
    extra = 3  # 3 slots by default


class QuestionAdmin(admin.ModelAdmin):
    # customize fields for creating new questions
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    # embed Choices within Questions instead of separately
    inlines = [ChoiceInline]

    # customize template for index page
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # adds filtering
    list_filter = ['pub_date']

    # adds search box
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
