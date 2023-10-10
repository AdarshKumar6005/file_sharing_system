from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group



@api_view(['POST'])
def login(request):
    try:
        data= request.data
        username = data['username']
        password = data['password']
        user = authenticate(username = username, password=password)
        if user == None:
            return Response({'msg':'Unable to Authenticate'}, status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'Token':str(token)}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'msg':'Unable to login'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    data=request.data
    if data.get('username')==None:
        return Response({'msg':"Username not provided"}, status=status.HTTP_400_BAD_REQUEST)
    if data.get('password')==None:
        return Response({'msg':"Password not provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        a = User.objects.create_user(**data)
    except Exception as e:
        print(e)
        return Response({'msg':"Invalid data, unable to create user"}, status=status.HTTP_400_BAD_REQUEST)
    
    grp = Group.objects.get(id=1)
    grp.user_set.add(a)
    grp.save
    
    return Response({'msg':"User Created successfully"}, status=status.HTTP_201_CREATED)
