# --- conceptual_followup_bot_handler.py ---
# Purpose: Illustrative backend logic for triggering the SMS follow-up sequence
# when an order is marked as complete.
# This guides the development of the POST /api/v1/orders/{orderID}/trigger-followup endpoint.

# Assume Flask-like imports, time module, etc.
# import time

# --- Placeholder / Mock Data Access & Service Call Functions ---

def get_order_from_db(order_id, user_id):
    """Conceptual: Fetches an order if it belongs to the user."""
    print(f"[Database - Mock] Fetching order {order_id} for user {user_id}...")
    if order_id == "order_mrs_bola_123" and user_id == "funke_user_123": # Mock specific order
        return {
            "orderID": "order_mrs_bola_123", "userID": "funke_user_123",
            "clientID": "client_bola_456", "serviceDescription": "Two Aso Ebi outfits",
            "status": "Completed", "isThankYouSMSSent": False, "isReviewRequestSMSSent": False,
            "completedAt": "2025-05-14T15:00:00Z"
        }
    return None

def get_client_from_db(client_id, user_id):
    """Conceptual: Fetches client details."""
    print(f"[Database - Mock] Fetching client {client_id} for user {user_id}...")
    if client_id == "client_bola_456" and user_id == "funke_user_123": # Mock specific client
        return {"clientID": "client_bola_456", "clientName": "Mrs. Bola", "clientPhoneNumber": "+2348012345678"}
    return None

def get_user_profile_from_db(user_id):
    """Conceptual: Fetches user's business details."""
    print(f"[Database - Mock] Fetching user profile {user_id}...")
    if user_id == "funke_user_123": # Mock specific user
        return {"userID": "funke_user_123", "businessName": "Funke's Creations", "preferredReviewLink": "https://reviews.example.com/funkescreations"}
    return None

def get_sms_template_text(template_type, user_preferences=None):
    """Conceptual: Retrieves SMS template text."""
    print(f"[Template Engine - Mock] Getting SMS template for '{template_type}'...")
    if template_type == "ThankYou":
        return "Hello [Client Name], thank you for choosing [Business Name]! We hope you love your items/service. - [Business Name]"
    elif template_type == "ReviewRequest":
        return "Hi [Client Name], we hope you're enjoying your service from [Business Name]! If you have a moment, please share your feedback here: [Review Link]. Thanks!"
    return None

def personalize_sms(template_text, client_name, business_name, review_link=None, service_desc=None):
    """Conceptual: Personalizes the SMS template."""
    message = template_text.replace("[Client Name]", client_name)
    message = message.replace("[Business Name]", business_name)
    if review_link: message = message.replace("[Review Link]", review_link)
    if service_desc: message = message.replace("[Service Description snippet]", service_desc) # Example for more detail
    print(f"[Personalization - Mock] Personalized message: {message}")
    return message

def send_sms_via_gateway(phone_number, message):
    """Conceptual: Simulates sending an SMS. Returns True if successful (mocked)."""
    print(f"[SMS Gateway - Mock] Sending SMS to {phone_number}: '{message}'")
    return True if phone_number else False

def update_order_followup_status_in_db(order_id, sms_type_sent, status=True):
    """Conceptual: Updates the OrderLog with SMS sent status."""
    print(f"[Database - Mock] Updating order {order_id}: {sms_type_sent}Sent = {status}")
    return True

def schedule_delayed_job(job_type, delay_seconds, job_data):
    """Conceptual: Simulates scheduling a background job."""
    print(f"[Background Scheduler - Mock] Scheduling job '{job_type}' to run in {delay_seconds} seconds with data: {job_data}")
    # In a real system, this job would later call a function like 'execute_send_review_request_sms'
    return True

# This function would be executed by the background scheduler for the delayed job
# def execute_send_review_request_sms_conceptual(job_data):
#     print("\n[Background Job - Mock EXECUTION] Sending Review Request SMS...")
#     order_id = job_data.get("orderID")
#     # Fetch fresh client/user details in case they changed, or use passed data
#     client_phone_number = job_data.get("clientPhoneNumber") 
#     client_name = job_data.get("clientName")
#     business_name = job_data.get("businessName")
#     review_link = job_data.get("reviewLink")

#     if not all([order_id, client_phone_number, client_name, business_name, review_link]):
#         print("[Background Job - Mock EXECUTION] Error: Missing data.")
#         return

