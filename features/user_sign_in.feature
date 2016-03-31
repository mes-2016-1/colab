
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
    Given The user "colabtest" with the password "colabtest" exists
    When I fill "colabtest" in "id_username" field
    When I fill "colabtest" in "id_password" field
    When I click in "Login" button
    Then The browser URL should be "/dashboard"
    

