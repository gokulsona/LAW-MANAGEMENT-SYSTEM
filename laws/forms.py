from django import forms
from . models import Cases


class CaseForm(forms.ModelForm):
    class Meta:
        model=Cases
        fields = ['case_title', 'petitioner_name', 'petitioner_phn', 'petitioner_email', 'petitioner_address', 'district', 'court', 'case_date', 'case_description']        
        
        
        labels = {
            'case_title':'Case Title',
            'petitioner_name':'Petitioner Name',
            'petitioner_phn' : 'Petitioner Phone Number',
            'petitioner_email' : 'Petitioner Email',
            'petitioner_address':'Petitioner Address',
            'district':' Select District',
            'court': 'Select Court',
            'case_date':'Select Case Date',
            'case_description':'Case Description'
        }
        
        widgets = {
            'case_title': forms.TextInput(attrs={'placeholder': 'Enter Type of Case'}),
            'petitioner_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'petitioner_phn': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'petitioner_email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'petitioner_address': forms.Textarea(attrs={'placeholder': 'Enter your Address'}),
            'case_date': forms.DateInput(attrs={'type': 'date'}),
            'case_description': forms.Textarea(attrs={'placeholder': 'Case Description'}),
            
        }
        
        
#Edit Case Form
class EditCaseForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ['case_title', 'petitioner_name', 'petitioner_phn', 'petitioner_email', 'petitioner_address', 'district', 'court', 'case_date', 'case_description']        
        
        labels = {
            'case_title':'Case Title',
            'petitioner_name':'Petitioner Name',
            
            'petitioner_phn' : 'Petitioner Phone Number',
            'petitioner_email' : 'Petitioner Email',
            'petitioner_address':'Petitioner Address',
            'district':' Select District',
            'court': 'Select Court',
            'case_date':'Select Case Date',
            'case_description':'Case Description'
        }
        
        widgets = {
            'case_title': forms.TextInput(attrs={'placeholder': 'Enter Type of Case'}),
            'petitioner_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'petitioner_phn': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'petitioner_email': forms.EmailInput(attrs={'placeholder': 'Enter your Email'}),
            'petitioner_address': forms.Textarea(attrs={'placeholder': 'Enter your Address'}),
            'case_date': forms.DateInput(attrs={'type': 'date'}),
            'case_description': forms.Textarea(attrs={'placeholder': 'Case Description'}),
            
        }