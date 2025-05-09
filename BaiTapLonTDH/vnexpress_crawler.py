from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Mở trang VNExpress
    driver.get("https://vnexpress.net/")
    driver.maximize_window()

    # Click vào mục "Khoa học"
    khoa_hoc_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wrap-main-nav"]/nav/ul/li[6]/a'))
    )
    khoa_hoc_link.click()

    # Đợi tiêu đề trang chuyên mục hiển thị
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dark_theme"]/section[5]/div/nav/div/h1/a'))
    )

    print("Tiêu đề trang:", driver.title)

    # Lấy danh sách tiêu đề bài viết trong mục "Khoa học"
    titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".title-news a"))
    )

    print("\n📌 Các bài viết trong mục Khoa học:")
    for i, title in enumerate(titles, 1):
        text = title.text.strip()
        if text:
            print(f"{i}. {text}")

    # ==============================
    # TIẾP THEO: BẤM NÚT TÌM KIẾM
    # ==============================

    # Bấm biểu tượng tìm kiếm
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="inp_keyword"]'))
    )
    search_button.click()

    # Gõ từ khóa vào ô tìm kiếm và nhấn Enter
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="btnSearchHeader"]/svg'))
    )
    search_input.send_keys("vũ trụ", Keys.ENTER)

    # Đợi kết quả tìm kiếm hiển thị
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".title-news a"))
    )

    print("\n🔍 Kết quả tìm kiếm cho 'vũ trụ':")
    search_results = driver.find_elements(By.CSS_SELECTOR, ".title-news a")
    for i, result in enumerate(search_results, 1):
        text = result.text.strip()
        if text:
            print(f"{i}. {text}")

finally:
    time.sleep(2)
    driver.quit()
