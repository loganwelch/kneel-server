import sqlite3
import json
from models import Order, Metal, Size, Style

ORDERS = [
    {
        "metal_id": 2,
        "size_id": 5,
        "style_id": 2,
        "id": 1
    },
    {
        "metal_id": 1,
        "size_id": 4,
        "style_id": 3,
        "id": 2
    },
    {
        "metal_id": 4,
        "size_id": 1,
        "style_id": 3,
        "id": 3
    },
    {
        "metal_id": 4,
        "size_id": 3,
        "style_id": 1,
        "id": 4
    },
    {
        "metal_id": 3,
        "size_id": 2,
        "style_id": 1,
        "id": 5
    },
    {
        "metal_id": 5,
        "size_id": 5,
        "style_id": 3,
        "id": 6
    }
]

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.metal metal_metal,
            m.price metal_price,
            s.carets size_carets,
            s.price size_price,
            st.style style_style,
            st.price style_price
        FROM orders o
        JOIN metals m
            ON m.id = o.metal_id
        JOIN sizes s
            ON s.id = o.size_id
        JOIN styles st
            ON st.id = o.style_id
        """)

        # Initialize an empty list to hold all animal representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])
            
            # Create a Location instance from the current row
            metal = Metal(row['id'], row['metal_metal'], row['metal_price'])

            # Create a Customer instance from the current row
            size = Size(row['id'], row['size_carets'], row['size_price'])

            # Create a Customer instance from the current row
            style = Style(row['id'], row['style_style'], row['style_price'])

            # Add the dictionary representation of the location to the animal
            order.metal = metal.__dict__

            # Add the dictionary representation of the customer to the animal
            order.size = size.__dict__

            # Add the dictionary representation of the customer to the animal
            order.style = style.__dict__

            # Add the dictionary representation of the animal to the list
            orders.append(order.__dict__)

    return orders



# Function with a single parameter


def get_single_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.metal metal_metal,
            m.price metal_price,
            s.carets size_carets,
            s.price size_price,
            st.style style_style,
            st.price style_price
        FROM orders o
        JOIN metals m
            ON m.id = o.metal_id
        JOIN sizes s
            ON s.id = o.size_id
        JOIN styles st
            ON st.id = o.style_id
        WHERE o.id = ?
        """, (id, ))

        #animals = []

        # Load the single result into memory
        data = db_cursor.fetchone()
        if data:
        # Create an animal instance from the current row
            order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'])
            metal = Metal(data['id'], data['metal_metal'], data['metal_price'])
            size = Size(data['id'], data['size_carets'], data['size_price'])
            style = Style(data['id'], data['style_style'], data['style_price'])

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__
            return order.__dict__
        else:
            return None


def create_order(new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ?);
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order


def delete_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
