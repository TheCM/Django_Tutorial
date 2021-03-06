import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Poll

class QuestionMethodTests(TestCase):
  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() should return False for questions whose
    pub_date is in the future.
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Poll(pub_date=time)
    self.assertEqual(future_question.was_published_recently(), False)	

# Create your tests here.
