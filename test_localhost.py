from playwright.sync_api import Page, expect
import psycopg2
from db_config import get_db_connection 

def test_my_local_site(page: Page):
    try:
        # 1. Point Playwright to your running localhost server
        page.goto("http://localhost:3000")
        
        # 2. Print the page title to verify connection
        print("\nConnected! Page Title is:", page.title())
        
        # 3. Quick check to make sure the page structure is up
        assert page.title() != "This Will Fail"

        # ─── ADD THIS LINE ───
        # This pauses the browser for 10,000 milliseconds (10 seconds)
        page.wait_for_timeout(10000) 
    except AssertionError as e:
        # 1. Capture screenshot as a binary buffer if the test fails
        screenshot_bytes = page.screenshot(full_page=True)
        
        # 2. Get database connection
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            # 3. Log the test failure and the image directly into pgAdmin
            insert_query = """
            INSERT INTO bug_logs (test_name, error_message, screenshot_binary)
            VALUES (%s, %s, %s);
            """
            cursor.execute(insert_query, ("test_my_local_site", str(e), psycopg2.Binary(screenshot_bytes)))
            
            conn.commit()
            cursor.close()
            conn.close()
            print("💾 Bug and screenshot logged successfully to pgAdmin!")
            
        raise e  # Make sure the test still shows as failed in your test runner
