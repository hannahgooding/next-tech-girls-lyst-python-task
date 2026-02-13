"""
Test suite for product filtering functions.

This module contains pytest tests for all filtering functions in the filter.py module.
"""

import pytest
import json
from filter import (
    load_products,
    filter_by_color,
    filter_by_price_range,
    filter_by_sale_status,
    filter_by_brand,
    apply_filters,
    save_filtered_results,
    sort_by_price_high_to_low,
    sort_by_price_low_to_high,
    sort_by_popularity,
)


@pytest.fixture
def all_products():
    """Fixture to load all products from data.jsonl"""
    return load_products()


@pytest.fixture
def sample_products():
    """Fixture with a small sample of products for testing"""
    return [
        {
            "product_id": 1,
            "color": "red",
            "designer": "gucci",
            "on_sale": True,
            "regular_price": 500.0,
            "discount_price": 250.0,
            "popularity_score": 2.5,
        },
        {
            "product_id": 2,
            "color": "black",
            "designer": "gucci",
            "on_sale": True,
            "regular_price": 800.0,
            "discount_price": 400.0,
            "popularity_score": 3.8,
        },
        {
            "product_id": 3,
            "color": "black",
            "designer": "dolce-gabbana",
            "on_sale": False,
            "regular_price": 150.0,
            "discount_price": 150.0,
            "popularity_score": 1.2,
        },
        {
            "product_id": 4,
            "color": "blue",
            "designer": "gucci",
            "on_sale": False,
            "regular_price": 50.0,
            "discount_price": 50.0,
            "popularity_score": 4.5,
        },
    ]


class TestFilterByColor:
    """Tests for the filter_by_color function"""

    def test_filter_by_color_red(self, all_products):
        """Test filtering products by red color"""
        red_products = filter_by_color(all_products, "red")
        assert isinstance(red_products, list)
        # All filtered products should have the color "red"
        assert all(product.get("color") == "red" for product in red_products)

    def test_filter_by_color_black(self, sample_products):
        """Test filtering by black color with sample data"""
        black_products = filter_by_color(sample_products, "black")
        assert len(black_products) == 2
        assert all(product["color"] == "black" for product in black_products)

    def test_filter_by_color_empty_result(self, sample_products):
        """Test filtering by a color that doesn't exist"""
        purple_products = filter_by_color(sample_products, "purple")
        assert len(purple_products) == 0


class TestFilterByPriceRange:
    """Tests for the filter_by_price_range function"""

    def test_filter_by_price_range_affordable(self, all_products):
        """Test filtering products under $100"""
        affordable_products = filter_by_price_range(all_products, 0, 100)
        assert isinstance(affordable_products, list)
        # All products should be within the price range
        for product in affordable_products:
            price = (
                product.get("discount_price")
                if product.get("on_sale")
                else product.get("regular_price")
            )
            assert 0 <= price <= 100

    def test_filter_by_price_range_mid_range(self, sample_products):
        """Test filtering by mid-range prices"""
        mid_range = filter_by_price_range(sample_products, 100, 500)
        assert len(mid_range) == 3  # Products with prices 150, 250, and 400 (discount)
        for product in mid_range:
            price = (
                product["discount_price"]
                if product["on_sale"]
                else product["regular_price"]
            )
            assert 100 <= price <= 500

    def test_filter_by_price_range_on_sale(self, sample_products):
        """Test that sale items use discount_price"""
        # Product 1: on_sale=True, discount_price=250
        result = filter_by_price_range(sample_products, 240, 260)
        assert len(result) == 1
        assert result[0]["product_id"] == 1


class TestFilterBySaleStatus:
    """Tests for the filter_by_sale_status function"""

    def test_filter_by_sale_status_on_sale(self, all_products):
        """Test filtering products that are on sale"""
        sale_products = filter_by_sale_status(all_products, on_sale=True)
        assert isinstance(sale_products, list)
        assert all(product.get("on_sale") is True for product in sale_products)

    def test_filter_by_sale_status_not_on_sale(self, sample_products):
        """Test filtering products that are not on sale"""
        regular_products = filter_by_sale_status(sample_products, on_sale=False)
        assert len(regular_products) == 2
        assert all(product["on_sale"] is False for product in regular_products)

    def test_filter_by_sale_status_default(self, sample_products):
        """Test that default parameter filters for on_sale=True"""
        sale_products = filter_by_sale_status(sample_products)
        assert all(product["on_sale"] is True for product in sale_products)


