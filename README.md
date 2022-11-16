# Task 1: software configuration
## Subtask 1: Why did I choose to participate in the Dare IT Challenge?
I decided to take part in this competition because Dare it, Activision and Blizzard companies gave a great opportunity to people from Ukraine :blue_heart::yellow_heart: , who are now in Poland, to gain new knowledge and find a job in the IT field.

Since childhood I have been interested in everything related to computers, studied in the field of computer technology, and recently I have found the ability to find errors in processes and mark them. I believe that these two things can be perfectly combined for me in the field of QA.

### [*Serhii Parfentiev*](https://t.me/Serejque)

# Task 2: selectors
## Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.

**scout_panel_header_xpath**
___
```
//*[@id="__next"]/form/div/div[1]/h5
//*[contains(@class, "gutter")]
//h5
```

**login_field_xpath**
___
```commandline
//*[@id="login"]
//*[@name = 'login']
```

**password_field_xpath**
___
```commandline
//*[@id="password"]
//*[@name="password"]
```

**remind_password_hyperlink_xpath**
___
```commandline
//*[@id="__next"]/form/div/div[1]/a
//*[text()="Remind password"]
//child::div/a
```

**switch_language_button_xpath**
___
```commandline
//*[contains(@class, "Menu")]
//*[@role]
//*[@aria-haspopup]
```

**sign_in_button_xpath**
___
```commandline
//*[text()='Sign in']
//*[@type = "submit"]
//*[contains(@class, "ButtonBase")]
```
## Subtask 2: Adding selectors to project

It`s done! You can check it via link https://github.com/Irgey/challenge_portfolio.serhii/blob/c55529583666d42df6711ffee92231484e7b841d/pages/login_page.py

## Subtask 3: Adding a new file

It`s done! You can check it via link https://github.com/Irgey/challenge_portfolio.serhii/blob/c55529583666d42df6711ffee92231484e7b841d/pages/dashboard.py

## Subtask 4: Adding a new file- add a match form

It`s done! You can check it via link https://github.com/Irgey/challenge_portfolio.serhii/blob/c55529583666d42df6711ffee92231484e7b841d/pages/add_players_page.py

