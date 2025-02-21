from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # By 모듈 임포트

driver = wb.Chrome()
driver.get("http://www.naver.com")

for symbol in driver.find_element(By.TAG_NAME,'h4'):
    print(symbol.text)
    
# 검색어 입력
search = driver.find_element(By.ID, "query")

search.send_keys("지하철")  # 검색어 입력
search.send_keys(Keys.ENTER)  # 엔터 입력

# 뒤로가기
driver.back()

# 클릭
btn = driver.find_element(By.ID, "search_btn")
btn.click()

# 스크린샷
driver.get_screenshot_as_file("subway.png")

# 창 종료
driver.quit()
