import unittest
import time
from appium import webdriver


class TestZipgoApp(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		desired_caps = {}
		desired_caps['deviceName'] = "CVH7N16806000999"
		desired_caps['platformName'] = "Android"
		desired_caps['platformVersion'] = "7.1.2"

		desired_caps['appPackage'] = 'com.zipgo.customer'
		desired_caps['appActivity'] = 'com.zipgo.customer.activities.SplashActivity'

		cls.driver =  webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

	def test01_openapp(self):
		time.sleep(5)
		menu_button = self.driver.find_element_by_id("com.zipgo.customer:id/menu_btn")
		menu_button.click()
		#click on Edit Profile

		self.driver.find_element_by_name("Edit Profile").click()

	def test02_edit_profile(self):
		driver = self.driver
		time.sleep(3)

		driver.find_element_by_id("com.zipgo.customer:id/edit_button").click()
		#edit number
		number = driver.find_element_by_id("com.zipgo.customer:id/et_name")
		number.clear()
		number.send_keys('New Name')

		driver.find_element_by_xpath("//android.widget.TextView[@text='SAVE']").click()
		time.sleep(2)
		driver.back()



if __name__ == "__main__":

	unittest.main(verbosity=2)