
@selenium
Feature: User sign in
  In order to be able to access the system funcionalities
  As an User
  I want to be able to sign in

  Scenario: Clicking the login button and displaying login page
    When I access the URL "/"
    When I click in "Login"
    Then The browser URL should be "/account/login"

  Scenario: Sign in with a valid user
    When I access the URL "/"
    When I click in "Login"
    Given The user "colabtest" with the password "colabtest" that is "active"
    When I fill "colabtest" in "id_username" field
    When I fill "colabtest" in "id_password" field
    When I click in "Login" button
    Then The browser URL should be "/dashboard"

  Scenario: Sign in with an unregistered user
    When I access the URL "/"
    When I click in "Login"
    When I fill "unregistered" in "id_username" field
    When I fill "any" in "id_password" field
    When I click in "Login" button
    Then The browser URL should be "/account/login"
    Then I should see "Please correct the error below and try again" in "main-content"

  Scenario: Sign in with a inactive user
    When I access the URL "/"
    When I click in "Login"
    Given The user "colabtest" with the password "colabtest" that is "inactive"
    When I fill "colabtest" in "id_username" field
    When I fill "colabtest" in "id_password" field
    When I click in "Login" button
    Then The browser URL should be "/account/login"
    Then I should see "This account is inactive" in "main-content"

  Scenario: Sign in with no user information given
    When I access the URL "/"
    When I click in "Login"
    When I click in "Login" button
    Then The browser URL should be "/account/login"
    Then The field "id_username" should have an error
    Then The field "id_password" should have an error
  
  Scenario: Sign in with no password given
    When I access the URL "/"
    When I click in "Login"
    When I fill "colabtest" in "id_username" field
    When I click in "Login" button
    Then The browser URL should be "/account/login"
    Then The field "id_password" should have an error
  
  Scenario: Sign in with no username given
    When I access the URL "/"
    When I click in "Login"
    When I fill "colabtest" in "id_password" field
    When I click in "Login" button
    Then The browser URL should be "/account/login"
    Then The field "id_username" should have an error