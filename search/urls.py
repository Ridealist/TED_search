from django.urls import path
from .api.views import TalkList
from .views import IndexView

app_name = 'search'
urlpatterns = [
    path('api/v1/talks/', TalkList.as_view(), name='results'),
    path('', IndexView.as_view(), name='index'),
]