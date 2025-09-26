Feature: User​
    Validates user creation and authentication

Scenario: Succesful Login
    Given I am an authenticated user​
    When I log in into the application​
    Then I should see all my products