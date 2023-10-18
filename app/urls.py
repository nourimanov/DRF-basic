from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comment', views.CommentModelViewSet, 'comment')


urlpatterns = [
    path('', include(router.urls)),
    path('post-list', views.PostListAPIView.as_view(), name='post-list'),
    path('post-add', views.PostAddAPIView.as_view(), name='post-add'),
    path('post-update/<int:pk>', views.PostUpdateAPIView.as_view(), name='post-update'),
    path('post-delete/<int:pk>', views.PostDestroyAPIView.as_view(), name='post-delete'),
]
