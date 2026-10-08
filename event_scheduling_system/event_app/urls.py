from django.urls import path
from event_app.views import*

urlpatterns = [
    path('',login_page, name='login_page'),
    path('register-page/',register_page, name='register_page'),
    path('logout-page/',logout_page, name='logout_page'),
    
    path('dashboard/',dashboard, name='dashboard'),
    path('event-page/',event_page, name='event_page'),
    
    path('event-create/',event_create, name='event_create'),
    path('event-details/<str:e_id>',event_details, name='event_details'),
    path('event-update/<str:e_id>',event_update, name='event_update'),
    path('event-delete/<str:e_id>',event_delete, name='event_delete'),
]