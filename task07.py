cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
for i in cart:
    cart[i]['total_price'] = cart[i]['price'] * cart[i]['quantity']
umumiy_narx = sum(map(lambda x: x['total_price'], cart.values()))
print(umumiy_narx)