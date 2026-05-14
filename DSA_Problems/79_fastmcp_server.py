from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import Dict, List

# Initialize MCP server
mcp = FastMCP("inventory-mcp-server")


# -----------------------------
# Models
# -----------------------------

class Settings(BaseModel):
    app_name: str = "My FastAPI App"
    admin_email: str = "admin@example.com"
    debug: bool = True


class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class HealthStatus(BaseModel):
    status: str = "good"
    message: str = "MCP server is fine"


# -----------------------------
# In-memory DB
# -----------------------------

items_db: Dict[int, Item] = {}

items_list = [
    Item(name="Laptop", description="Gaming laptop", price=1200.0, quantity=5),
    Item(name="Mouse", description="Wireless mouse", price=25.5, quantity=50),
    Item(name="Keyboard", description="Mechanical keyboard", price=75.0, quantity=20),
    Item(name="Monitor", description="24 inch monitor", price=150.0, quantity=15),
    Item(name="Headphones", description="Noise-cancelling headphones", price=200.0, quantity=10),
    Item(name="Webcam", description="HD webcam", price=60.0, quantity=30),
    Item(name="Microphone", description="USB microphone", price=90.0, quantity=25),
    Item(name="Chair", description="Ergonomic office chair", price=300.0, quantity=8),
    Item(name="Desk", description="Standing desk", price=400.0, quantity=6),
    Item(name="USB Hub", description="4-port USB 3.0 hub", price=35.0, quantity=40),
]


# -----------------------------
# MCP Tools
# -----------------------------

@mcp.tool()
def get_config() -> dict:
    """
    Return application configuration settings.
    """

    settings = Settings()

    return settings.model_dump()


@mcp.tool()
def health_check() -> dict:
    """
    Health check for MCP server.
    """

    return HealthStatus().model_dump()


@mcp.tool()
def get_items(skip: int = 0, limit: int = 10) -> List[dict]:
    """
    Return paginated list of items.
    """

    paginated_items = items_list[skip : skip + limit]

    return [item.model_dump() for item in paginated_items]


@mcp.tool()
def get_item(item_id: int) -> dict:
    """
    Retrieve item by ID.
    """

    if item_id not in items_db:
        return {
            "error": "Item not found"
        }

    return items_db[item_id].model_dump()


@mcp.tool()
def create_item(
    item_id: int,
    name: str,
    description: str,
    price: float,
    quantity: int
) -> dict:
    """
    Create a new item.
    """

    if item_id in items_db:
        return {
            "error": "Item ID already exists"
        }

    item = Item(
        name=name,
        description=description,
        price=price,
        quantity=quantity
    )

    items_db[item_id] = item

    return {
        "message": "Item created successfully",
        "item": item.model_dump()
    }


@mcp.tool()
def update_item(
    item_id: int,
    name: str,
    description: str,
    price: float,
    quantity: int
) -> dict:
    """
    Update existing item.
    """

    if item_id not in items_db:
        return {
            "error": "Item not found"
        }

    updated_item = Item(
        name=name,
        description=description,
        price=price,
        quantity=quantity
    )

    items_db[item_id] = updated_item

    return {
        "message": "Item updated successfully",
        "item": updated_item.model_dump()
    }


@mcp.tool()
def delete_item(item_id: int) -> dict:
    """
    Delete item by ID.
    """

    if item_id not in items_db:
        return {
            "error": "Item not found"
        }

    del items_db[item_id]

    return {
        "message": "Item deleted successfully"
    }


@mcp.tool()
def list_available_tools() -> List[str]:
    """
    Return list of available MCP tools.
    """

    return [
        "get_config",
        "health_check",
        "get_items",
        "get_item",
        "create_item",
        "update_item",
        "delete_item"
    ]


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":
    print("Starting Inventory MCP Server...")
    mcp.run(transport="stdio")