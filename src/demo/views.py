# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from demo import tasks


def task1(request):
    tasks.demo_task1.delay()
    return render(request, 'demo/task1.html')


def task2(request):
    tasks.demo_task2.delay()
    return render(request, 'demo/task2.html')
