from playwright.sync_api import sync_playwright

def download_example_html():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        html_content = page.content()
        with open("example.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        browser.close()
    print("Downloaded example.com HTML to example.html")

if __name__ == "__main__":
    download_example_html()

