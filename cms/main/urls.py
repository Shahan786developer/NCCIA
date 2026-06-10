from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('verifications/', verifications, name='verifications'),
    path('newcomplaint/', newcomplaint, name='newcomplaint'),
    path('newenquiry/', newenquiry, name='newenquiry'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
