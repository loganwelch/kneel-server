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
    return ORDERS

# Function with a single parameter


def get_single_order(id):
    # Variable to hold the found metal, if it exists
    requested_order = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order


def create_order(order):
    # Get the id value of the last animal in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    # Initial -1 value for animal index, in case one isn't found
    order_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
