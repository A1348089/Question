from rest_framework import serializers

from QuestionBank.models import *

class BlanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blanks
        fields = '__all__'

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
  
    options = OptionsSerializer(many=True, read_only = True)
    matches = MatchesSerializer(many=True, read_only = True)
    blanks = BlanksSerializer(many=True, read_only = True)

    class Meta:
        model = Question
        fields = '__all__'
   

class QuestionTypeSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only = True)
    class Meta:
        model = QuestionType
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Field
        fields = '__all__'










