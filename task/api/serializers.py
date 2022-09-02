from rest_framework import serializers
from task.models import Task
from account.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = '__all__'
        read_only_fields = ('user', )

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=self.context.get('request').user.id)
        return super().create(validated_data) 