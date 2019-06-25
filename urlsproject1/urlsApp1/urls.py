from django.conf.urls import url
urlpatterns = [
    url(r'^hydjobs/', 'views.hydjobsinfo'),
    url(r'^chennaijobs/','views.chennaijobsinfo'),
    url(r'^mumbaijobs/','views.mumbaijobsinfo'),
    url(r'^kolkatajobs/','views.kolkatajobsinfo'),

]