#     template_text = get_sms_template_text("ReviewRequest")
#     if template_text:
#         message = personalize_sms(template_text, client_name, business_name, review_link=review_link)
#         if send_sms_via_gateway(client_phone_number, message):
#             update_order_followup_status_in_db(order_id, "ReviewRequest")
#             print(f"[Background Job - Mock EXECUTION] Review request SMS successfully sent for order {order_id}.")
#         else:
#             print(f"[Background Job - Mock EXECUTION] Failed to send review request SMS for order {order_id}.")
#     else:
#         print("[Background Job - Mock EXECUTION] Error: Could not retrieve review request SMS template.")

# --- Conceptual API Endpoint Logic (Illustrative) ---
# def handle_trigger_order_followup_request(user_id, order_id):
#     print(f"\n--- Conceptual Request: Trigger Follow-up for Order {order_id}, User {user_id} ---")
#     order = get_order_from_db(order_id, user_id)
#     if not order:
#         print(f"Error: Order {order_id} not found or not authorized.")
#         return {"success": False, "message": "Order not found or not authorized."}

#     if order.get("status") != "Completed":
#         print(f"Error: Order {order_id} is not 'Completed'. Status: {order.get('status')}")
#         return {"success": False, "message": "Order not 'Completed'."}

#     client = get_client_from_db(order.get("clientID"), user_id)
#     user_profile = get_user_profile_from_db(user_id)

#     if not client or not client.get("clientPhoneNumber"):
#         print(f"Error: Client phone number missing for order {order_id}.")
#         return {"success": False, "message": "Client phone number missing."}
#     if not user_profile:
#         print(f"Error: User profile missing for {user_id}.") # Should not happen for authenticated user
#         return {"success": False, "message": "User profile error."}

#     thank_you_sent_successfully = False
#     response_message = ""

#     # Process "Thank You" SMS
#     if not order.get("isThankYouSMSSent"):
#         template_text = get_sms_template_text("ThankYou")
#         if template_text:
#             message = personalize_sms(template_text, client.get("clientName"), user_profile.get("businessName"), service_desc=order.get("serviceDescription"))
#             if send_sms_via_gateway(client.get("clientPhoneNumber"), message):
#                 update_order_followup_status_in_db(order_id, "ThankYou")
#                 thank_you_sent_successfully = True
#                 response_message += "Thank You SMS sent. "
#                 print(f"Thank You SMS sent for order {order_id}.")
#             else:
#                 response_message += "Failed to send Thank You SMS. "
#                 print(f"Failed to send Thank You SMS for order {order_id}.")
#         else: # Should not happen if templates are configured
#             response_message += "Server error: Thank You template missing. "
#             print(f"Server error: Thank You template missing for order {order_id}.")
#     else:
#         thank_you_sent_successfully = True # Already sent, so allow review scheduling
#         response_message += "Thank You SMS previously sent. "
#         print(f"Thank You SMS previously sent for order {order_id}.")


#     # Schedule "Review Request" SMS
#     if thank_you_sent_successfully and not order.get("isReviewRequestSMSSent"):
#         delay_seconds = 24 * 60 * 60 # 24 hours
#         job_data = {
#             "orderID": order_id, "clientPhoneNumber": client.get("clientPhoneNumber"),
#             "clientName": client.get("clientName"), "businessName": user_profile.get("businessName"),
#             "reviewLink": user_profile.get("preferredReviewLink")
#         }
#         if schedule_delayed_job("SendReviewRequestSMS", delay_seconds, job_data):
#             response_message += "Review request SMS scheduled."
#             print(f"Review Request SMS scheduled for order {order_id}.")
#         else:
#             response_message += "Failed to schedule review request SMS."
#             print(f"Failed to schedule Review Request SMS for order {order_id}.")
#     elif order.get("isReviewRequestSMSSent"):
#         response_message += "Review request SMS previously processed."
#         print(f"Review Request SMS previously processed for order {order_id}.")

#     print(f"--- End Conceptual Request for Order {order_id} ---")
#     return {"success": True, "message": response_message.strip()}


# # --- Example of how these conceptual functions might be used (for illustration only) ---
# if __name__ == '__main__':
#     # Simulate Funke triggering the follow-up for Mrs. Bola's order
#     result = handle_trigger_order_followup_request("funke_user_123", "order_mrs_bola_123")
#     print(f"\nFinal API Response (Conceptual): {result}")

#     # Simulate the background job running later (this is a direct call for demo)
#     # In a real system, a scheduler would call something like 'execute_send_review_request_sms_conceptual'
#     # with the job_data that was queued by 'schedule_delayed_job'.
#     print("\n(Conceptual: If a background job for review request was scheduled, it would run later)")
#     # mock_job_data_for_execution = { ... as defined in schedule_delayed_job ... }
#     # execute_send_review_request_sms_conceptual(mock_job_data_for_execution)

