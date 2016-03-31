@selenium
Feature: User Profile Edition
    In order to update my personal information
    As an User
    I want to be able to edit my profile

    Scenario: Edit profile without required information
        Given I am logged in as "john"
        When I open the user menu
        When I click in "My Profile"
        When I click in "  Edit Profile"
        When I fill " " in "id_first_name" field
        When I fill " " in "id_last_name" field
        When I click in "Update" button
        Then The field "id_first_name" should have an error
        Then The field "id_last_name" should have an error
