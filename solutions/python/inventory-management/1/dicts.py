"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = dict()
    for item in items:
        if not inventory.get(item):
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


def add_items(inventory: dict, items: list[str]):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    new_inventory = create_inventory(items)
    for item in inventory.keys():
        if not new_inventory.get(item):
            new_inventory[item] = inventory[item]
        else:
            new_inventory[item] += inventory[item]
    return new_inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if inventory.get(item):
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item):
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    available_items_list = []
    for item in inventory:
        if inventory[item] > 0:
            available_items_list.append((item, inventory[item]))
    return available_items_list
