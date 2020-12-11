from django.urls import path

from main.api.views import api_detail_court_view

app_name = 'main'

urlpatterns = [
    path('<name>/', api_detail_court_view, name='detail')
]