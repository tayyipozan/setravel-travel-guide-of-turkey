from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'floatingInput',
        }))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control pwd',
            'placeholder': 'Password',
            'id': 'floatingPassword',
        }))


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'id': 'floatingInput',
        }))

    last_name = forms.CharField(max_length=50, label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'id': 'floatingInput',
        }))

    email = forms.EmailField(max_length=50, label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'id': 'floatingInput',
        }))

    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'floatingInput',
        }))

    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control pwd',
            'placeholder': 'Password',
            'id': 'floatingPassword',
        }))

    question = forms.CharField(max_length=50, label='Soru', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Soru',
            'id': 'floatingInput',
        }))

    answer = forms.CharField(max_length=50, label='Cevap', widget=forms.TextInput(
        attrs={
            'class': 'form-control pwd',
            'placeholder': 'Cevap',
            'id': 'floatingInput',
        }))


class UserInformationForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            'id': 'floatingInput',
        }))

    last_name = forms.CharField(max_length=50, label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            'id': 'floatingInput',
        }))

    email = forms.EmailField(max_length=50, label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'id': 'floatingInput',
        }))


class ChangePasswordForm(forms.Form):
    resquestion = forms.CharField(max_length=50, label='Your Question', disabled=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
        }))
    resanswer = forms.CharField(max_length=50, label='Answer', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Answer',
            'id': 'floatingPassword',
        }))
    newpassword = forms.CharField(max_length=50, label='New Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'newpassword',
            'id': 'floatingPassword',
        }))
    renewpassword = forms.CharField(max_length=50, label='New Password Again', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'renewpassword',
            'id': 'floatingPassword',
        }))
