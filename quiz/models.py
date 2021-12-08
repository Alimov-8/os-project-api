from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, id: {self.id}"


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quiz')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    # RATE_CHOICES = (
    #     (1, 'Choice 1'),
    #     (2, 'Choice 2'),
    #     (3, 'Choice 3'),
    #     (4, 'Choice 4'),
    # )
    question = models.CharField(max_length=255)
    
    # choice_1 = models.CharField(max_length=255, null=True, unique=True)
    # choice_2 = models.CharField(max_length=255, null=True, unique=True)
    # choice_3 = models.CharField(max_length=255, null=True, unique=True)
    # correct_answer = models.IntegerField(choices=RATE_CHOICES, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.question
    
    
class Choice(models.Model):
    choice_id = models.IntegerField()
    choice = models.CharField(max_length=255)
    is_correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')

    def __str__(self):
        return self.choice

