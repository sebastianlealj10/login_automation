Feature: As a registered user I am able to login
  """
  Rainy day scenarios
  """
  Scenario: The user is able to login with slow internet connexion
    Given I am a registered as "Jhon"
    When My internet connexion is "25kb/s"
    And I login into the page
    Then I am in the home page

  Scenario: The user is able to login with from a mobile browser
    Given I am a registered as "Jhon"
    And I enter to the page from a mobile browser
    When I login into the page
    Then I am in the home page
  """
  Edge scenarios
  """
 Scenario: The user is able to login with a password greater than 25 characters
    Given I am a registered as "Long password user"
    When I login into the page
    Then I am in the home page