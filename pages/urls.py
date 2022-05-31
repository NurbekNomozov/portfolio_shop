from django.urls import path

from pages.views import ContactCreateView, HomeTemplateview, AboutTemplateview

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('', HomeTemplateview.as_view(), name='home'),
    path('about/', AboutTemplateview.as_view(), name='about'),
]