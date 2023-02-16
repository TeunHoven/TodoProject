from django import forms

class AddTodoForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.Textarea(attrs={'size': 10, 'class': 'form-control', 'placeholder': 'Todo Name'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description'}))
    date_finished = forms.DateTimeField(label='Deadline', widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': '25/06/2023'}))

# TODO add user to list (automatically)
class AddTodoListForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.Textarea(attrs={'size': 10, 'class': 'form-control', 'placeholder': 'List Name'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List Description'}))
