from django import forms  
from p_library.models import UserProfile  
  
  
class ProfileCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = ['age']