from django import forms

gender1=[('MALE','male'),('FEMALE','female')]
course1=[('Python','Python'),('Django','django'),('sql','sql')]
class Student(forms.Form):
    name=forms.CharField(max_length=100,label='NAME',label_suffix='first',help_text='name should contain only alphabets')
    age=forms.IntegerField(max_value=70)
    address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput())
    gender=forms.ChoiceField(choices=gender1)
    course=forms.MultipleChoiceField(choices=course1)
    radio=forms.ChoiceField(choices=gender1,widget=forms.RadioSelect)
    checkbox=forms.MultipleChoiceField(choices=course1,widget=forms.CheckboxSelectMultiple)