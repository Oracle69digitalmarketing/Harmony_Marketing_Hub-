# --- harmony_mvp_followup_logic.py ---
# Conceptual Python script illustrating backend logic for the Client Follow-Up Bot MVP.
# This is for planning and understanding, not direct execution as a full application.

import time
import json
from datetime import datetime, timedelta # For simulating delays

# --- Mock Configuration ---
MOCK_USER_ID = "funke_user_123" # Simulating Funke, our authenticated user
REVIEW_REQUEST_DELAY_SECONDS = 24 * 60 * 60 # 24 hours, for example

# --- Mock Database (Simulating data that would be in PostgreSQL, MySQL, etc.) ---
mock_db = {
    "users": {
        "funke_user_123": {
            "userID": "funke_user_123",
            "businessName": "Funke's Creations",
            "preferredReviewLink": "https://reviews.example.com/funkescreations"
        }
    },
    "clients": {
        "client_bola_456": {
            "clientID": "client_bola_456", "userID": "funke_user_123",
            "clientName": "Mrs. Bola A.", "clientPhoneNumber": "+2348012345678" # Example Nigerian number
        },
        "client_john_789": {
            "clientID": "client_john_789", "userID": "funke_user_123",
            "clientName": "Mr. John B.", "clientPhoneNumber": "+2348098765432"
        }
    },
    "orders": {
        "order_mrs_bola_123": {
            "orderID": "order_mrs_bola_123", "userID": "funke_user_123",
            "clientID": "client_bola_456", "serviceDescription": "Two Aso Ebi outfits",
            "status": "Completed", "isThankYouSMSSent": False, "isReviewRequestSMSSent": False,
            "completedAt": (datetime.now() - timedelta(days=1)).isoformat() # Completed yesterday
        },
        "order_john_789_A": {
            "orderID": "order_john_789_A", "userID": "funke_user_123",
            "clientID": "client_john_789", "serviceDescription": "Kaftan Repair",
            "status": "Ongoing", "isThankYouSMSSent": False, "isReviewRequestSMSSent": False,
            "completedAt": None
        },
        "order_john_789_B": {
            "orderID": "order_john_789_B", "userID": "funke_user_123",
            "clientID": "client_john_789", "serviceDescription": "New Senator Suit",
            "status": "Completed", "isThankYouSMSSent": True, "isReviewRequestSMSSent": False, # Thank you sent
            "completedAt": (datetime.now() - timedelta(days=3)).isoformat()
        }
    }
}

# --- Conceptual Helper Functions (Simulating External Services & DB Interactions) ---

def db_get_order(order_id, user_id):
    """Simulates fetching an order from the database if it belongs to the user."""
    order = mock_db["orders"].get(order_id)
    if order and order["userID"] == user_id:
        print(f"[MOCK DB] Fetched order: {order_id}")
        return order.copy() # Return a copy to avoid modifying the mock DB directly
    print(f"[MOCK DB] Error: Order {order_id} not found for user {user_id}.")
    return None

def db_get_client(client_id, user_id):
    """Simulates fetching client details."""
    client = mock_db["clients"].get(client_id)
    if client and client["userID"] == user_id:
        print(f"[MOCK DB] Fetched client: {client_id}")
        return client.copy()
    print(f"[MOCK DB] Error: Client {client_id} not found for user {user_id}.")
    return None

def db_get_user_profile(user_id):
    """Simulates fetching user's business details."""
    user = mock_db["users"].get(user_id)
    if user:
        print(f"[MOCK DB] Fetched user profile: {user_id}")
        return user.copy()
    print(f"[MOCK DB] Error: User profile {user_id} not found.")
    return None

def get_sms_template(template_type):
    """Simulates retrieving an SMS template."""
    print(f"[MOCK TEMPLATE ENGINE] Getting SMS template for '{template_type}'...")
    if template_type == "ThankYou":
        return "Hello [Client Name], thank you for choosing [Business Name]! We hope you love your ([Service Desc]). - [Business Name]"
    elif template_type == "ReviewRequest":
        return "Hi [Client Name], we hope you're enjoying your service from [Business Name]! If you have a moment, please share your feedback here: [Review Link]. Thanks!"
    return None

def personalize_sms_message(template_text, client_name, business_name, review_link=None, service_desc="items/service"):
    """Simulates personalizing the SMS template."""
    message = template_text.replace("[Client Name]", client_name)
    message = message.replace("[Business Name]", business_name)
    message = message.replace("[Service Desc]", service_desc)
    if review_link:
        message = message.replace("[Review Link]", review_link)
    print(f"[MOCK PERSONALIZATION] Personalized SMS: '{message}'")
    return message

