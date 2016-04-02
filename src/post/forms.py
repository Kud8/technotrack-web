# -*- coding: utf-8 -*-

from django import forms
from .models import Post

class QuestionListForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('pub_date', u'Дата создания')), required=False)

    def clean_search(self):
        search = self.cleaned_data.get('search')
        return search


class QuesForm(forms.Form):

    title = forms.CharField(max_length=140)
    text = forms.CharField(widget=forms.Textarea)
