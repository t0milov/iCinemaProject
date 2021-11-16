from django.urls import path

from .views import NodeView

app_name = 'scripts'

urlpatterns = [
    path('get/', NodeView.as_view()),     # URL по которому отображается data
    path('post/', NodeView.post, name='post')
]