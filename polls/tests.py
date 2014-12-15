import datetime

from django.test import TestCase
from polls.views import Question,Choice
from django.utils import timezone
# Create your tests here.
class QuestionMethodTest(TestCase):
    def test_was_published_recently_with_future_question(self):
         time = timezone.now() + datetime.timedelta(days=30)
         future_question =Question(pub_date=time)
         self.assertEqual(future_question.was_published_recently(),False)
         