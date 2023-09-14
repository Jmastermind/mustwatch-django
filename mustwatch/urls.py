from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from rest_framework.schemas import get_schema_view

from core.views import SignUp

handler400 = 'core.views.bad_request'
handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

urlpatterns = [
    path(
        '',
        include('movies.urls', namespace=apps.get_app_config('movies').name),
    ),
    path('', include('django.contrib.auth.urls')),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about',
    ),
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'api/',
        include('api.urls', namespace=apps.get_app_config('api').name),
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='api/redoc.html'),
        name='redoc',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
