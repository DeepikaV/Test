import sys
import commands
from selenium import webdriver

class test:
	
	def versions(self):
		print commands.getoutput("java -version") 
		print ("")
		print ("The Python version is %s.%s.%s" % sys.version_info[:3])
		print ('')
		print commands.getoutput("pybot --version")
		print ('')
		print commands.getoutput("git --version")
		driver = webdriver.Firefox()
		print ('')
		print ("Firefox version is:" )
		print driver.capabilities['version']


	


		 
