from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
 questions = Question.objects.all()
# Serialize and use the JSON string directly without additional encoding
 questions_json = serializers.serialize('json', questions)
 return render(request, 'eduprod/index.html', {'questions_json': questions_json})