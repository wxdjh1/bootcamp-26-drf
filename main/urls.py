from rest_framework.routers import SimpleRouter
from main.views import PostViewsSet

router = SimpleRouter()
router.register('post', PostViewsSet, basename='posts')

urlpatterns = router.urls