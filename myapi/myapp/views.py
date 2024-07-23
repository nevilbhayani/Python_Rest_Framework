from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

# Create your views here.

class BlogApi(APIView):
    def get(self,request):
        blogdata = Blog.objects.all()
        blogser = BlogSerializer(blogdata,many=True)
        return Response({"data":blogser.data})
    
    
    def post(self,request):
        ser_data =  BlogSerializer(data=request.data)
        if not ser_data.is_valid():
          return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"successful data insert"})


    def put(self,request):
        try:
            id=request.data["id"]
            tododata =  Blog.objects.get(id=id)
            ser_data = BlogSerializer(tododata,request.data)
            if not ser_data.is_valid():
              return Response({"message":"something went wrong","errors":ser_data.errors})
            ser_data.save()
            return Response({"userdata":ser_data.data,"message":"todo updated"})
        except Exception as e:
            return Response({"msg":"id not fond"})
        
    def delete(self,request):
        try:
            id = request.data['id']
            data = Blog.objects.get(id=id)
            data.delete()
            return Response({"message":"Delete Successfully"})
        except:
            return Response({"Error":"Something Wrong"})
