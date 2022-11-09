from pages.base_page import BasePage


class AddPlayers(BasePage)
    main_title_xpath = "//*/header//h6"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    switch_language_button_xpath = "//ul[2]/div[1]"
    log_out_button_xpath = "//ul[2]/div[2]"
    submit_button_xpath = "//*[@type= "submit"]"
    clear_button_xpath = "//*/button[2]"
    email_input_field-xpath = "//*[@name = "email"]"
    age_input_field_xpath = "//*[@type = "date"]"
    leg_select_menu = "//*[@id="mui-component-select-leg"]"
    pass