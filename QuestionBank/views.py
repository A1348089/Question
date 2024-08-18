from django.shortcuts import render

from QuestionBank.models import *
from QuestionBank.api.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
# Create your views here.

################ Field Views Start ####################
class FieldListDetails(APIView):
    def get(self,request):
        queryset = Field.objects.all()
        serializer = FieldSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = FieldSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FieldDetails(APIView):

    def get_object(self, pk):
        try:
            return Field.objects.get(pk=pk)
        except Field.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = FieldSerializer(queryset)
        return Response(serializer.data)
    def put(self,request,pk):
        field_object = self.get_object(pk=pk)
        serializer = FieldSerializer(field_object, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################ Field Views End ####################

################ Category Views Start ####################
class CategoryListDetails(APIView):

    def get(self,request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetails(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)
    def put(self,request,pk):
        category_object = self.get_object(pk=pk)
        serializer = CategorySerializer(category_object, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
################ Category Views End ####################
    
################ SubCategory Views Start ####################
class SubCategoryListDetails(APIView):

    def get(self,request):
        queryset = SubCategory.objects.all()
        serializer = SubCategorySerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = SubCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubCategoryDetails(APIView):
    def get_object(self, pk):
        try:
            return SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = SubCategorySerializer(queryset)
        return Response(serializer.data)
    def put(self,request,pk):
        subcategory_object = self.get_object(pk=pk)
        serializer = SubCategorySerializer(subcategory_object, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
################ SubCategory Views End ####################

################ Questions Views Start ####################
class QuestionListDetails(APIView):

    def get(self,request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionDetails(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data)
    def put(self,request,pk):
        question_object = self.get_object(pk=pk)
        serializer = QuestionSerializer(question_object, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
################ Questions Views End ####################