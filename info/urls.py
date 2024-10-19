
from django.urls import path
from .views import HomeView, AboutMeView, MyProjectsView, ContactView, MyResearchView, SkillsView, WorkView, EducationView, ResumeView, PortfolioView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeView, name='home'),
    path('about/', views.AboutMeView, name='about'),
    path('projects', views.MyProjectsView, name='projects'),
    path('research/', views.MyResearchView, name='research'),
    path('skills/', views.SkillsView, name='skills'),
    path('resume/', views.ResumeView, name='resume'),
    path('work/', views.WorkView, name='work'),
    path('portfolio/', views.PortfolioView, name='portfolio'),
    path('education/', views.EducationView, name='education'),
    path('contact/', views.ContactView, name='contact'),

    # path('resume/', AutoGenerateView.as_view(), name='auto'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
