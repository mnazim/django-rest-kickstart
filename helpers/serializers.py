from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, instance):
        return str(instance.id)
