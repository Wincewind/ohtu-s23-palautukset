*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  validun  password1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  password1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  password1234
    Output Should Contain  The username must consist of the letters a-z and its length must be at least 3


Register With Enough Long But Invald Username And Valid Password
    Input Credentials  kalle123  password1234
    Output Should Contain  The username must consist of the letters a-z and its length must be at least 3


Register With Valid Username And Too Short Password
    Input Credentials  validun  a1
    Output Should Contain  The password must be at least 8 characters long and contain 1 or more characters other than a-ö

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  validun  passwordonetwothreefour
    Output Should Contain  The password must be at least 8 characters long and contain 1 or more characters other than a-ö

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command