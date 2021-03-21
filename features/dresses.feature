Feature: As a user I am able to select a subcategory of dress
  """
  This is an example of selecting a value in the dropdown using selenium ActionChains
  """
  Scenario: The user is able to select casual dress
    Given I am logged into the page as "Jhon"
    When I choose casual dresses
    Then The casual dresses banner is shown

  """
  Another way to interact with a dropdown is using selenium sendkeys and sending keyboard keys to select a value in the
  dropdown
  """
  """
  Also it is possible to send javascript commands through selenium to select a specific value of the dropdown
  """