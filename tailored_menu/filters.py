import django_filters
from .models import TailoredMenu

class TailoredMenuFilter(django_filters.FilterSet):
    display_title = django_filters.CharFilter(field_name='display_title', lookup_expr='icontains')
    country_id = django_filters.NumberFilter(field_name='country_id')  # Use theme__id for filtering the related model's id

    class Meta:
        model = TailoredMenu
        fields = ['display_title', 'country_id']  # Include theme_id for filtering on the related Theme model
