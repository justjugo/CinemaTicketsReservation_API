from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest,Reservation,Movie
from rest_framework.decorators import api_view
from .serializers import MovieSerializer,GuestSerializer,ReservationSerializer
from rest_framework.response import Response
from rest_framework import status,filters,generics,mixins,viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#________________________Guest Model ________________________
#1 without restframwork 

def no_rest_no_model(request):
    guest=[
        {
            'id':1,
            'name':'jugurtha',
            'mobil':'0799401145'
        },
         {
            'id':2,
            'name':'jugurtha',
            'mobil':'0799401145'
        },
    ]
    return JsonResponse (guest,safe=False )


#2 without restframwork but from the model

def no_rest_from_model(request):
    data=Guest.objects.all()

    response={
        'guest':list(data.values('name','mobile'))
    }

    return JsonResponse(response)

#3 Function based View 
#3.1 GET POST
@api_view(['GET','POST'])
def FBV_List(request):
    
    
    if request.method == 'GET' :
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests, many=True)
        return Response(serializer.data)
    else :
        if request.method=='POST':
            serializer=GuestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else :
                return Response(serializer,status=status.HTTP_400_BAD_REQUEST)



#3.2 Get Put Delete
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):
    try:
        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #1 GET
    if request.method=='GET':
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    
    #2 PUT
    elif request.method=='PUT':
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #3 DELETE
    if request.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#4 CBV Class Based View 
#4.1 GET and POST

class CBV_List(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        guests=Guest.objects.all()
        serializer= GuestSerializer(guests,many=True)
        return  Response(serializer.data)
    
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST )
    
#4.2 GET PUT DELETE class based view 

class CBV_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Http404

    def get(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#5 Mixins :
#5.1 Mixins List  
class Mixins_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
#5.2 Mixins Get Put Delete

class Mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)

#6 Generics 
#6.2 get end post

class Generics_List(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer



#6.2 get put and delete

class Generics_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

#__ViewSets_________________________________     
class Viewsets_guest(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class ViewSet_movie(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class ViesSet_reservation(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer




#______________________ Film Model __________________

#1 API with the Function Based View

@api_view(['GET','POST'])
def movie_List(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def movie_PK(request,pk):
    try:
        movie=Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=MovieSerializer(movie,many=False)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#2 API with the Class Based View :

class Movie_List(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Movie_PK(APIView):
    def get_object(self,pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,reuqest,pk):
        movie=self.get_object(pk)
        serializer=MovieSerializer(movie,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        movie=self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

#3 API with mixins
#3.1 GET and POST 
class Mixins_MovieList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
#3.2 GET PUT DELETE 
class Mixins_MovisPK(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        self.destroy(request)


#4 Generics 
#4.1 GET POST

class Generics_MovieList(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class Generics_MoviePK(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

#find  movie with FBV
@api_view(['GET'])
def findmovie(request):
    movies=Movie.objects.filter(
        hall=request.data['hall'],
        
    )

    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

#new reservation 
@api_view(['POST'])
def newreservation(request):
    serializer=ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
