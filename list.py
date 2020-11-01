"""
Zadanie 
"""

shopping_list = {
"piekarnia": ["chleb", "bułki", "pączek"],
"warzywniak": ["marchew", "seler", "rukola"]
}
products = []
amount = 0

for shop, product in shopping_list.items():
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {product}.")