from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

class Signup (APIView):
    def post (self, request):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message" : "User Successful Created!"
                    
                },
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )

# LOGIN View
class LoginView (APIView):
    permission_classes = [AllowAny]

    def post (self, request):
        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh =  RefreshToken.for_user(user)
            return Response(
                {
                    'Success' : "OK",
                    "Message" : "Login Succssfull",
                    "user" : { "id" : user.id,
                              "email" : user.email },
                              "tokens" : {
                                  "access" : str(refresh.access_token),
                                  "refresh" : str(refresh)
                              }


                },status=status.HTTP_200_OK
               
            )    

# Logout
class Logoutview (APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post (self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(
                {"errors" : "refresh token required!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response (
                {"Message" : "succussfull Logout!.."},
                status=status.HTTP_200_OK
            )    
        except TokenError:
            return Response(
                {
                    "Message" : "Invalid refresh_token..."
                },
                status=status.HTTP_400_BAD_REQUEST
            )