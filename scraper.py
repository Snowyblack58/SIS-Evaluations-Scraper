from selenium import webdriver
import yaml
import re

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
	percentages = driver.find_elements_by_class_name('percentage')
	responses = driver.find_elements_by_xpath('html/body/div/form/table/tbody/tr/td/table/tbody/tr/td/span/span')
	distribution = [0,0,0,0,0]
	for cnt in range(0, len(responses)):
		votes = int(re.search('\d+', responses[cnt].text).group(0))
		for i in range(5):
			distribution[i] += round(float(percentages[cnt*5+i].text[:-1]) / 100 * votes)
	return distribution

def main():
	distribution = getHoursSpentDistribution('APMA','1110')
	print(distribution)
main()