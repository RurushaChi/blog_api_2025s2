from rest_framework.routers import DefaultRouter

from blog.viewsets import CategoryViewSet, PostViewSet, ProfileViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

router.register(r'posts', PostViewSet)

router.register(r'profiles', ProfileViewSet)

router.register(r'comments', CommentViewSet)

urlpatterns= router.urls