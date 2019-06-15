from django import forms

class userFormRegister(forms.Form):
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'First name'}),label='')
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Last name'}),label='')
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Username'}),label='')
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Email'}),label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Password'}),label='')

class userFormLogin(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Username'}),label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Password'}),label='')


class MessageContact(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Name'}),label='')
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Email'}),label='')
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Subject'}),label='')
    msg = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': "form-control rounded-0 py-3 pl-5 font-13 sign-register-input", 'placeholder': 'Message'}),label='')


class userPos(forms.Form):
    lat = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 'lat', 'type' : 'hidden'}))
    lon = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 'lon', 'type' : 'hidden'}))

class CommentaireForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control form-control rounded-0 p-3", 'placeholder': 'Name'}),label='')
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control form-control rounded-0 p-3", 'placeholder': 'Email'}),label='')
    msg = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': "form-control form-control rounded-0 p-3", 'placeholder': 'Comment'}),label='')