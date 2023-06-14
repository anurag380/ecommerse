from django import forms
from .models import Customer,Products
import re
from django.contrib.auth import authenticate




class Register(forms.ModelForm):

    con_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Password'}))

    class Meta:
        model = Customer
        fields = ['name','email','phno', 'password']

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':"User Name"}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'E-mail'}),
            'phno' : forms.NumberInput(attrs={'placeholder' : 'Phone No.'}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'}),
            }

    def clean(self):

        super(Register, self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        phno = self.data.get('phno')
        password = self.cleaned_data.get('password')
        con_password = self.cleaned_data.get('con_password')
        

        regpass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"


        # print(phno)
        # if len(self.phno) < 10:
        #     raise forms.ValidationError({"phno" : "Phone number should have 10 numbers"})
        if re.search(regpass, password):
            pass
        else:
            raise forms.ValidationError({'password' : ['Minimum eight characters',
                                                        'at least one uppercase letter',
                                                        'one lowercase letter',
                                                        'one number and one special character']})   
        if password != con_password:
            raise forms.ValidationError({"con_password" : "Passwords are not matched"})
        else:
            pass

# class Loginform(forms.Form):
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'E-mail'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}))
    
    
    # def clean(self):
    #     super(Loginform, self).clean()
    #     email = self.cleaned_data['email']
    #     password = self.cleaned_data['password']
    #     user = authenticate(email = email, password = password)
    #     if user is not None:
    #         pass
    #     else:
    #         raise forms.ValidationError({"password" : "Please check the fields"})


class Productform(forms.ModelForm):  
    class Meta:
        model = Products
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':"Product Name"}),
            'price' : forms.NumberInput(attrs={'placeholder' : 'Product Price'}),
            # 'image' : forms.FileField()
            }



