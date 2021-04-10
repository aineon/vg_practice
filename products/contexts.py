from products.models import Product

import random


def rand_product_list(request):
    """Generate list of random products"""

    all_products = list(Product.objects.all())
    rand_products = random.sample(all_products, 7)

    context = {
        'rand_products': rand_products,
    }
    return context
