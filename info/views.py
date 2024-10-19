from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'info/index.html', {})

def AboutMeView(request):
    return render(request, 'info/about.html', {})

def MyProjectsView(request):
    return render(request, 'info/projects.html', {})

def MyResearchView(request):
    return render(request, 'info/home.html', {})

def SkillsView(request):
    return render(request, 'info/skills.html', {})

def PortfolioView(request):
    return render(request, 'info/portfolio.html', {})

def EducationView(request):
    return render(request, 'info/education.html', {})

def ResumeView(request):
    return render(request, 'info/resume.html', {})

def ContactView(request):
    return render(request, 'info/contact.html', {})

def WorkView(request):
    return render(request, 'info/work.html', {})
# Resume view
# class AutoGenerateView(APIView):
#     def post(self, request):
#         User = get_user_model()
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')

#         if User.objects.filter(email=email).exists():
#             return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

#         user = User.objects.create_user(username=username, password=password, email=email)
#         user.save()
#         return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    
#     def get(self, request):
#         return Response({'message': 'All Users that created successfully'}, status=status.HTTP_201_CREATED)
