import unittest
import time
from appium import webdriver


class TestZipgoApp(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		desired_caps = {}
		desired_caps['deviceName'] = "YOur Device name"
		
		desired_caps['platformName'] = "Android"
		
		#change the version as required
		desired_caps['platformVersion'] = "7.1.2"

		desired_caps['appPackage'] = 'com.zipgo.customer'
		desired_caps['appActivity'] = 'com.zipgo.customer.activities.SplashActivity'

		cls.driver =  webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

	def test01_openapp(self):
		time.sleep(5)
		#click on MEnu option
		menu_button = self.driver.find_element_by_id("com.zipgo.customer:id/menu_btn")
		menu_button.click()
		
		#click on Edit Profile
		self.driver.find_element_by_name("Edit Profile").click()

	def test02_edit_profile(self):
		driver = self.driver
		time.sleep(3)
		#click on Edit Button
		driver.find_element_by_id("com.zipgo.customer:id/edit_button").click()
		#edit Name
		number = driver.find_element_by_id("com.zipgo.customer:id/et_name")
		number.clear()
		number.send_keys('New Name')
		#save Changes
		driver.find_element_by_xpath("//android.widget.TextView[@text='SAVE']").click()
		time.sleep(2)
		#Close App
		driver.back()



if __name__ == "__main__":

	unittest.main(verbosity=2)
