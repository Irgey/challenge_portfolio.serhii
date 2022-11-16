import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    main_title_xpath = "//*/header//h6"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    switch_language_button_xpath = "//ul[2]/div[1]"
    log_out_button_xpath = "//ul[2]/div[2]"
    add_player_hyperlink_xpath = "//*[@href = '/en/players/add']"
    dev_team_contact_hyperlink_xpath = "//*[@target = '_blank']"
    shortcuts_section_title_xpath = "//*[text()='Shortcuts']"
    logo_scouts_panel_xpath = "//*[@title]"
    last_created_player_hyperlink_xpath = "//*/a[2]"

    def title_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_hyperlink_xpath)