from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, register,
                    get_jwt_token, UserViewSet)

router = routers.DefaultRouter()
router.register('titles', TitleViewSet, basename='title')
router.register('genres', GenreViewSet, basename='genre')
router.register('categories', CategoryViewSet, basename='category')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
