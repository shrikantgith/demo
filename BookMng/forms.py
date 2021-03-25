from django import forms
from .models import Seller
Userch= [
    ('Buyer', 'Buyer'),
    ('Seller', 'Seller'),]
class BuyerRegistration(forms.ModelForm):
    class Meta:
        model = Seller
        fields  ='__all__'
        widgets={'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
                 'usertype':forms.Select(attrs={'class':'form-control','placeholder':'Select'},choices=Userch),
                 'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
                 }
    def clean(self):
        super(BuyerRegistration, self).clean()
        email = self.cleaned_data['email']
        if len(email)< 50:
            self._errors['email']= self.error_class(['Pls give valid email'])
        return self.cleaned_data

