from django.shortcuts import render, redirect
from .forms import ComputerItemForm, SearchForm

# Zadanie 2: Słownik z 5 elementami
ITEMS = [
    {"id": 1, "name": "Laptop Dell XPS 15", "price": 7500.00, "category": "Laptop", "is_available": True},
    {"id": 2, "name": "Komputer Gaming Pro", "price": 5200.00, "category": "Desktop", "is_available": True},
    {"id": 3, "name": "Procesor Intel i7", "price": 1400.00, "category": "Części", "is_available": False},
    {"id": 4, "name": "Karta RTX 4070", "price": 2900.00, "category": "Części", "is_available": True},
    {"id": 5, "name": "Stary Monitor LCD", "price": 150.00, "category": "Inne", "is_available": False},
]

def index(request):
    return render(request, 'shop/index.html')

def item_list(request):
    search_form = SearchForm(request.GET)
    filtered_items = ITEMS

    if search_form.is_valid():
        query = search_form.cleaned_data.get('q')
        in_stock = search_form.cleaned_data.get('in_stock')

        if query:
            filtered_items = [i for i in filtered_items if query.lower() in i['name'].lower()]
        if in_stock:
            filtered_items = [i for i in filtered_items if i['is_available']]

    return render(request, 'shop/item_list.html', {
        'items': filtered_items,
        'search_form': search_form
    })

def item_detail(request, item_id):
    item = next((item for item in ITEMS if item["id"] == item_id), None)
    return render(request, 'shop/item_detail.html', {'item': item})

def item_add(request):
    if request.method == 'POST':
        form = ComputerItemForm(request.POST)
        if form.is_valid():
            return redirect('shop:item_list')
    else:
        form = ComputerItemForm()

    return render(request, 'shop/item_form.html', {'form': form})