from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Complaint
from django.utils import timezone
from django.db.models import Q


def index(request):
    latest_complaint_list = Complaint.objects.all().exclude(answer="Нет ответа").all().order_by('-id')
    return render(request, 'appeals/list.html', {'latest_complaint_list': latest_complaint_list})


def add_complaint(request):
    Complaint(text=request.POST['text'], answer="Нет ответа").save()
    return HttpResponseRedirect(reverse('appeals:index'))
