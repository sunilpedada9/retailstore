from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','password','first_name','last_name','user_type','phone_number','address','status_id')
        extra_kwargs={'password':{'write_only':True,'required':False}}
    
    def create(self,validated_data):
        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self,instance,validated_data):
        instance.username=validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.user_type=validated_data.get('user_type',instance.user_type)
        instance.phone_number=validated_data.get('phone_number',instance.phone_number)
        instance.address=validated_data.get('address',instance.address)
        instance.status_id=validated_data.get('status_id',instance.status_id)
        instance.save()
        return instance