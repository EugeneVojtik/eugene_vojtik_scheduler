from django.contrib import auth
from django.contrib.auth import login
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView

from authentication_app.serializers import RegisterSerializer, SchedulerUserSerializer
from scheduler_APP.settings import EMAIL_HOST_USER


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"User account is created": SchedulerUserSerializer(user, context=self.get_serializer_context()).data},
            status=status.HTTP_201_CREATED)


class CreateToken(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = auth.authenticate(request, password=password, email=email)
        if user is not None:
            token, flag = Token.objects.get_or_create(user=user)
            subject = "Access token has been sent"
            send_mail(
                subject=subject,
                message=token.__str__(),
                from_email=EMAIL_HOST_USER,
                recipient_list=[email]
            )
            return Response({'your token: ': token.__str__()}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        user = auth.authenticate(
            request,
            email=request.data['email'],
            password=request.data['password']
        )
        if user is not None:
            login(request, user)
            return Response({}, status=status.HTTP_201_CREATED)
        return Response("user is not registered", status=status.HTTP_400_BAD_REQUEST)
