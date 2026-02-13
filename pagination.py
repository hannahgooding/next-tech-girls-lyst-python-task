"""
Product Pagination Module

This module contains functions to paginate product data.
Students will implement the pagination logic for each function below.
"""

import math


def get_total_pages(products, items_per_page=50):
    """
    Calculate the total number of pages needed to display all products.

    Args:
        products (list): List of product dictionaries
        items_per_page (int): Number of items to display per page (default: 50)

    Returns:
        int: Total number of pages needed

    Example:
        If there are 175 products and items_per_page is 50,
        this should return 4 (pages 1, 2, 3, and 4)

    TODO: Implement this function to calculate total pages.
    Hint: Use the len() function to get the number of products.
    Hint: You may need to use math.ceil() to round up to the nearest whole number.
    """
    # YOUR CODE HERE
    pass


def get_page_data(products, page_number, items_per_page=50):
    """
    Get the products for a specific page.

    Args:
        products (list): List of product dictionaries
        page_number (int): The page number to retrieve (1-indexed, so page 1 is the first page)
        items_per_page (int): Number of items to display per page (default: 50)

    Returns:
        list: List of products for the specified page

    Example:
        If page_number is 1 and items_per_page is 50,
        this should return products 0-49 (the first 50 products).
        If page_number is 2, it should return products 50-99.

    TODO: Implement this function to return the correct slice of products.
    Hint: Use list slicing to get a subset of the products list.
    Hint: Calculate the start_index and end_index based on page_number and items_per_page.
    """
    # YOUR CODE HERE
    pass


def create_pagination_info(products, page_number, items_per_page=50):
    """
    Create a dictionary with pagination information.

    Args:
        products (list): List of product dictionaries
        page_number (int): The current page number (1-indexed)
        items_per_page (int): Number of items to display per page (default: 50)

    Returns:
        dict: Dictionary containing pagination info with keys:
            - 'current_page' (int): The current page number
            - 'total_pages' (int): Total number of pages
            - 'items_per_page' (int): Number of items per page
            - 'total_items' (int): Total number of products
            - 'has_previous' (bool): True if there is a previous page
            - 'has_next' (bool): True if there is a next page
            - 'start_index' (int): Index of first item on current page (0-indexed)
            - 'end_index' (int): Index of last item on current page (0-indexed)

    Example:
        For 175 products, page 2, 50 items per page:
        {
            'current_page': 2,
            'total_pages': 4,
            'items_per_page': 50,
            'total_items': 175,
            'has_previous': True,
            'has_next': True,
            'start_index': 50,
            'end_index': 99
        }

    TODO: Implement this function to return a dictionary with all the pagination info.
    Hint: Use the get_total_pages() function you implemented above.
    Hint: has_previous is True if current_page > 1
    Hint: has_next is True if current_page < total_pages
    """
    # YOUR CODE HERE
    pass
