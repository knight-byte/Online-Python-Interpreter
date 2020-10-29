from django import forms

""" 
class NameForm(forms.Form):
    yourName = forms.CharField(label="Your Name", max_length=100)
    body = forms.CharField(widget=forms.Textarea)
 """

""" # Form for the code snippet.
class CodeSnippet(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'code-area'}))
    # userInput = forms.CharField(widget=forms.Textarea)
 """
# Form for taking input from the user (code & input combined)
class UserInput(forms.Form):
    userCode = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'code-area',
        'placeholder': 'Write your code here. Not sure what to do, see our Learn Tab',
        'class': 'coding-area'}),required=True)
    customInput = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'custom-input',
        'placeholder': 'Custom input for the program goes here. Leave blank if no input is needed by the program.',
        'class': 'input-area'}), required=False)
