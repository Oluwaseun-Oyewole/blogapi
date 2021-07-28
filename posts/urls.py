from django.db import router
from django.urls import path
from rest_framework import urlpatterns
from rest_framework import routers
from .views import PostViews, UserViews
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', PostViews, basename='posts')
router.register('users', UserViews, basename='users' )


urlpatterns = router.urls


# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]