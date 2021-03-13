import time, pytest
from selenium.webdriver.support.select import Select
from CommonUtilities.BaseClass import BaseClass
#User defined class imports
from Data_Repository.HomePageData import HomePageDataContent
from GreenKartPages.HomePage import HomePage

class TestGreenKart(BaseClass):

    def test_GreenKart(self, getData):
        print("Person Y updating code - THis is for GIT purpose")
        print("Person X updating code - THis is for GIT purpose")
        print("Adding code in branch develop only")
        print("Code Added by American Architect")
        print("Code really added by American architect, above print  is actually by Indina architect")
        self.OpenURL(self.driver, getData["URL"])
        time.sleep(4)
        self.ExplicitWaitForLinkText("Practice Projects")
        homepage1 = HomePage(self.driver)
        test_case_name = "test_GreenKart_Veggies_with_ot_Search"
        log = self.loggerProgram(test_case_name)

        homepage1.PractiseProjectsLinkClick().click()
        # IF INTERMEDIATE IS DISPLAYED PROVIDE DETAILS AND PROCEED
        time.sleep(2)
        if homepage1.HomePage2SubmitButtonClick().is_displayed():
            homepage1.EnterNameTextBox().send_keys(getData["FNAME"])
            homepage1.EnterEmailTextBox().send_keys(getData["EMAIL"])
            homepage1.AgreeTermsCheckBoxClick().click()
            homepage1.SubmitButtonClick().click()

        # IF INTERMEDIATE PAGE IS NOT DISPLAYED CONTROL COMES HERE SKIPPING ABOVE IF PART
        self.ExplicitWaitForLinkText("Automation Practise - 1")
        gkvegpage = homepage1.GreenKartWebLinkClick()

        # LANDED IN GREENKART PAGE
        gkvegpage.SearchVeggiesTextBox().send_keys("ot")
        time.sleep(3)
        products = gkvegpage.GroupAllAddToCartButtons()
        p = b = c = 1
        po_amount = ca_amount = be_amount = 0
        log.info("List of products searched for the text "+ gkvegpage.SearchVeggiesTextBox().text)
        for product in products:
            #prod_text = product.find_element_by_xpath("parent::div /parent::div/h4").text
            prod_text = gkvegpage.GetProductLabel(product).text
            log.info(prod_text)
            if prod_text == "Carrot - 1 Kg":
                c = c + 1
                time.sleep(1)
                gkvegpage.CarrotPlusClick(product).click()
                ca_amount = c * int((gkvegpage.CarrotCostGet(product)).text)
                time.sleep(1)
                product.click()
            elif prod_text == "Beetroot - 1 Kg":
                b = b + 1
                time.sleep(1)
                gkvegpage.BeetrootPlusClick(product).click()
                be_amount = b * int(gkvegpage.BeetrootCostGet(product).text)
                time.sleep(1)
                product.click()
            elif prod_text == "Potato - 1 Kg":
                p = p + 1
                time.sleep(1)
                gkvegpage.PotatoPlusClick(product).click()
                time.sleep(1)
                po_amount = p * int(gkvegpage.PotatoCostGet(product).text)
                product.click()

            src_amount = po_amount + ca_amount + be_amount
            src_quantity = p + c + b

        log.info("Potato Cost is "+ str(po_amount) +" Carrot Cost is "+str(ca_amount)+" BeetRoot cost is "+str(be_amount))
        log.info("Total Quantity is "+str(src_quantity))
        log.info("Total Cost in Veggies List page is "+str(src_amount))
        time.sleep(1)
        gkvegpage.CartClick().click()

        allbuttons = gkvegpage.FindCheckOutButton()
        for button in allbuttons:
            if button.text == "PROCEED TO CHECKOUT":
                veglistreview = gkvegpage.ProceedCheckoutClick(button)
                # At this point control goes to next table page
                break

        time.sleep(3)
        veglistreview.PromoCodeEnter().send_keys("rahulshettyacademy")
        veglistreview.PromoApplyButton().click()
        self.ExplicitWaitForClassName("promoInfo")
        tgt_amounts = veglistreview.AllAmountsFromTable()
        tgt_quantity = veglistreview.AllQuantityFromTable()
        total = 0
        item_match = 0

        for amountcheck in tgt_amounts:
            total = int(amountcheck.text) + total
            log.info("Target page individual items cost is "+ amountcheck.text)
            if int(amountcheck.text) == be_amount or int(amountcheck.text) == po_amount or int(amountcheck.text) == ca_amount:
                item_match = item_match + 1

        tgt_quantity_total = 0
        for quantity_per_item_in_target in tgt_quantity:
            tgt_quantity_total = int(quantity_per_item_in_target.text) + tgt_quantity_total
            log.info("Target page individual quantity is "+ quantity_per_item_in_target.text)

        log.info("Summation of individually added item in target page "+str(total))
        log.info("How many added in target page "+str(item_match))
        assert total == src_amount #* int(veglistreview.PercentageOff().text)
        assert total == int(veglistreview.TotalAmount().text)
        assert tgt_quantity_total == src_quantity

        # At this point control goes to Country Selection page
        terms_agree = veglistreview.PlaceOrderButton()

        self.ExplicitWaitForXPATH("//select")
        dropdown = Select(terms_agree.CountryDropDown())
        time.sleep(2)
        dropdown.select_by_visible_text("India")
        time.sleep(2)
        terms_agree.ChkBoxClick().click()
        #assert terms_agree.ChkBoxClick().isSelected()
        time.sleep(2)

        terms_agree.ProceedClick().click()

    @pytest.fixture(params=HomePageDataContent.getTestData("GreenKart"))
    def getData(self, request):
        return request.param


    #@pytest.fixture(params=[{"FNAME": "Aravinth", "LNAME": "arvinth.b@gmail.com"},
    #                        {"FNAME": "Aishvarya", "LNAME": "arvinth.b@gmail.com"}])
    #def getData(self, request):
    #    return request.param