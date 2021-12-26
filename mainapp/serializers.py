from rest_framework import serializers 
from .models import Customer, Student, Financial, Result, Course

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class academicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Customer
		fields = ['email', 'username', 'name', 'bin', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		customer = Customer(
                    email=self.validated_data['email'],
					username=self.validated_data['username'],
                    name=self.validated_data['name'],
                    bin=self.validated_data['bin']
				)

		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		customer.set_password(password)
		customer.save()
		return customer