# main/urls.py
from django.urls import path
from .views import index, base, send_file_view, about, books, journals, news, presentations, pics, fliers, advid, rec,test ,training, education, policy, security, mentor, research, footer

urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('footer/', footer, name='footer'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
    path('journals/', journals, name='journals'),
    path('news/', news, name='news'),
    path('presentations/', presentations, name='presentations'),
    path('pics/', pics, name='pics'),
    path('training/', training, name='training'),
    path('education/', education, name='education'),
    path('policy/', policy, name='policy'),
    path('security/', security, name='security'),
    path('mentor/', mentor, name='mentor'),
    path('research/', research, name='research'),
    path('rec/', rec, name='rec'),
    path('test/', test, name='test'),
    path('fliers/', fliers, name='fliers'),
    path('advid/', advid, name='advid'),
    path('send-file/', send_file_view, name='send_file'),
]
