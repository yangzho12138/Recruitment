from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import Resume
from django.core import serializers

from django.contrib.auth.models import User
from jobs.producer import publish

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
        UGPA = data.get("UGPA", "").strip()
        GU = data.get("GU", "").strip()
        GGPA = data.get("GGPA", "").strip()
        PU = data.get("PU", "").strip()
        PGPA = data.get("PGPA", "").strip()
        intro = data.get("intro", "").strip()
        workExp = data.get("workExp", "").strip()
        projExp = data.get("projExp", "").strip()
        if not name or not email or not phone or not degree or not major:
            return Response({
                'status': 400,
                'message': 'please fill all the needed fields'
            })
        try:
            resumeExisting = Resume.objects.get(email=email)
            resumeExisting.username = name or resumeExisting.username
            resumeExisting.phone = phone or resumeExisting.phone
            resumeExisting.gender = gender or resumeExisting.gender
            resumeExisting.born_address = bornAddress or resumeExisting.born_address
            resumeExisting.city = city or resumeExisting.city
            resumeExisting.degree = degree or resumeExisting.degree
            resumeExisting.major = major or resumeExisting.major
            resumeExisting.bachelor_school = UU or resumeExisting.bachelor_school
            resumeExisting.bachelor_GPA = UGPA or resumeExisting.bachelor_GPA
            resumeExisting.master_school = GU or resumeExisting.master_school
            resumeExisting.master_GPA = GGPA or resumeExisting.master_GPA
            resumeExisting.doctor_school = PU or resumeExisting.doctor_school
            resumeExisting.doctor_GPA = PGPA or resumeExisting.doctor_GPA
            resumeExisting.candidate_introduction = intro or resumeExisting.candidate_introduction
            resumeExisting.work_experience = workExp or resumeExisting.work_experience
            resumeExisting.project_experience = projExp or resumeExisting.project_experience
            resumeExisting.save()
            return Response({
                'status': 201,
                'message': 'online resume updated successfully'
            })
        except Resume.DoesNotExist:
            resume = Resume(
                username=name,
                applicant=User.objects.get(email=request.user.email),
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
                project_experience=projExp,
            )
            resume.save()
            return Response({
                'status': 201,
                'message': 'online resume uploaded successfully',
            })


    def get(self, request):
        user = request.user
        print(user)
        try:
            resume = Resume.objects.get(email=user.email)
            print(resume)
            return Response({
                'status': 200,
                'message': 'get resume successfully',
                'data': serializers.serialize('json', [resume,])
            })
        except Resume.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'resume not found'
            })


class uploadFileView(APIView):
    permission_classes = ([IsAuthenticated])

    def post(self, request):
        file = request.FILES.get('file')
        if file:
            try:
                resume = Resume.objects.get(email=request.user.email)
                resume.attachment = file
                resume.save()
                return Response({
                    'status': 200,
                    'message': 'Upload successfully!'
                })
            except Resume.DoesNotExist:
                return Response({
                    'status': 404,
                    'message': 'Please submit online resume before upload attachment!'
                })
        return Response({
            'status': 404,
            'message': 'Not found file'
        })


