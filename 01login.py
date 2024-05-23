from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

# ChromeDriver 경로 설정
chrome_driver_path = "C:\\Users\\daou\\Desktop\\자동화 업무\\chromedriver.exe"
service = Service(chrome_driver_path)

# WebDriver 초기화 함수
def initialize_webdriver():
    driver = webdriver.Chrome(service=service)
    return driver

# 로그인 자동화 함수
def login_to_site(driver, url, user_id, password):
    driver.get(url)

    # WebDriverWait 객체 생성
    wait = WebDriverWait(driver, 15)

    try:
        # ID 입력 필드를 기다리고 입력
        id_input_xpath = "//input[@class='ipt_login login_wide']"
        id_input = wait.until(EC.presence_of_element_located((By.XPATH, id_input_xpath)))

        # JavaScript를 사용하여 값을 설정
        driver.execute_script("arguments[0].value = arguments[1];", id_input, user_id)

        # PW 입력 필드를 기다리고 입력
        pw_input_xpath = "//input[@class='ipt_login']"
        pw_input = wait.until(EC.presence_of_element_located((By.XPATH, pw_input_xpath)))
        pw_input.send_keys(password)

        # Enter 키를 통해 로그인
        pw_input.send_keys("\n")

        # 로그인 성공을 확인하기 위해 특정 요소를 기다림
        success_element_id = "welcome_message"
        success_element = wait.until(EC.presence_of_element_located((By.ID, success_element_id)))
        print("로그인 성공")

    except TimeoutException:
        print("로그인 실패 혹은 페이지 로드 지연")


if __name__ == "__main__":
    driver = initialize_webdriver()

    try:
        login_to_site(driver, 'https://nstaging.daouoffice.com/login', "test@uqg8vgqajs.co.co", "1qaz2wsx#")
    finally:
        # 드라이버 종료
        driver.quit()
