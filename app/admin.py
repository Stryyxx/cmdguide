from django.contrib import admin
from .models import Quiz, Question, Choice, Attempt, Answer

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Attempt)
admin.site.register(Answer)
