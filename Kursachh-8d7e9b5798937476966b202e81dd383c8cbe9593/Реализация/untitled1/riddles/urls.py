from django.conf.urls import url

from . import views

app_name = 'riddles'

urlpatterns = [
    url(r'^$', views.riddles, name='riddles'),
    url('(?P<plane_id>\d+)', views.air_detail, name='air_detail_url'),
    url('fly/', views.fly_list, name='fly_list_url'),
    url('(?P<fly_id>\d+)', views.fly_detail, name='fly_detail_url')

]
