from rest_framework import serializers
from rest_framework.fields import CharField

from movies.models import Movie


class MoviesSerializer(serializers.ModelSerializer):
    new_poster = CharField(required=None, default=None)

    class Meta:
        model = Movie
        exclude = (
            'title_en',
            'type_en',
            'genre_en',
            'director_1_en',
            'director_2_en',
            'star_1_en',
            'star_2_en',
            'star_3_en',
            'description_en',
        )

    def get_fields(self):
        fields = super().get_fields()
        exclude_fields = self.context.get('exclude_fields', [])
        for field in exclude_fields:
            fields.pop(field, default=None)
        return fields

    def validate(self, attrs):
        if attrs.get('new_poster'):
            attrs['poster'] = attrs['new_poster']
        return attrs
