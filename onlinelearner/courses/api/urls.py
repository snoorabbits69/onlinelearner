from django.urls import path,include
from rest_framework import routers
from . import views

app_name='courses'

router=routers.DefaultRouter()
router.register('courses',views.CourseViewset)
router.register('subjects',views.SubjectViewset)

urlpatterns = [
    
    path('',include(router.urls)),
]
