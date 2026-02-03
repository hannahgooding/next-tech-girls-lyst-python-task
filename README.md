# Next Tech Girls Python Task

In this repository you will find a small application that replicates the core tech of the Lyst product feed. This is your chance to get hands-on experience with real developer tasks, focusing on Python logic, data, and building features for our customers. Think of this as building a mini-Lyst!

We have set up some boilerplate code, with a basic python module that serves a HTML file. If you run the program you will see a webpage that shows a feed of fashion products. You will be building some backend functionality that will update what products you see on the webpage.


## Setup Instructions

### 1. Create a Virtual Environment

First, create a virtual environment to isolate the project dependencies:

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the project dependencies including pytest for running tests:

```bash
pip install -r requirements.txt
```

## How to Run the Program

In your Terminal, run:

```bash
python server.py
```

Then open your browser and navigate to:
```
http://localhost:8000
```

You should see a webpage displaying fashion products!

## Your Tasks

You will be implementing filtering and pagination functionality in Python. The webpage is already set up to use your Python code - you just need to complete the functions!

### Task 1: Implement Product Filters (filter.py)

Open `filter.py` and implement the following functions. Each function has detailed documentation explaining what it should do:

#### 1. `filter_by_color(products, color)`
Filter products to show only items of a specific color (e.g., "red", "blue", "black").

#### 2. `filter_by_price_range(products, min_price, max_price)`
Filter products to show only items within a price range.

#### 3. `filter_by_sale_status(products, on_sale=True)`
Filter products to show only items that are on sale (or not on sale).

#### 4. `filter_by_brand(products, brand)`
Filter products to show only items from a specific brand/designer (e.g., "gucci", "prada").

#### 5. `sort_by_price_high_to_low(products)`
Sort products by price from highest to lowest.

#### 6. `sort_by_price_low_to_high(products)`
Sort products by price from lowest to highest.

#### 7. `sort_by_popularity(products)`
Sort products by popularity score from highest to lowest.

#### 8. `apply_filters(products, color=None, price_range=None, on_sale=None, brand=None)`
Combine multiple filters together. This is the main function that gets called by the web application.


### Task 2: Implement Pagination (pagination.py) - OPTIONAL CHALLENGE

Open `pagination.py` and implement the following functions:

#### 1. `get_total_pages(products, items_per_page=50)`
Calculate how many pages are needed to display all products.

**Example:** 175 products ÷ 50 per page = 4 pages

#### 2. `get_page_data(products, page_number, items_per_page=50)`
Get the products for a specific page using list slicing.

**Example:** Page 1 returns products 0-49, Page 2 returns products 50-99

#### 3. `create_pagination_info(products, page_number, items_per_page=50)`
Create a dictionary with all pagination information (current page, total pages, has next/previous, etc.)

**Note:** These functions already have working starter code, but you can try to implement them yourself as a challenge!


## Testing Your Code

### Manual Testing

1. Start the server: `python server.py`
2. Open http://localhost:8000 in your browser
3. Try the filter controls:
   - Select a color from the dropdown
   - Choose a price range
   - Check "On Sale Only"
   - Select a brand
   - Try different sorting options
   - Click "Apply Filters" to see your Python code in action!

### Automated Testing

Run the test suite to check your implementations:

```bash
python -m pytest test_filter.py -v
```

This will run automated tests for each function. Green = passing, Red = needs work!

### Debug Mode

You can also test individual functions by running:

```bash
python filter.py
```

Uncomment the example code at the bottom of `filter.py` to test your functions directly.

## Tips for Success

1. **Read the documentation** - Each function has detailed docstrings explaining what it should do
2. **Start simple** - Begin with `filter_by_color` and work your way up
3. **Use the hints** - Each function includes hints to guide you
4. **Test frequently** - Run the tests after implementing each function
5. **Ask questions** - Don't be afraid to ask for help!

## Understanding the Data

Each product in `data.json` is a dictionary with these fields:

```python
{
    "designer": "gucci",           # Brand name (lowercase with hyphens)
    "color": "black",              # Color of the item
    "regular_price": 750.00,       # Original price
    "discount_price": 600.00,      # Sale price (if on_sale is True)
    "on_sale": True,               # Whether item is on sale
    "popularity_score": 0.85,      # Popularity rating (0-1)
    "category": "bags",            # Product category
    "short_description": "...",    # Description
    "image_url": "...",           # Product image
    "retailer": "..."             # Where it's sold
}
```

## Project Structure

```
├── server.py           # Web server (handles HTTP requests)
├── filter.py          # YOUR CODE HERE - filtering functions
├── pagination.py      # YOUR CODE HERE - pagination functions (optional)
├── test_filter.py     # Automated tests
├── data.json          # Product data (JSONL format)
├── index.html         # Frontend webpage
├── styles.css         # Styling
└── README.md          # This file
```

Good luck and have fun coding! 🚀


