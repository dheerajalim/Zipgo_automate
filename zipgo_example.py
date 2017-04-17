import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class TestZipgo(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.driver = webdriver.Chrome('C:\Personal\Development\Python\seliniumtest\chromedriver.exe')
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(10)

		cls.driver.get("https://www.zipgo.in")


	def test01_Routes(self):

		driver = self.driver

		routes_link = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a')
		routes_link.click()
		time.sleep(2)

		origin = driver.find_element_by_name("pickup_location_info[location_text]")
		destination = driver.find_element_by_name("destination_location_info[location_text]")

		origin.clear()
		destination.clear()

		origin.send_keys("Kor")
		time.sleep(2)
		#ActionChains(self.driver).key_down(Keys.DOWN).key_down(Keys.RETURN).perform()
		ActionChains(self.driver).send_keys(Keys.DOWN,Keys.RETURN).perform()

		destination.send_keys("Ele")
		time.sleep(2)

		ActionChains(self.driver).send_keys(Keys.DOWN,Keys.DOWN,Keys.RETURN).perform()

		time.sleep(5)

		view_schedule_button  = driver.find_element_by_class_name("view-trips-js")
		view_schedule_button.click()

		#closing the trip summary

		driver.find_element_by_class_name("close-trips-div").click()


	def test02_getapplink(self):

		driver = self.driver

		phone = driver.find_element_by_name("phone")
		phone.clear()
		phone.send_keys("Your Number")
		phone.submit()

		time.sleep(2)

		link_messsage = driver.find_element_by_xpath("/html/body/nav/div[3]/p")
		self.assertEqual("Thank you for choosing ZipGo. App dowload link will be sent to your mobile.", link_messsage.text)





if __name__ == "__main__":

	unittest.main(verbosity=2)

