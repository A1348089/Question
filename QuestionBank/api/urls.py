from django.urls import path
from QuestionBank.views import *

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Field URLS
    path('field/',FieldListDetails.as_view(),name="field-details-list"),
    path('field/<int:pk>',FieldDetails.as_view(),name="field-details"),
    # Category URLS
    path('category/',CategoryListDetails.as_view(),name="category-details-list"),
    path('category/<int:pk>',CategoryDetails.as_view(),name="category-details"),
    # SubCategory URLS
    path('subcategory/',SubCategoryListDetails.as_view(),name="subcategory-details-list"),
    path('subcategory/<int:pk>',SubCategoryDetails.as_view(),name="subcategory-details"),
    # SubCategory URLS
    path('question/',QuestionListDetails.as_view(),name="question-details-list"),
    path('question/<int:pk>',QuestionDetails.as_view(),name="question-details"),

]

urlpatterns = format_suffix_patterns(urlpatterns)