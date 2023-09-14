from rest_framework import viewsets

from api.permissions import AdminOrReadOnly
from api.serializers import MoviesSerializer
from movies.models import Movie


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (AdminOrReadOnly,)
    throttle_scope = 'low_request'
    ordering = ('id',)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action != 'partial_update' and self.action != 'update':
            context['exclude_fields'] = ['new_poster']
        return context
