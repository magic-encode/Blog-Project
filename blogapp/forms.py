from django import forms

from .models import Blog
from .models import Catagory
from .models import Comments


class BlogForm(forms.Form):
    class Meta:
        model = Blog
        fields = '__all__'


class CatagoryForm(forms.Form):
    class Meta:
        model = Catagory
        fields = '__all__'
        

class CommentForm(forms.Form):
    class Meta:
        model = Comments
        fields = '__all__'






