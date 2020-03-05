from django.urls import path
from dzg_houtaiapp import views
app_name = 'dzg_houtaiapp'
urlpatterns = [
    path('hthome/',views.hthome,name='hthome'),
    path('dzg_login/',views.dzg_login,name='dzg_login'),
    path('get_code/',views.get_code,name='get_code'),
    path('check_user/',views.check_user,name='check_user'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('show_banner/',views.show_banner,name='show_banner'),
    path('del_banner/',views.del_banner,name='del_banner'),
    path('query_banner/',views.query_banner,name='query_banner'),
    path('change_banner/',views.change_banner,name='change_banner'),
]