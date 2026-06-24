def test_my_local_site(page):
    # 1. Point Playwright to your running localhost server
    page.goto("http://localhost:3000")
    
    # 2. Print the page title to verify connection
    print("\nConnected! Page Title is:", page.title())
    
    # 3. Quick check to make sure the page structure is up
    assert page.title() != ""

    # ─── ADD THIS LINE ───
    # This pauses the browser for 10,000 milliseconds (10 seconds)
    page.wait_for_timeout(10000) 