from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import Resume

from django.contrib.auth.models import User

# Create your views here.
class UserView(APIView):

    def post(self, request):
        data = request.POST
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

class ResumeView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        data = request.POST
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        phone = data.get("phone", "").strip()
        gender = data.get("gender", "").strip()
        bornAddress = data.get("bornAddress", "").strip()
        city = data.get("city", "").strip()
        degree = data.get("degree", "").strip()
        major = data.get("major", "").strip()
        UU = data.get("UU", "").strip()
        UGPA = data.get("UGPA", 0)
        GU = data.get("GU", "").strip()
        GGPA = data.get("GGPA", 0)
        PU = data.get("PU", "").strip()
        PGPA = data.get("PGPA", 0)
        intro = data.get("intro", "").strip()
        workExp = data.get("workExp", "").strip()
        projExp = data.get("projExp", "").strip()
        if not name or not email or not phone or not degree or not major:
            return Response({
                'status': 400,
                'message': 'please fill all the needed fields'
            })
        resume = Resume(
            username=name,
            email=email,
            phone=phone,
            gender=gender,
            born_address=bornAddress,
            city=city,
            degree=degree,
            major=major,
            bachelor_school=UU,
            bachelor_GPA=UGPA,
            master_school=GU,
            master_GPA=GGPA,
            doctor_school=PU,
            doctor_GPA=PGPA,
            candidate_introduction=intro,
            work_experience=workExp,
            project_experience=projExp
        )
        resume.save()
        return Response({
            'status': 201,
            'message': 'online resume uploaded successfully'
        })