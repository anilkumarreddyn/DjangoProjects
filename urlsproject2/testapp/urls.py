from django.conf.urls import url,include
from testapp import views
urlpatterns = [
    url(r'^hydjobs/', views.hydjobsinfo),
    url(r'^punejobs/', views.punejobsinfo),
    url(r'^mumbaijobs/', views.mumbaijobsinfo),
    url(r'^noidajobs/', views.noidajobsinfo),
]
