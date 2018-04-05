# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def task1(request):
    return render(request, 'demo/task1.html')


def task2(request):
    return render(request, 'demo/task2.html')