def mock_send_sms_via_gateway(phone_number, message):
    """Simulates sending an SMS. Returns True if successful (mocked)."""
    if not phone_number:
        print(f"[MOCK SMS GATEWAY] Error: No phone number to send SMS: '{message}'")
        return False
    print(f"[MOCK SMS GATEWAY] Sending SMS to {phone_number}: '{message}'")
    # In a real system, this would interact with Twilio, Africa's Talking, etc.
    return True # Assume success for mock

def db_update_order_followup_status(order_id, sms_type_sent, status=True):
    """Simulates updating the OrderLog with SMS sent status in the database."""
    if order_id in mock_db["orders"]:
        if sms_type_sent == "ThankYou":
            mock_db["orders"][order_id]["isThankYouSMSSent"] = status
        elif sms_type_sent == "ReviewRequest":
            mock_db["orders"][order_id]["isReviewRequestSMSSent"] = status
        print(f"[MOCK DB] Updated order {order_id}: {sms_type_sent}Sent = {status}")
        return True
    return False

# --- Conceptual Background Job Scheduler & Executor ---
mock_background_job_queue = []

def mock_schedule_delayed_job(job_type, delay_seconds, job_data):
    """Simulates scheduling a background job."""
    scheduled_time = time.time() + delay_seconds
    job = {"type": job_type, "scheduled_time": scheduled_time, "data": job_data}
    mock_background_job_queue.append(job)
    print(f"[MOCK SCHEDULER] Scheduled job '{job_type}' to run around {datetime.fromtimestamp(scheduled_time)} with data: {job_data}")
    return True

def execute_pending_background_jobs_conceptual():
    """
    Simulates a background worker picking up and executing jobs.
    In a real system, this would run in a separate process.
    """
    print("\n[MOCK BACKGROUND WORKER] Checking for pending jobs...")
    current_time = time.time()
    due_jobs = [job for job in mock_background_job_queue if job["scheduled_time"] <= current_time]
    
    for job in due_jobs:
        print(f"[MOCK BACKGROUND WORKER] Executing job: {job['type']} with data {job['data']}")
        if job["type"] == "SendReviewRequestSMS":
            execute_send_review_request_sms_conceptual(job["data"])
        mock_background_job_queue.remove(job) # Remove after processing
    if not due_jobs:
        print("[MOCK BACKGROUND WORKER] No due jobs found.")


def execute_send_review_request_sms_conceptual(job_data):
    """The actual logic the background job would execute for sending a review request."""
    order_id = job_data.get("orderID")
    client_phone_number = job_data.get("clientPhoneNumber")
    client_name = job_data.get("clientName")
    business_name = job_data.get("businessName")
    review_link = job_data.get("reviewLink")
    service_desc = job_data.get("serviceDescription", "your service")


    if not all([order_id, client_phone_number, client_name, business_name, review_link]):
        print("[MOCK BACKGROUND JOB - Review SMS] Error: Missing critical data.")
        return

    template_text = get_sms_template("ReviewRequest")
    if template_text:
        message = personalize_sms_message(template_text, client_name, business_name, review_link=review_link, service_desc=service_desc)
        if mock_send_sms_via_gateway(client_phone_number, message):
            db_update_order_followup_status(order_id, "ReviewRequest", status=True)
            print(f"[MOCK BACKGROUND JOB - Review SMS] Review request SMS successfully sent for order {order_id}.")
        else:
            print(f"[MOCK BACKGROUND JOB - Review SMS] Failed to send review request SMS for order {order_id}.")
    else:
        print("[MOCK BACKGROUND JOB - Review SMS] Error: Could not retrieve review request SMS template.")

# --- Conceptual Main Logic Function (Simulating API Endpoint Controller) ---

