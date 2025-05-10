# Equipment and item handling functions for Red Dragon Rising

import json

def load_items():
    """Loads item data from JSON."""
    with open("assets/items.json", "r") as file:
        return json.load(file)

def get_item_stat(item_id, category, stat):
    """Retrieves a specific stat (name, attack, cost, etc.) for an item."""
    items = load_items()
    return items[category].get(str(item_id), {}).get(stat, "Unknown Stat")

def get_item_info(item_id, category):
    """Retrieves all stats for an item."""
    items = load_items()
    return items[category].get(str(item_id), {})
