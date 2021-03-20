Feature: As a registered user I am able to login
  Scenario Outline: The registered users are able to login
    Given I am a registered with the <user>
    When I login into the page
    Then I am in the home page
    Examples:
      | user  |
      | Jhon  |
      | Maria |