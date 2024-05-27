from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

# ChromeDriver 경로 설정
chrome_driver_path = "C:\\Users\\daou\\Desktop\\자동화 업무\\chromedriver.exe"
service = Service(chrome_driver_path)

def initialize_webdriver():
    return webdriver.Chrome(service=service)

def login_and_click_button(url, user_id, password):
    driver = initialize_webdriver()
    driver.maximize_window()  # 창을 최대화

    try:
        # 로그인
        login_to_site(driver, url, user_id, password)

        # 출근 버튼 클릭
        click_the_button(driver)

    finally:
        # 브라우저 세션 종료
        driver.quit()

def login_to_site(driver, url, user_id, password):
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    try:
        # ID 입력 필드를 기다리고 입력
        id_input_xpath = "//input[@class='ipt_login login_wide']"
        id_input = wait.until(EC.presence_of_element_located((By.XPATH, id_input_xpath)))
        id_input.clear()
        id_input.send_keys(user_id)

        # PW 입력 필드를 기다리고 입력
        pw_input_xpath = "//input[@class='ipt_login']"
        pw_input = wait.until(EC.presence_of_element_located((By.XPATH, pw_input_xpath)))
        pw_input.clear()
        pw_input.send_keys(password)
        pw_input.send_keys("\n")

        # 로그인 성공은 주석 처리
        # success_element_id = "welcome_message"
        # wait.until(EC.presence_of_element_located((By.ID, success_element_id)))

    except TimeoutException:
        print("로그인 실패, 페이지 로드 지연")

def click_the_button(driver):
    wait = WebDriverWait(driver, 15)

    try:
        # 출근 버튼을 기다리고 클릭
        workIn_xpath = '//*[@id="workIn"]/html/body/div/div[2]/div/div[5]/div[1]/div[1]/div[3]/div/div[2]/section/div[1]/a[1]'
        work_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, workIn_xpath))) # BTN이 클릭 가능해질 때 까지 기다리기
        work_in_button.click()

        print("PASS")

    except TimeoutException:
        print("FAIL: 출근 BTN 클릭 실패")

if __name__ == "__main__":
    login_and_click_button('https://nstaging.daouoffice.com/login', "test@p5prz89a93.co.co", "1qaz2wsx#")
