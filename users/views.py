from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

# Create your views here.
class UserView(APIView):

    def post(self, request):
        data = request.POST
        print(data)
        username = data.get("username", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        if not username or not password or not password_confirm or not email:
            return Response({
                'status': 400,
                'message': 'please fill all the fields'
            })
        if password != password_confirm:
            return Response({
                'status': 400,
                'message': 'the password entered twice must be the same'
            })
        if User.objects.filter(email=email).exists():
            return Response({
                'status': 400,
                'message': 'the email has been registered'
            })
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        return Response({
            'status': 201,
            'message': 'register successfully'
        })

class InfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        user = request.user
        return Response({
            "status": 200,
            "message": "success",
            "data": {
                "username": user.username,
                "email": user.email
            }
        })