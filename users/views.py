# # users/views.py
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework_jwt.settings import api_settings
# from .serializers import UserSerializer



# from django.contrib.auth import authenticate, login
# from django.http import JsonResponse
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny,IsAuthenticated

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()

#         # Generate JWT token
#         payload = jwt_payload_handler(user)
#         token = jwt_encode_handler(payload)

#         return Response({'token': token}, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([AllowAny])  # Allow unauthenticated users to access this view
# def user_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
    
#     # Authenticate the user
#     user = authenticate(request, username=username, password=password)
    
#     if user is not None:
#         # Login the user
#         login(request, user)
        
#         # Optionally, you can return a success response
#         return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     else:
#         # Authentication failed, return an error response
#         return JsonResponse({'message': 'Unable to log in with provided credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     try:
#         refresh_token = request.data.get('refresh_token')
#         if refresh_token:
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

#     except Exception as e:
#         return Response({"message": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response