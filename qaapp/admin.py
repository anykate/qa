from django.contrib import admin
from .models import Question, Answer, QuestionVote


# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionVote)
