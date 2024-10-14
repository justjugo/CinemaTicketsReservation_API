

from django.contrib import admin
from django.urls import path,include
from tickets.views import no_rest_no_model,no_rest_from_model,FBV_List,FBV_pk,CBV_List,CBV_pk,Mixins_List,Mixins_pk,Generics_List,Generics_PK,Viewsets_guest,movie_List,movie_PK,Movie_List,Movie_PK,Mixins_MovieList,Mixins_MovisPK,Generics_MovieList,Generics_MoviePK,ViewSet_movie,ViesSet_reservation,findmovie,newreservation
from rest_framework.routers import DefaultRouter
from tickets import views
from rest_framework.authtoken.views import obtain_auth_token


router= DefaultRouter()
router.register('guests',Viewsets_guest)
router.register('movies',ViewSet_movie)
router.register('reservations',ViesSet_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('django/jsonresponsenomodel/',no_rest_no_model),
    #2
    path('django/jsonresponsemodel/',no_rest_from_model),

    #3 function based view
    path('rest/FBV',FBV_List),
    path('rest/FBV/<int:pk>',FBV_pk),

    #4 class based view 
    path('rest/CBV',CBV_List.as_view()),
    path('rest/CBV/<int:pk>',CBV_pk.as_view()),

    #5 Mixins 
    path('rest/mixins',Mixins_List.as_view()),
    path('rest/mixins/<int:pk>',Mixins_pk.as_view()),

    #6 Generics
    path('rest/generics',Generics_List.as_view()),
    path('rest/generics/<int:pk>',Generics_PK.as_view()),

    #7 Viewset
    path('rest/viewsets/',include(router.urls)),

    #_____Movie_____
    #1 FBV
    path('rest/FBV/Movie/',movie_List),
    path('rest/FBV/Movie/<int:pk>',movie_PK),

    #2 CBV 
    path('rest/CBV/Movie/',Movie_List.as_view()),
    path('rest/CBV/Movie/<int:pk>',Movie_PK.as_view()),

    #3 Mixins
    path('rest/mixins/movie/',Mixins_MovieList.as_view()),
    path('rest/mixins/movie/<int:pk>',Mixins_MovisPK.as_view()),

    #6 Generics
    path('rest/generics/movie',Generics_MovieList.as_view()),
    path('rest/generics/movie/<int:pk>',Generics_MoviePK.as_view()),

    #find a movie with FBV

    path('FBV/movie/',findmovie),
    path('FBV/newreservation/',newreservation),

    path('api-auth',obtain_auth_token,name='obtain_auth_token')



   







]
