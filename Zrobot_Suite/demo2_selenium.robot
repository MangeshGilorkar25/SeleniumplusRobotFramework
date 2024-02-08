*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1 FB Login
    Open Browser   browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s
    Go To    url=https://www.facebook.com/
    Click Element    xpath=//button[text()='Allow all cookies']
    Input Text    locator=id=email    text=hello12344444@gmail.com
    Input Password    id=pass    pass
    Click Element    name=login

TC2 FB SignUP
    Open Browser   browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s
    Go To    url=https://www.facebook.com/
    Click Element    xpath=//button[text()='Allow all cookies']
    Click Element    link=Create new account
    Select From List By Label    id=day     20
