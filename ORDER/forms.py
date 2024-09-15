# from django import forms
# from .models import Order,Order2

# class Order_form(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['resume_type', 'deadline','price_quote']
# class Order_form2(forms.ModelForm):
#     class Meta:
#         model = Order2
#         fields = [
#             'firstname', 'lastname', 'email', 'phone_number', 'gender',
#             'title', 'number_of_pages', 'deadline', 'abstract',
#             'description', 'accept_terms'
#         ]
#         widgets = {
#             'firstname': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
#             'lastname': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
#             'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
#             'gender': forms.RadioSelect,
#             'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
#             'number_of_pages': forms.NumberInput(attrs={'placeholder': 'Number of Pages', 'class': 'form-control'}),
#             'deadline': forms.DateInput(attrs={'placeholder': 'Deadline', 'class': 'form-control'}),
#             'abstract': forms.ClearableFileInput(attrs={'placeholder': 'Abstract', 'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'placeholder': 'Your message here!', 'class': 'form-control', 'style': 'height: 99px;'}),
#             'accept_terms': forms.CheckboxInput(attrs={'class': 'form-control'})
#         }