# graph/planner/validator.py
def validate_plan(plan: dict) -> dict:
    """Validate and fix common planning issues."""
    
    # Ensure at least one source
    if not plan.get("sources"):
        plan["sources"] = ["private_rag"]
    
    # Ensure required fields
    if not plan.get("retrieval_fields"):
        plan["retrieval_fields"] = ["title", "price", "rating"]
    
    # Remove invalid fields
    valid_fields = {
        "title", "brand", "price", "rating", "category", 
        "material", "features", "ingredients", "in_stock", "review_count"
    }
    plan["retrieval_fields"] = [f for f in plan["retrieval_fields"] if f in valid_fields]
    
    # Ensure filters is a dict
    if not isinstance(plan.get("filters"), dict):
        plan["filters"] = {}
    
    return plan