from django.urls import path
from userapp import views
app_name = 'userapp'
urlpatterns = [
    path('user_echarts/',views.user_echarts,name='user_echarts'),
    path('get_echarts/',views.get_echarts,name='get_echarts'),
    path('user_map/',views.user_map,name='user_map'),
    path('get_map/',views.get_map,name='get_map'),
]