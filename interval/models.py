from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=32)
    date = models.DateTimeField(default=datetime.now)
    rightanswers = models.IntegerField(null=True) #if user answers right this goes up
    status = models.BooleanField(default=True) #if test is already active
    question_index = models.IntegerField(default=0)



class Question(models.Model):
    question_index = models.IntegerField()
    user_answer = models.CharField(max_length=32)
    xp_gain = models.IntegerField(default=250)
    start_note = models.CharField(max_length=32)
    answer_array = models.CharField(max_length=250)
    interval_type = models.CharField(max_length=32)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=32)

    def answer_array_as_list(self):
        return self.answer_array.split(",")

    def is_last_question(self):
        return self.question_index >= 7
