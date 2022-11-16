from pages.base_page import BasePage


class AddPlayers(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    main_title_xpath = "//title"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    switch_language_button_xpath = "//ul[2]/div[1]"
    log_out_button_xpath = "//ul[2]/div[2]"
    submit_button_xpath = "//*[@type= 'submit']"
    clear_button_xpath = "//*/button[2]"
    email_input_field_xpath = "//*[@name = 'email']"
    age_input_field_xpath = "//*[@type = 'date']"
    leg_select_menu = "//*[@id='mui-component-select-leg']"


    def title_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title
