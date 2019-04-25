from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, UserProfile
from .validators import phone_number_length_validator


# following two forms are created for Admin page's User model. DO NOT CHANGE ANYTHING 😅
class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number',)
        # widgets = {
        #     'phone_number': forms.NumberInput(
        #         attrs={'class': 'input'}
        #     ),
        # }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserRegistrationForm(forms.ModelForm):

    phone_number = forms.CharField(label='Phone number', validators=[phone_number_length_validator],
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'input',
                                           'placeholder': 'ex. 9876543210'
                                       }
                                   ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input',

        }
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={
            'class': 'input',

        }
    ))

    class Meta:
        model = User

        # This will be displayed in the form
        fields = ['phone_number', 'password', 'password2', ]

        widgets = {
            'phone_number': forms.NumberInput(
                attrs={'class': '', 'placeholder': 'ex. 9876543210'}
            ),

        }

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Password does not match')

        return password

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        phone_number_qs = User.objects.filter(phone_number=phone_number)

        if phone_number_qs.exists():
            raise forms.ValidationError('This phone number is already been used. Please Login')

        return phone_number


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label='Phone number',
                                   validators=[phone_number_length_validator],
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'input is-normal',
                                           'placeholder': "ex. 9876543210"
                                       }
                                   ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input',
        }
    ))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        phone_number_qs = User.objects.filter(phone_number=phone_number)

        if not phone_number_qs.exists():
            raise forms.ValidationError('This phone number does not exist. Create one using sign up link')

        return phone_number

    def clean(self, *args, **kwargs):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)

            if not user:
                raise forms.ValidationError("Phone number or Password is Incorrect")

            if not user.is_active:
                raise forms.ValidationError("User is Banned.")

        return super(UserLoginForm, self).clean()


class ProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = UserProfile
        exclude = ['user']

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'input', 'placeholder': 'ex. John'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'input', 'placeholder': 'ex. Snow'}
            ),
            'address': forms.Textarea(
                attrs={'class': 'textarea', 'placeholder': 'your village', 'rows': 5, 'cols': 1}
            )
        }


class ForgetPasswordForm(forms.Form):
    phone_number = forms.IntegerField(label='Phone number', widget=forms.NumberInput(
        attrs={
            'class': 'input is-normal',
            'placeholder': "ex. 9876543210"
        }
    ))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number:
            """
            If phone number exists send the 6 digit OTP or whatever to reset the password
            """

            print('sending otp')
