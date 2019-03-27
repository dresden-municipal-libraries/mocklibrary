import datetime
from catalog.forms import RenewBookForm
from django.test import TestCase

# Test for Forms models here

class RenewBookFormTest(self):

    def test_renew_book_in_past(self):

        """
        Test for invalid form if renewal date for books is yesterday
        """

        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date' : date})
        self.assertTrue(form.is_valid())

    def test_renew_book_in_future(self):

        """
        Test for invalid form if renewal date for books more than 4 weeks
        """

        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date' : date})
        self.assertTrue(form.is_valid())

    def test_renew_book_is_today(self):

        """
        Test for invalid form if renewal date for books is yesterday
        """

        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date' : date})
        self.assertTrue(form.is_valid())

    def test_renew_book_is_max(self):

        """
        Test for invalid form if renewal date for books is reach to 4 weeks
        """

        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date' : date})
        self.assertTrue(form.is_valid())
