from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import filter as filter_module
import pagination as pagination_module


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data.json":
            # Check if there are active filters
            if os.path.exists("current_filters.json"):
                with open("current_filters.json", "r") as f:
                    filters = json.load(f)

                # Load all products
                all_products = filter_module.load_products("data.json")

                # Apply filters using the filter.py functions
                color = filters.get("color") or None
                brand = filters.get("brand") or None
                on_sale = (
                    filters.get("on_sale")
                    if filters.get("on_sale") is not None
                    else None
                )

                # Parse price range
                price_range = None
                if filters.get("price_range"):
                    price_parts = filters["price_range"].split("-")
                    price_range = (float(price_parts[0]), float(price_parts[1]))

                # Apply the filters
                filtered_products = filter_module.apply_filters(
                    all_products,
                    color=color,
                    price_range=price_range,
                    on_sale=on_sale,
                    brand=brand,
                )

                # Apply sorting if specified
                sort_by = filters.get("sort_by")
                if sort_by == "price_high_to_low":
                    filtered_products = filter_module.sort_by_price_high_to_low(
                        filtered_products
                    )
                elif sort_by == "price_low_to_high":
                    filtered_products = filter_module.sort_by_price_low_to_high(
                        filtered_products
                    )
                elif sort_by == "popularity":
                    filtered_products = filter_module.sort_by_popularity(
                        filtered_products
                    )

                # Convert filtered products back to JSONL format
                data = "\n".join([json.dumps(product) for product in filtered_products])
            else:
                # No filters, return all data
                with open("data.json", "r") as f:
                    data = f.read()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode())
        elif self.path.startswith("/api/products"):
            # Handle paginated product requests
            # Parse query parameters for page number
            from urllib.parse import urlparse, parse_qs

            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)

            # Get page number from query params (default to 1)
            page_number = int(query_params.get("page", [1])[0])
            items_per_page = int(query_params.get("items_per_page", [50])[0])

            # Load and filter products (same logic as /data.json)
            if os.path.exists("current_filters.json"):
                with open("current_filters.json", "r") as f:
                    filters = json.load(f)

                # Load all products
                all_products = filter_module.load_products("data.json")

                # Apply filters
                color = filters.get("color") or None
                brand = filters.get("brand") or None
                on_sale = (
                    filters.get("on_sale")
                    if filters.get("on_sale") is not None
                    else None
                )

                # Parse price range
                price_range = None
                if filters.get("price_range"):
                    price_parts = filters["price_range"].split("-")
                    price_range = (float(price_parts[0]), float(price_parts[1]))

                # Apply the filters
                filtered_products = filter_module.apply_filters(
                    all_products,
                    color=color,
                    price_range=price_range,
                    on_sale=on_sale,
                    brand=brand,
                )

                # Apply sorting if specified
                sort_by = filters.get("sort_by")
                if sort_by == "price_high_to_low":
                    filtered_products = filter_module.sort_by_price_high_to_low(
                        filtered_products
                    )
                elif sort_by == "price_low_to_high":
                    filtered_products = filter_module.sort_by_price_low_to_high(
                        filtered_products
                    )
                elif sort_by == "popularity":
                    filtered_products = filter_module.sort_by_popularity(
                        filtered_products
                    )
            else:
                # No filters, load all products
                filtered_products = filter_module.load_products("data.json")

            # Apply pagination using pagination.py functions
            page_data = pagination_module.get_page_data(
                filtered_products, page_number, items_per_page
            )
            pagination_info = pagination_module.create_pagination_info(
                filtered_products, page_number, items_per_page
            )

            # Create response with both products and pagination info
            response_data = {"products": page_data, "pagination": pagination_info}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/set-filters":
            # Read the filter data from the request
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            filters = json.loads(post_data.decode())

            # Save filters to a JSON file
            with open("current_filters.json", "w") as f:
                json.dump(filters, f)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode())
        elif self.path == "/api/clear-filters":
            # Remove the filters file
            if os.path.exists("current_filters.json"):
                os.remove("current_filters.json")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode())
        else:
            self.send_response(404)
            self.end_headers()


server_address = ("", 8000)
httpd = HTTPServer(server_address, Handler)
print("Serving on http://localhost:8000")
httpd.serve_forever()
