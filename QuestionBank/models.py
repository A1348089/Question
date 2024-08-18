from django.db import models

# Create your models here.

class Field(models.Model):
    field_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.field_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE,related_name="category")
    def __str__(self):
        return self.category_name
    
class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100, null=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.sub_category_name

class QuestionType(models.Model):
    question_type = models.CharField(max_length=100, null=False)
    subcategory = models.ManyToManyField(SubCategory)
    def __str__(self):
        return self.question_type

class Question(models.Model):
    LEVEL_CHOICES = [
        ("EASY","EASY"),
        ("INTERMEDIATE","INTERMEDIATE"),
        ("HARD","HARD")
    ]
    question = models.CharField(max_length=500, null=False)
    level = models.CharField(max_length=20, choices = LEVEL_CHOICES, default="EASY")
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, related_name="question")
    
    def __str__(self):
        return self.question
    
class Options(models.Model):
    option_text = models.CharField(max_length=250, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="options")
    is_correct = models.BooleanField()

    def __str__(self):
        return self.option_text
    
class Matches(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="matches")
    left_text = models.CharField(max_length=250, null=False)
    right_text = models.CharField(max_length=250, null=False)

    def __str__(self):
        return f"{self.left_text},{self.right_text}"
    
class Blanks(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="blanks")
    blank_text = models.CharField(max_length=100,null=False)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.blank_text