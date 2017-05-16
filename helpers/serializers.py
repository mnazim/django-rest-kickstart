from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()

    def get_pk(self, instance):
        return str(instance.id)
