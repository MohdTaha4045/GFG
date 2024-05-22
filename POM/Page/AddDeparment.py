from selenium.webdriver.common.by import By


class AddDepartment :

    def __init__(self, driver):
        self.driver = driver
        self.department = (By.XPATH,"//span[text()='Department']")
        self.addDepartment = (By.XPATH,"//span[text()='Add Department']")
        self.departmentName = (By.ID,"name")
        self.ParentDepartment_dropdown = (By.ID,"parent")
        self.Designation_dropdown = (By.XPATH,"//span[text()='Select Designation(s)']")

    def open_page(self,url):
        self.driver.get(url)

    def open_department(self):
        self.department.click()

    def add_department(self):
        self.addDepartment.click()

    def Pass_departmentName(self, name)
         self.driver.find_element(self.departmentName).send_keys(name)

    def select_parentDepartment(self):
        self.driver.find_element(self.ParentDepartment_dropdown).click()


