from django.conf.urls import url

from demo import views

urlpatterns = [
    # URLs for demo links
    url(r'^task1/$', views.task1, name='demo_task1'),
    url(r'^task2/$', views.task2, name='demo_task2'),
]
