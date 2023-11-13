*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App and Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Input Text      password_confirmation  kalle123 
    Click Button    Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid password
    Set Username  a
    Set Password  kalle123
    Input Text    password_confirmation  kalle123 
    Click Button  Register
    Register Should Fail With Message  The username must consist of the letters a-z and its length must be at least 3

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle
    Set Password  kalleonetwothree
    Input Text    password_confirmation  kalleonetwothree 
    Click Button  Register
    Register Should Fail With Message  The password must be at least 8 characters long and contain 1 or more characters other than a-ö

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Input Text    password_confirmation  kalle456 
    Click Button  Register
    Register Should Fail With Message  Password and its confirmation did not match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Input Text    password_confirmation  kalle123 
    Click Button  Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle
    Input Text    password_confirmation  kalle 
    Click Button  Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset App and Go To Register Page
    Go To Register Page
    Reset Application

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}