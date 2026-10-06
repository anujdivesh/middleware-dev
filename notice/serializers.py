from rest_framework import serializers
from rest_framework.fields import empty
from .models import Notice

class DefaultTrueBooleanField(serializers.BooleanField):
    # For multipart/form requests DRF treats a missing checkbox as False;
    # skip it instead so the model default (True) applies.
    default_empty_html = empty

class NoticeSerializer(serializers.ModelSerializer):
    description_enabled = DefaultTrueBooleanField(required=False)
    image_enabled = DefaultTrueBooleanField(required=False)
    url_enabled = DefaultTrueBooleanField(required=False)
    is_notice_enabled = DefaultTrueBooleanField(required=False)

    class Meta:
        model = Notice
        fields = ('__all__')
