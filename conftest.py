import subprocess
import time
import pytest

@pytest.fixture(scope="session", autouse=True)
def start_local_server():
    # 1. Playwright starts your dev server in the background automatically
    # Change "npm run dev" to the exact command you use to launch your project
    server_process = subprocess.Popen(
        ["npm", "run", "dev"], 
        shell=True,
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL
    )
    
    # 2. Give the server 3 seconds to spin up completely
    time.sleep(3)
    
    yield
    
    # 3. Playwright kills the background server once all tests finish
    server_process.terminate()

    # ─── FIXES THE BROWSER WINDOW FRAME SIZE ───
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        # Forces the actual physical Windows window to open fully maximized
        "args": ["--start-maximized"] 
    }

# ─── FIXES THE INTERNAL CONTENT VIEWPORT SIZE ───
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        # Disables default 1280x720 caps so the webpage fills the maximized window
        "viewport": None 
    }




