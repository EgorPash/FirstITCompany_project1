from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        type = cleaned_data.get("type")

        if category and type and category.type != type:
            raise forms.ValidationError("Категория не соответствует типу.")

        subcategory = cleaned_data.get("subcategory")
        if subcategory and subcategory.category != category:
            raise forms.ValidationError("Подкатегория не соответствует категории.")