class TestFilterByBrand:
    """Tests for the filter_by_brand function"""

    def test_filter_by_brand_gucci(self, all_products):
        """Test filtering Gucci products"""
        gucci_products = filter_by_brand(all_products, "gucci")
        assert isinstance(gucci_products, list)
        assert all(product.get("designer") == "gucci" for product in gucci_products)

    def test_filter_by_brand_dolce_gabbana(self, sample_products):
        """Test filtering Dolce & Gabbana products"""
        dg_products = filter_by_brand(sample_products, "dolce-gabbana")
        assert len(dg_products) == 1
        assert dg_products[0]["designer"] == "dolce-gabbana"

    def test_filter_by_brand_not_found(self, sample_products):
        """Test filtering by a brand that doesn't exist"""
        result = filter_by_brand(sample_products, "prada")
        assert len(result) == 0


class TestApplyFilters:
    """Tests for the apply_filters function"""

    def test_apply_filters_single_color(self, sample_products):
        """Test applying only color filter"""
        filtered = apply_filters(sample_products, color="black")
        assert len(filtered) == 2
        assert all(product["color"] == "black" for product in filtered)

    def test_apply_filters_multiple_criteria(self, all_products):
        """Test applying multiple filters: black, $100-500, on sale, Gucci"""
        filtered = apply_filters(
            all_products,
            color="black",
            price_range=(100, 500),
            on_sale=True,
            brand="gucci",
        )
        assert isinstance(filtered, list)
        # All products should match all criteria
        for product in filtered:
            assert product.get("color") == "black"
            assert product.get("designer") == "gucci"
            assert product.get("on_sale") is True
            price = product.get("discount_price")
            assert 100 <= price <= 500

    def test_apply_filters_no_filters(self, sample_products):
        """Test that no filters returns all products"""
        filtered = apply_filters(sample_products)
        assert len(filtered) == len(sample_products)

    def test_apply_filters_price_range_only(self, sample_products):
        """Test applying only price range filter"""
        filtered = apply_filters(sample_products, price_range=(0, 100))
        assert len(filtered) == 1
        assert filtered[0]["product_id"] == 4

    def test_apply_filters_brand_and_sale(self, sample_products):
        """Test applying brand and sale status filters"""
        filtered = apply_filters(sample_products, brand="gucci", on_sale=True)
        assert len(filtered) == 2
        assert all(
            product["designer"] == "gucci" and product["on_sale"]
            for product in filtered
        )


class TestIntegration:
    """Integration tests combining multiple operations"""

    def test_full_workflow(self, all_products, tmp_path):
        """Test a complete filtering workflow"""
        # Load products (already done via fixture)
        assert len(all_products) > 0

        # Apply multiple filters
        filtered = apply_filters(all_products, color="blue", on_sale=True)

        # Save results
        output_file = tmp_path / "integration_test.json"
        save_filtered_results(filtered, str(output_file))

        # Verify saved file
        assert output_file.exists()

        # Load and verify saved data
        with open(output_file, "r") as f:
            saved_products = [json.loads(line.strip()) for line in f]
            assert len(saved_products) == len(filtered)
            assert all(p["color"] == "blue" and p["on_sale"] for p in saved_products)


class TestSortByPriceHighToLow:
    """Tests for the sort_by_price_high_to_low function"""

    def test_sort_by_price_high_to_low_basic(self, sample_products):
        """Test sorting products by price from highest to lowest"""
        sorted_products = sort_by_price_high_to_low(sample_products)
        assert isinstance(sorted_products, list)
        assert len(sorted_products) == 4

        # Expected order based on actual prices (discount if on_sale, else regular):
        # Product 2: 400 (on_sale, discount_price)
        # Product 1: 250 (on_sale, discount_price)
        # Product 3: 150 (not on_sale, regular_price)
        # Product 4: 50 (not on_sale, regular_price)
        assert sorted_products[0]["product_id"] == 2
        assert sorted_products[1]["product_id"] == 1
        assert sorted_products[2]["product_id"] == 3
        assert sorted_products[3]["product_id"] == 4

    def test_sort_by_price_high_to_low_uses_discount_price(self, sample_products):
        """Test that sorting uses discount_price for items on sale"""
        sorted_products = sort_by_price_high_to_low(sample_products)
        # First item should be product 2 with discount_price 400
        assert sorted_products[0]["on_sale"] is True
        assert sorted_products[0]["discount_price"] == 400.0

    def test_sort_by_price_high_to_low_empty_list(self):
        """Test sorting an empty list"""
        sorted_products = sort_by_price_high_to_low([])
        assert sorted_products == []

    def test_sort_by_price_high_to_low_with_all_products(self, all_products):
        """Test sorting with the full product dataset"""
        sorted_products = sort_by_price_high_to_low(all_products)
        assert len(sorted_products) == len(all_products)

        # Verify descending order
        prices = []
        for product in sorted_products:
            price = (
                product["discount_price"]
                if product["on_sale"]
                else product["regular_price"]
            )
            prices.append(price)

        # Check that prices are in descending order
        assert prices == sorted(prices, reverse=True)


