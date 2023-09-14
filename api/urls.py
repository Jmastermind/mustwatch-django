from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import MoviesViewSet

app_name = '%(app_label)s'

router = routers.DefaultRouter()
router.register('movies', MoviesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
