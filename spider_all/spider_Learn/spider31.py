import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying.py import Chaojiying

EMAIL = 'cqc@cuiqingcai.com'
PASSWORD = ''
CHAOJIYING_USERNAME = 'anthocyanin'
CHAOJIYING_PASSWORD = 'gonghui123456'
CHAOJIYING_SOFT_ID = 899135
CHAOJIYING_KIND = 9201


class CrackTouClick():
    def __init__(self):
        self.url = 'http://admin.touclick.com/login.html'  # 网址目前已经不能用了，打不开
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID, CHAOJIYING_KIND)

    def __del__(self):
        self.browser.close()

    def open(self):
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_touch_button(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'touclick-hod-wrap')))
        return button

    def get_touch_element(self):
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-pub-content')))
        return element

    def get_position(self):
        element = self.get_touch_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self, name):
        top, bottom, left, right = self.get_position()
        print('验证码的位置：', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((top, bottom, left, right))
        captcha.save(name)
        return captcha

    def get_points(self, captcah_res):
        groups = captcah_res.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_touch_element(), location[0],
                                                                   location[1]).click().perform()
            time.sleep(1)

    def touch_click_verify(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'touclick-pub-submit')))
        return button

    def login(self):
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, '_submit')))
        submit.click()
        time.sleep(10)
        print('登陆成功')

    def crack(self):
        self.open()
        button = self.get_touch_button()
        button.click()
        image = self.get_touclick_image('captcha1')
        bytes_array = BytesIO()
        image.save(bytes_array, 'png')
        result = self.chaojiying.postpic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        locations = self.get_points(result)
        self.touch_click_words(locations)
        self.touch_click_verify()
        success = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'touclick-hod-note'), '验证成功'))
        print(success)

        if not success:
            self.crack()
        else:
            self.login()


if __name__ == '__main__':
    crack = CrackTouClick()
    crack.crack()


















