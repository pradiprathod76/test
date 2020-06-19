from project.views import UserViewset,CategoryViewset,AudioViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userapi',UserViewset)
router.register('categoryapi',CategoryViewset)
router.register('audioapi',AudioViewset)
