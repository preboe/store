from django import forms
from django.contrib.auth.models import User

# from .models import Order


class OrderForm(forms.ModelForm):

    pass

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['order_date'].lebel = 'Дата получения заказа'
    #
    # order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    #
    # class Meta:
    #
    #     model = Order
    #     fields = {
    #         'first_name', 'last_name'
    #     }



class LoginForm(forms.ModelForm):
     pass

#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['passrowr'].label = 'Пароль'
#
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе')
#         user = User.objects.filter(username=username).first()
#         if user:
#             if not user.chec_password(password):
#                 raise forms.ValidationError("Не верный пароль")
#         return self.cleaned_data


































