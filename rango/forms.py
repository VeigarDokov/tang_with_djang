"""Required modules"""
from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, ContactMessage, UserProfile, Portfolio


class CategoryForm(forms.ModelForm):
    """Create categories from website"""
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form
    class Meta:
        """Provide an association between the ModelForm and a model"""
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    """Create page form from website"""
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the Url of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        """Provide an association between the ModelForm and a model"""
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include
        # them.
        # Here, we are hiding the foreign key.
        # we can either exclude the categoy field from the form.
        exclude = ('category',)
        # or specify te fields to include (i.e not include the category field)
        # fields = ('title', 'url', 'views')


class ContactForm(forms.ModelForm):
    """context of contact form"""

    class Meta:
        """Connect with  ContactMessage model"""
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class UserForm(forms.ModelForm):
    """User form with password element"""
    # widget is used to hide password while user is typing
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """visible fields"""
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    """User Profile form"""
    class Meta:
        """visible fields"""
        model = UserProfile
        fields = ('website', 'picture')


class Portfolio(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('btc', 'xmr', 'ape', 'trades')
