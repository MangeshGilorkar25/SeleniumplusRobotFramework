*** Settings ***
Library     SeleniumLibrary
Test Setup  Open Browser   browser=chrome
Test Teardown   Close Browser

*** Keywords ***
Setup Browser
    [Arguments]     ${browser_name}
    Open Browser    browser=${browser_name}



*** Test Cases ***
TC1 FB Login
    Open Browser   browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s
    Go To    url=https://www.facebook.com/
    #Click Element    xpath=//button[text()='Allow all cookies']
    Input Text    locator=id=email    text=hello12344444@gmail.com
    Input Password    id=pass    pass
    Click Element    name=login

TC2 FB SignUP
    Open Browser   browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s
    Go To    url=https://www.facebook.com/
    #Click Element    xpath=//button[text()='Allow all cookies']
    Click Element    link=Create new account
    Select From List By Label    id=day     20

TC3 Tabs
    Open Browser   browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s
    Go To    url=https://www.db4free.net/
    Click Element    partial link=phpMyAdmin
    #@{window_handles}  get window handles
    Switch Window  phpMyAdmin
    Input Text    locator=id=input_username    text=admin
    Input Password    id=input_password    admin123
    Click Element    id=input_go
    Element Should Contain    id=pma_errors     Access denied for user
    #[Teardown]  Close Browser
