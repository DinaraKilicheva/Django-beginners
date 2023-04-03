from django.db import models


# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_true=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question}-{self.text}-{self.is_true}"
