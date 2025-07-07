import django_filters
from .models import Widget

class WidgetFilter(django_filters.FilterSet):
    display_title = django_filters.CharFilter(field_name='display_title', lookup_expr='icontains')
    country_id = django_filters.NumberFilter(field_name='country') 

    class Meta:
        model = Widget
        fields = ['display_title', 'country']  # Include theme_id for filtering on the related Theme model