class TestSortByPriceLowToHigh:
    """Tests for the sort_by_price_low_to_high function"""

    def test_sort_by_price_low_to_high_basic(self, sample_products):
        """Test sorting products by price from lowest to highest"""
        sorted_products = sort_by_price_low_to_high(sample_products)
        assert isinstance(sorted_products, list)
        assert len(sorted_products) == 4

        # Expected order (ascending prices):
        # Product 4: 50
        # Product 3: 150
        # Product 1: 250
        # Product 2: 400
        assert sorted_products[0]["product_id"] == 4
        assert sorted_products[1]["product_id"] == 3
        assert sorted_products[2]["product_id"] == 1
        assert sorted_products[3]["product_id"] == 2

    def test_sort_by_price_low_to_high_uses_discount_price(self, sample_products):
        """Test that sorting uses discount_price for items on sale"""
        sorted_products = sort_by_price_low_to_high(sample_products)
        # Last item should be product 2 with discount_price 400
        assert sorted_products[-1]["on_sale"] is True
        assert sorted_products[-1]["discount_price"] == 400.0

    def test_sort_by_price_low_to_high_empty_list(self):
        """Test sorting an empty list"""
        sorted_products = sort_by_price_low_to_high([])
        assert sorted_products == []

    def test_sort_by_price_low_to_high_with_all_products(self, all_products):
        """Test sorting with the full product dataset"""
        sorted_products = sort_by_price_low_to_high(all_products)
        assert len(sorted_products) == len(all_products)

        # Verify ascending order
        prices = []
        for product in sorted_products:
            price = (
                product["discount_price"]
                if product["on_sale"]
                else product["regular_price"]
            )
            prices.append(price)

        # Check that prices are in ascending order
        assert prices == sorted(prices)


class TestSortByPopularity:
    """Tests for the sort_by_popularity function"""

    def test_sort_by_popularity_basic(self, sample_products):
        """Test sorting products by popularity score"""
        sorted_products = sort_by_popularity(sample_products)
        assert isinstance(sorted_products, list)
        assert len(sorted_products) == 4

        # Expected order (descending popularity_score):
        # Product 4: 4.5
        # Product 2: 3.8
        # Product 1: 2.5
        # Product 3: 1.2
        assert sorted_products[0]["product_id"] == 4
        assert sorted_products[1]["product_id"] == 2
        assert sorted_products[2]["product_id"] == 1
        assert sorted_products[3]["product_id"] == 3

    def test_sort_by_popularity_scores(self, sample_products):
        """Test that popularity scores are in descending order"""
        sorted_products = sort_by_popularity(sample_products)
        scores = [p["popularity_score"] for p in sorted_products]
        assert scores == [4.5, 3.8, 2.5, 1.2]

    def test_sort_by_popularity_empty_list(self):
        """Test sorting an empty list"""
        sorted_products = sort_by_popularity([])
        assert sorted_products == []

    def test_sort_by_popularity_with_all_products(self, all_products):
        """Test sorting with the full product dataset"""
        sorted_products = sort_by_popularity(all_products)
        assert len(sorted_products) == len(all_products)

        # Verify descending order
        scores = [p["popularity_score"] for p in sorted_products]
        assert scores == sorted(scores, reverse=True)

    def test_sort_by_popularity_most_popular_first(self, sample_products):
        """Test that the most popular product is first"""
        sorted_products = sort_by_popularity(sample_products)
        # Product 4 has the highest popularity_score (4.5)
        assert sorted_products[0]["popularity_score"] == 4.5
        assert sorted_products[0]["product_id"] == 4
