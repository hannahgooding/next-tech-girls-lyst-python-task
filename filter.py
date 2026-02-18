"""
Product Filtering Module

This module contains functions to filter product data based on various criteria.
Students will implement the filtering logic for each function below.
"""

import json


def load_products(filename="data.jsonl"):
    """
    Load products from the JSONL data file.

    Args:
        filename (str): Path to the data file (default: "data.jsonl")

    Returns:
        list: List of product dictionaries
    """
    products = []
    with open(filename, "r") as file:
        for line in file:
            products.append(json.loads(line.strip()))
    return products


def filter_by_color(products, color):
    products = load_products()
    colourFiltered = []
    for product in products:
        if product ["color"] == color:
            colourFiltered.append(product)
    return colourFiltered
    """
    Filter products by a specific color.

    Args:
        products (list): List of product dictionaries
        color (str): The color to filter by (e.g., "red", "blue", "black")

    Returns:
        list: Filtered list of products matching the specified color

    TODO: Implement this function to return only products that match the given color.
    Hint: Each product has a 'color' field you can check.
    """
    # YOUR CODE HERE
    pass


def filter_by_price_range(products, min_price, max_price):
    products = load_products()
    priceFiltered = []
    for product in products:
        if product ["regular_price"] >= min_price and product ["regular_price"] <= max_price:
            if product ["on_sale"] == True:
                if product ["discount_price"] >= min_price and product ["discount_price"] <= max_price:
                    priceFiltered.append(product)

        
    return priceFiltered
    """
    Filter products within a specific price range.

    Args:
        products (list): List of product dictionaries
        min_price (float): Minimum price (inclusive)
        max_price (float): Maximum price (inclusive)

    Returns:
        list: Filtered list of products within the price range

    TODO: Implement this function to return only products within the price range.
    Hint: Consider both 'regular_price' and 'discount_price' fields.
    For items on sale, use the discount_price, otherwise use regular_price.
    """
    # YOUR CODE HERE
    pass


def filter_by_sale_status(products, on_sale=True):
    products = load_products()
    saleFiltered = []
    for product in products:
        if product ["on_sale"] == True:
            saleFiltered.append(product)
    return saleFiltered
    """
    Filter products by their sale status.

    Args:
        products (list): List of product dictionaries
        on_sale (bool): If True, return only products on sale.
                       If False, return only products not on sale.

    Returns:
        list: Filtered list of products matching the sale status

    TODO: Implement this function to return only products that match the sale status.
    Hint: Each product has an 'on_sale' field (True/False).
    """
    # YOUR CODE HERE
    pass


def filter_by_brand(products, brand):
    products = load_products()
    brandFiltered = []
    for product in products:
        if product ["designer"] == brand:
            brandFiltered.append(product)
    return brandFiltered
    """
    Filter products by a specific brand (designer).

    Args:
        products (list): List of product dictionaries
        brand (str): The brand to filter by (e.g., "gucci", "dolce-gabbana")

    Returns:
        list: Filtered list of products from the specified brand

    TODO: Implement this function to return only products from the given brand.
    Hint: Each product has a 'designer' field you can check.
    """
    # YOUR CODE HERE
    pass


def sort_by_price_high_to_low(products):

    """
    Sort products by price from highest to lowest.

    Args:
        products (list): List of product dictionaries

    Returns:
        list: Sorted list of products (highest to lowest price)

    TODO: Implement this function to sort products by price (descending).
    Hint: Use the discount_price if the item is on_sale, otherwise use regular_price.
    You can use Python's sorted() function with a key parameter.
    """
    # YOUR CODE HERE
    pass


def sort_by_price_low_to_high(products):
    for x in products:
        if x["on_sale"]:
            x["price"] = x["discount_price"]
        else:
            x["price"] = x["regular_price"]
    priceSorted = sorted(products, key=lambda x: x["price"], reverse=False)
    return priceSorted
    """
    Sort products by price from lowest to highest.

    Args:
        products (list): List of product dictionaries

    Returns:
        list: Sorted list of products (lowest to highest price)

    TODO: Implement this function to sort products by price (ascending).
    Hint: Use the discount_price if the item is on_sale, otherwise use regular_price.
    You can use Python's sorted() function with a key parameter.
    """
    # YOUR CODE HERE
    pass


def sort_by_popularity(products):
    popularSorted = sorted(products, key=lambda x: x["item_score"], reverse=True)
    return popularSorted
    """
    Sort products by popularity score from highest to lowest.

    Args:
        products (list): List of product dictionaries

    Returns:
        list: Sorted list of products (most popular first)

    TODO: Implement this function to sort products by item_score (descending).
    Hint: Each product has a 'item_score' field.
    You can use Python's sorted() function with a key parameter.
    """
    # YOUR CODE HERE
    pass


def apply_filters(products, color=None, price_range=None, on_sale=None, brand=None):
    """
    Apply multiple filters to the product list.
    This function combines all individual filters.

    Args:
        products (list): List of product dictionaries
        color (str, optional): Color to filter by
        price_range (tuple, optional): Tuple of (min_price, max_price)
        on_sale (bool, optional): Filter by sale status
        brand (str, optional): Brand to filter by

    Returns:
        list: Filtered list of products matching all specified criteria

    TODO: Implement this function to apply multiple filters in combination.
    Hint: Start with all products, then apply each filter one at a time if the
    parameter is provided (not None).
    """
    filtered_products = products

    # YOUR CODE HERE
    # Apply each filter if the parameter is provided
    # Example structure:
    if color is not None:
        filtered_products = filter_by_color(filtered_products, color)
    if price_range is not None:
        filtered_products = filter_by_price_range(filtered_products, price_range[0], price_range[1])
    if on_sale is not None:
        filtered_products = filter_by_sale_status(filtered_products, on_sale)
    if brand is not None:
        filtered_products = filter_by_brand(filtered_products, brand)

    return filtered_products


def save_filtered_results(products, output_filename="filtered_data.jsonl"):
    """
    Save filtered products to a new JSONL file.

    Args:
        products (list): List of product dictionaries to save
        output_filename (str): Path to the output file
    """
    with open(output_filename, "w") as file:
        for product in products:
            file.write(json.dumps(product) + "\n")
    print(f"Saved {len(products)} products to {output_filename}")


# Example usage (for testing your functions)
if __name__ == "__main__":
    # Load all products
    all_products = load_products()
    print(f"Loaded {len(all_products)} products")

    # Example: Test filtering by color
    # Uncomment the lines below once you've implemented the functions

    red_products = filter_by_color(all_products, "red")
    print(f"Found {len(red_products)} red products")

    # Example: Test filtering by price range
    affordable_products = filter_by_price_range(all_products, 0, 100)
    print(f"Found {len(affordable_products)} products under $100")

    # Example: Test filtering by sale status
    sale_products = filter_by_sale_status(all_products, on_sale=True)
    print(f"Found {len(sale_products)} products on sale")

    #Example: Test filtering by brand
    gucci_products = filter_by_brand(all_products, "gucci")
    print(f"Found {len(gucci_products)} Gucci products")

    # Example: Apply multiple filters
    # filtered = apply_filters(
    #     all_products,
    #     color="black",
    #     price_range=(100, 500),
    #     on_sale=True,
    #     brand="gucci"
    # )
    # print(f"Found {len(filtered)} products matching all criteria")

    # Save filtered results
    save_filtered_results(filtered)
