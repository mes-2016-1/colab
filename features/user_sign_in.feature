
@selenium
Feature: User sign in
  In order to be able to access the system funcionalities
  As an User
  I want to be able to sign in

  Scenario: Clicking the login button and displaying login page
    When I access the URL "/"
    When I click in "Login"
    Then The browser URL should be "/account/login"