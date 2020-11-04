"""
Zadanie 
"""

shopping_list = {
"piekarnia": ["chleb", "bułki", "pączek"],
"warzywniak": ["marchew", "seler", "rukola"]
}
amount = 0

for shop, product in shopping_list.items():
  products = []
  for item in product:
    products.append(item.capitalize())
    amount = len(item)
  print(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {products}.")

print(f"W sumie kupuję {amount} produktów.")