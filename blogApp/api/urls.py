from django.urls import path
from rest_framework import routers

from blogApp.api.views import CategoryView, BlogPostUDView

# router = routers.DynamicRoute()
router = routers.DefaultRouter()
router.register('blogs', BlogPostUDView)


urlpatterns = [
    path("category", CategoryView.as_view()),

] 
urlpatterns += router.urls
