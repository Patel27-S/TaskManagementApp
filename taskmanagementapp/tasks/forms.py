from django import forms

class AddTask(forms.Form):
    task = forms.CharField(label="New Task" , max_length = 150)
   