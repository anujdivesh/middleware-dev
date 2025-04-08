import django_filters
from .models import Dashboard

class DashboardFilter(django_filters.FilterSet):
    display_title = django_filters.CharFilter(field_name='display_title', lookup_expr='icontains')
    country_id = django_filters.NumberFilter(field_name='country__id') 

    class Meta:
        model = Dashboard
        fields = ['display_title', 'country__id']  # Include theme_id for filtering on the related Theme model
