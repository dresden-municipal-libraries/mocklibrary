import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create forms here

class RenewBookForm(forms.Form):

    """
    Class for Library Administrator to Renew the Books
    """

    renewal_date = forms.DateField(help_text='Enter a Date Between Now until 4 Weeks')

    def clean_renewal_date_books(self):
        data = self.cleaned_data['cleaned_data']

        """
        Conditional statements given by =
        :check date for renew a book if it is not in past:
        :check date for renew a book between 4 weeks:
        :check date for library admin can change date between 4 weeks:
        :return cleaned data:
        """

        if data < datetime.date.today():
            raise ValidationError(_('Invalid Date'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid Date (Date More Than 4 Weeks)'))
        return data
