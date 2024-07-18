from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now()+datetime.timedelta(days=30)
        futrue_question = Question(pub_data=time)
        self.assertIs(futrue_question.was_published_recently(),False)
# Create your tests here.
