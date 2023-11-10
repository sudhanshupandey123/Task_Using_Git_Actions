@Desktop
Feature: Company Details

  Scenario Outline: Extracting Company Details
    Given User is On Google Page
    When He Searched For Company "<company_name>"
    And He Extract Information
    Then Successfully Make Csv file of all data
    Examples:
      | company_name                             |
      | sulopa                                   |
      | fluree                                   |
      | g7 cr technologies india private limited |
