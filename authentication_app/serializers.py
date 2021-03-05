from rest_framework.serializers import ModelSerializer

from event_manager.models import SchedulerUser


class SchedulerUserSerializer(ModelSerializer):
    class Meta:
        model = SchedulerUser
        fields = ('id', 'username', 'email', 'country')


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = SchedulerUser
        fields = ('id', 'username', 'email', 'password', 'country')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = SchedulerUser.objects.create_user(username=validated_data['username'],
                                                 email=validated_data['email'],
                                                 password=validated_data['password'],
                                                 country=validated_data['country'])

        return user
