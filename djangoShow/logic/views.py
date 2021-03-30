from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from django.core.exceptions import PermissionDenied


def start_page(request):
    return render(request, 'logic/start.html', {'user': request.user})
