*** Settings ***
Library    DateTime

*** Variables ***
${My_NAME}      Mangesh Gilorkar
${MOBILE}       561651561132121

*** Test Cases ***
TC1
    Log To Console    message=Mangesh Gilorkar
    Log To Console    Welcome to robot framework

TC2
    Log To Console    ${My_NAME}
    Log To Console    ${MOBILE}
    ${value}    Set Variable    45
    Log To Console    ${value}

TC3
    ${radius}   Set Variable    10
    ${pi}     Set Variable  3.14
    ${res}    Evaluate   ${pi}*${radius}*${radius}
    Log To Console  ${res}

TC4
    ${date}     Get Current Date
    Log To Console    ${date}
    Log    ${date}