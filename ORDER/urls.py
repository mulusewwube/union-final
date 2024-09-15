from django.urls import path
from .views import (profile_page,research_help,Writing_editing_project,create_research,create_thesis,graphics_design_submission,programming_project_submission,video_editing_submission,transcription,business_plan,assignment,user_orders,completed_orders,pending_orders,website_project)
from django.conf import settings
from django.conf.urls.static import static


app_name = 'order'

urlpatterns = [
               
    path('pending_orders/',pending_orders,name='pending_orders' ),
    path('completed_orders/',completed_orders,name='completed_orders' ),
    path('total_order/',user_orders,name='total_order' ),
    
    path('order/',create_research,name='order' ),
    path('thesis/',create_thesis,name='thesis' ),
    path('graphdesign/',graphics_design_submission,name='graphics-design' ),
    path('programming/',programming_project_submission,name='program-project' ),
    path('video/',video_editing_submission,name='video-project' ),
    path('transcription/',transcription,name='transcription' ),
    path('assignment/',assignment,name='assignment' ),
    path('business/',business_plan,name='business-plan' ),
    path('website/',website_project,name='website-project' ),
    path('editing/',Writing_editing_project,name='editing-project' ),
    path('research_help/',research_help,name='research_help'),

    path('profile/',profile_page,name='profile' ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)