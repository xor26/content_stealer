from main_app import views
from django.urls import path
from rest_framework import routers

from main_app.views import ListPostsView

router = routers.DefaultRouter()
router.register(r'/', views.ListPostsView)

urlpatterns = [
    path('receive', views.receive_posts),
    path('send', views.send_posts),
    path('api_view', ListPostsView.as_view())

]

