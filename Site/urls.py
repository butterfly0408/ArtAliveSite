from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('about', views.about, name='about'),
    path('classes', views.classes, name='classes'),
    path('exhibition', views.exhibition, name='exhibition'),
    path('news_events', views.news_events, name='news_events'),
    path('contact', views.contact, name='contact'),
    path('join', views.join, name='join'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),

    path('teacher_profile/<int:teacher_id>', views.teacher_profile, name='teacher_profile'),
    
    # API
    path('painting_data/<int:painting_id>', views.painting_data, name='painting_data'),
    
    path('contact_mail', views.contact_mail, name='contact_mail'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('join_form', views.join_form, name='join_form'),
]
