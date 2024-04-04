from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    questions = Question.objects.all()
    # Serialize the queryset into JSON string
    questions_json = serializers.serialize('json', questions)
    # Pass the JSON string to the template context
    return render(request, 'eduprod/flashcard.html', {'questions_json': questions_json})

