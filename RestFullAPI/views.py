from tokenize import TokenError

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from tenacity.retry import retry_if_result

from Home.serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from tenacity import retry, stop_after_attempt, wait_fixed

def welcome(request):
    return render(request,'/')

@retry(stop=stop_after_attempt(5), wait=wait_fixed(4), reraise=True)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error': 'Username o Password no válidos'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({'token': token.key, "user": serializer.data},status=status.HTTP_200_OK)

# @api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, "users": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@retry(retry=retry_if_result(lambda x: x is None))
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile(request):
    # print(request.user)
    # permission_classes(IsAuthenticated,)
    serializer = ProfileSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def logout(self, request):

    permission_classes = (IsAuthenticated,)

    tokens = OutstandingToken.objects.filter(user_id=request.user.id)
    for token in tokens:
        t, _ = BlacklistedToken.objects.get_or_create(token=token)

    return Response(status=status.HTTP_205_RESET_CONTENT)