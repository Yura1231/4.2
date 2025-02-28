
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .serializers import UserRegistrationSerializer ,  PostSerializer
from .models import User, Post
from bson import ObjectId
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = request.data
        
        if User.objects.filter(email=data["email"]).exists():
              return Response({"message": "Користувач з таким email вже існу'''є!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully', 'email': serializer.data['email']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])

def get_user_by_id(request, user_id):
    # Шукаємо користувача за _id
    try:
        user = User.objects.get(_id=ObjectId(user_id))  # Використовуємо поле _id
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Якщо користувач знайдений, серіалізуємо його дані
    serializer = UserRegistrationSerializer(user)   
    return Response(serializer.data )



@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # 🔹 Перевіряємо, чи вказані всі поля
    if not email or not password:
        return Response({'message': 'Email та пароль обов’язкові!'}, status=status.HTTP_400_BAD_REQUEST)

    # 🔹 Перевіряємо, чи користувач існує
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'message': 'Користувача з таким email не знайдено!'}, status=status.HTTP_404_NOT_FOUND)

    # 🔹 Перевіряємо правильність пароля
    if not check_password(password, user.password):  # Використовуємо check_password()
        return Response({'message': 'Неправильний пароль!'}, status=status.HTTP_400_BAD_REQUEST)

    # 🔹 Генеруємо JWT-токени
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'message': 'Вхід успішний!',
        'user': {
            '_id': str(user._id),
            'email': user.email,
            'username': user.username,
            
        }
    }, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = request.data
    data['author'] = ObjectId(request.user._id)  # Встановлюємо автора поста
    serializer = PostSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)