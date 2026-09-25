from django import forms

class ComputerItemForm(forms.Form):
    # Zadanie 9: Pole z widgetem posiadającym klasę CSS 'wide'
    name = forms.CharField(
        max_length=100,
        min_length=3,
        label="Nazwa sprzętu",
        widget=forms.TextInput(attrs={"class": "wide"})
    )
    price = forms.DecimalField(max_digits=8, decimal_places=2, min_value=0, label="Cena (PLN)")
    promo_price = forms.DecimalField(max_digits=8, decimal_places=2, required=False, label="Cena promocyjna")
    category = forms.ChoiceField(
        choices=[
            ('laptop', 'Laptop'),
            ('desktop', 'Komputer Stacjonarny'),
            ('parts', 'Części komputerowe')
        ],
        label="Kategoria"
    )
    is_available = forms.BooleanField(required=False, label="Dostępny na stanie")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Opis")

    # Zadanie 6: clean_<pole> - nazwa nie może być "test"
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and name.lower() == 'test':
            raise forms.ValidationError("Nazwa produktu nie może brzmieć 'test'!")
        return name

    # Zadanie 6: clean() - walidacja wielopolowa (cena promo < cena podstawowa)
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        promo_price = cleaned_data.get('promo_price')

        if price and promo_price and promo_price >= price:
            raise forms.ValidationError("Cena promocyjna musi być niższa od ceny podstawowej!")
        return cleaned_data

# Zadanie 8: SearchForm
class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="Szukaj")
    in_stock = forms.BooleanField(required=False, label="Tylko dostępne")