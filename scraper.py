from selenium import webdriver
import yaml

def login(driver):
	creds = yaml.load(open('NPcredentialsNP.yml'))
	driver.find_element_by_id('user').send_keys(creds['computingID'])
	driver.find_element_by_id('pass').send_keys(creds['password'])
	driver.find_element_by_id('pass').submit()

def getHoursSpentDistribution(group, number):
	driver = webdriver.Firefox()
	driver.get('https://evals.itc.virginia.edu/course-selectionguide/pages/SGMain.jsp?cmp=' + group + ',' + number + ',')
	if driver.title == 'NetBadge Web Login':
		login(driver)


def main():
	getHoursSpentDistribution('APMA','1110')
main()