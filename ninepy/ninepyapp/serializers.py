from rest_framework.serializers import ModelSerializer
from .models import Questions

class Questions_serial(ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'
