from CommonUtilities.BaseClass import BaseClass
from Data_Repository.HomePageData import HomePageDataContent
import time, pytest

from GreenKartPages.HomePage import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage(BaseClass):


    def test_formSubmission(self, getData):
        self.OpenURL(self.driver, getData["URL"])
        test_case_name = "test_Registration_Form_Submission"
        log = self.loggerProgram(test_case_name)
        homepage2 = HomePage(self.driver)
        homepage2.GetNameType().send_keys(getData["FNAME"])
        homepage2.EmailType().send_keys(getData["EMAIL"])
        homepage2.PasswordType().send_keys(getData["PASSWORD"])
        homepage2.CheckboxClick().click()
        #genderdropdown = Select(homepage2.GenderSelect())
        #genderdropdown.select_by_index(1)
        self.SelectFromDropDown(homepage2.GenderSelect(), getData["GENDER"])
        time.sleep(1)
        #genderdropdown.select_by_visible_text("Male")
        homepage2.SubmitButtonClick().click()
        assert "success" in homepage2.SuccessMessageCheck().text
        log.info(homepage2.SuccessMessageCheck().text)
        self.driver.refresh()

    @pytest.fixture(params=HomePageDataContent.getTestData("HomePage"))
    def getData(self, request):
        return request.param


    #@pytest.fixture(params=[("Aravinth", "abc@xyz.com", "sample", "Male"), ("Aishvarya","xyz@abc.com", "sample", "Female")])
    #@pytest.fixture(params=[{"firstname":"Aravinth", "email":"abc@xyz.com", "password":"sample", "gender":"Male"},
    #                        {"firstname":"Aishvarya", "email":"xyx@abc.com", "password":"sample", "gender":"Female"}])
    #def getData(self, request):
    #    return request.param

