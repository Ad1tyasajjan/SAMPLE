# Code Quality Error 3: High Cyclomatic Complexity
# WARNING: This function is too complex and hard to maintain!

def process_order(order, user, payment, shipping, coupon, gift_wrap, 
                  express, insurance, notifications, tracking):
    """
    This function has extremely high cyclomatic complexity.
    It should be refactored into smaller, focused functions.
    """
    result = {"status": "pending", "total": 0, "messages": []}
    
    # Check user
    if user is None:
        result["status"] = "error"
        result["messages"].append("No user")
        return result
    elif user.get("active") is False:
        result["status"] = "error"
        result["messages"].append("Inactive user")
        return result
    elif user.get("verified") is False:
        if user.get("trust_score", 0) < 50:
            result["status"] = "error"
            result["messages"].append("Unverified low-trust user")
            return result
        else:
            result["messages"].append("Warning: unverified user")
    
    # Check order
    if order is None:
        result["status"] = "error"
        return result
    elif len(order.get("items", [])) == 0:
        result["status"] = "error"
        result["messages"].append("Empty order")
        return result
    elif len(order.get("items", [])) > 100:
        result["messages"].append("Large order - manual review needed")
    
    # Calculate total
    total = 0
    for item in order.get("items", []):
        if item.get("price"):
            if item.get("quantity"):
                if item.get("discount"):
                    total += item["price"] * item["quantity"] * (1 - item["discount"])
                else:
                    total += item["price"] * item["quantity"]
            else:
                total += item["price"]
        else:
            result["messages"].append(f"Item without price: {item}")
    
    # Apply coupon
    if coupon:
        if coupon.get("type") == "percent":
            if coupon.get("value"):
                if coupon["value"] <= 100:
                    total = total * (1 - coupon["value"] / 100)
                else:
                    result["messages"].append("Invalid coupon value")
            else:
                result["messages"].append("Coupon missing value")
        elif coupon.get("type") == "fixed":
            if coupon.get("value"):
                total = max(0, total - coupon["value"])
            else:
                result["messages"].append("Coupon missing value")
        else:
            result["messages"].append("Unknown coupon type")
    
    # Shipping
    if shipping:
        if shipping.get("method") == "standard":
            total += 5.99
        elif shipping.get("method") == "express":
            if express:
                total += 15.99
            else:
                total += 12.99
        elif shipping.get("method") == "overnight":
            total += 25.99
        else:
            total += 5.99
    
    # Gift wrap
    if gift_wrap:
        if gift_wrap.get("premium"):
            total += 9.99
        else:
            total += 4.99
    
    # Insurance
    if insurance:
        if insurance.get("level") == "basic":
            total += total * 0.02
        elif insurance.get("level") == "premium":
            total += total * 0.05
        elif insurance.get("level") == "full":
            total += total * 0.10
    
    # Payment processing
    if payment:
        if payment.get("method") == "credit":
            if payment.get("verified"):
                result["payment_status"] = "approved"
            else:
                result["payment_status"] = "pending_verification"
        elif payment.get("method") == "debit":
            result["payment_status"] = "approved"
        elif payment.get("method") == "paypal":
            if payment.get("account"):
                result["payment_status"] = "redirect_to_paypal"
            else:
                result["status"] = "error"
                result["messages"].append("PayPal account required")
                return result
        elif payment.get("method") == "crypto":
            result["payment_status"] = "awaiting_confirmation"
        else:
            result["status"] = "error"
            result["messages"].append("Unknown payment method")
            return result
    else:
        result["status"] = "error"
        result["messages"].append("Payment required")
        return result
    
    # Notifications
    if notifications:
        if notifications.get("email"):
            result["send_email"] = True
        if notifications.get("sms"):
            if user.get("phone"):
                result["send_sms"] = True
            else:
                result["messages"].append("SMS requested but no phone")
        if notifications.get("push"):
            result["send_push"] = True
    
    # Tracking
    if tracking:
        if tracking.get("enabled"):
            if tracking.get("provider") == "ups":
                result["tracking_provider"] = "UPS"
            elif tracking.get("provider") == "fedex":
                result["tracking_provider"] = "FedEx"
            elif tracking.get("provider") == "usps":
                result["tracking_provider"] = "USPS"
            else:
                result["tracking_provider"] = "Default"
    
    result["total"] = round(total, 2)
    result["status"] = "success"
    return result
