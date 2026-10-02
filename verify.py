from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(record_video_dir="/home/jules/verification/videos/")
    page = context.new_page()
    page.goto("http://localhost:4322/economics-site/article-1/")
    page.wait_for_timeout(2000)
    page.evaluate("window.scrollBy(0, window.innerHeight)")
    page.wait_for_timeout(2000)
    page.screenshot(path="/home/jules/verification/screenshots/verification2.png")
    context.close()
    browser.close()