def trigger_follow_up_sequence(user_id, order_id):
    """
    Conceptual logic for POST /api/v1/orders/{orderID}/trigger-followup.
    """
    print(f"\n--- Triggering Follow-Up Sequence for Order: {order_id}, User: {user_id} ---")
    
    order = db_get_order(order_id, user_id)
    if not order: return {"success": False, "message": "Order not found or unauthorized."}

    if order.get("status") != "Completed":
        return {"success": False, "message": f"Order status is '{order.get('status')}', not 'Completed'."}

    client = db_get_client(order["clientID"], user_id)
    user_profile = db_get_user_profile(user_id)

    if not client or not client.get("clientPhoneNumber"):
        return {"success": False, "message": "Client phone number missing."}
    if not user_profile: # Should not happen for an authenticated user
        return {"success": False, "message": "User profile error."}

    # 1. Process "Thank You" SMS
    thank_you_sent_this_time = False
    if not order.get("isThankYouSMSSent"):
        template_text = get_sms_template("ThankYou")
        if template_text:
            message = personalize_sms_message(
                template_text,
                client["clientName"],
                user_profile["businessName"],
                service_desc=order["serviceDescription"]
            )
            if mock_send_sms_via_gateway(client["clientPhoneNumber"], message):
                db_update_order_followup_status(order_id, "ThankYou", status=True)
                thank_you_sent_this_time = True
                print("Thank You SMS sent successfully.")
            else:
                print("Failed to send Thank You SMS.")
                return {"success": False, "message": "Failed to send Thank You SMS."}
        else:
            print("Server error: Thank You template missing.")
            return {"success": False, "message": "Server error: Thank You template missing."}
    else:
        print("Thank You SMS was previously sent for this order.")
        thank_you_sent_this_time = True # Consider it "successful" for review scheduling logic

    # 2. Schedule "Review Request" SMS
    if thank_you_sent_this_time and not order.get("isReviewRequestSMSSent"):
        job_data = {
            "orderID": order_id,
            "clientPhoneNumber": client["clientPhoneNumber"],
            "clientName": client["clientName"],
            "businessName": user_profile["businessName"],
            "reviewLink": user_profile["preferredReviewLink"],
            "serviceDescription": order["serviceDescription"]
        }
        if mock_schedule_delayed_job("SendReviewRequestSMS", REVIEW_REQUEST_DELAY_SECONDS, job_data):
            print("Review Request SMS scheduled successfully.")
            return {"success": True, "message": "Thank You SMS sent. Review request SMS scheduled."}
        else:
            print("Failed to schedule Review Request SMS.")
            return {"success": True, "message": "Thank You SMS sent, but failed to schedule review request."} # Partial success
    elif order.get("isReviewRequestSMSSent"):
        print("Review Request SMS was previously sent/scheduled for this order.")
        return {"success": True, "message": "Thank You SMS processed. Review request previously handled."}
    
    # Fallback message if thank_you_sent_this_time is False (shouldn't happen if error handling above is correct)
    return {"success": False, "message": "Could not process follow-up sequence."}


# --- Illustrative "Run" Section (Simulating a workflow) ---
if __name__ == "__main__":
    print("=== Harmony Marketing Hub - MVP Follow-Up Bot Logic (Conceptual Script) ===")

    # Case 1: Trigger for Mrs. Bola's order (new follow-up)
    print("\n[WORKFLOW CASE 1] Triggering follow-up for Mrs. Bola's order (order_mrs_bola_123)...")
    result1 = trigger_follow_up_sequence(MOCK_USER_ID, "order_mrs_bola_123")
    print(f"Result for Mrs. Bola: {result1}")
    print(f"Order status in mock_db: {mock_db['orders']['order_mrs_bola_123']}")

    # Case 2: Trigger for an order that's not completed
    print("\n[WORKFLOW CASE 2] Triggering follow-up for Mr. John's ongoing order (order_john_789_A)...")
    result2 = trigger_follow_up_sequence(MOCK_USER_ID, "order_john_789_A")
    print(f"Result for John (Ongoing): {result2}")

    # Case 3: Trigger for an order where Thank You was already sent
    print("\n[WORKFLOW CASE 3] Triggering follow-up for Mr. John's other completed order (order_john_789_B)...")
    result3 = trigger_follow_up_sequence(MOCK_USER_ID, "order_john_789_B")
    print(f"Result for John (ThankYou Sent): {result3}")
    print(f"Order status in mock_db: {mock_db['orders']['order_john_789_B']}")
    
    # Simulate time passing and background worker running
    print("\n[WORKFLOW] Simulating some time passing for background jobs...")
    # In a real app, jobs run independently. Forcing execution here for demo.
    # Let's "fast-forward" time to make jobs due.
    for job in mock_background_job_queue:
        job["scheduled_time"] = time.time() - 1 # Make it overdue

    execute_pending_background_jobs_conceptual()
    # Check status of Mrs. Bola's order again to see if review SMS flag changed
    print(f"\nOrder status for Mrs. Bola in mock_db after background job simulation: {mock_db['orders']['order_mrs_bola_123']}")


    print("\n=== End of Conceptual Script Run ===")
