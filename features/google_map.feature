@FSE
Feature: Google Map

  Scenario Outline: Google Map Search Bar
    Given He Open Google Map
    When He Searched "<searched_for>"
    Then He Extract Information Of First "<count_of_restaurant>" Restaurants
    And He Successfully Make CSV File Of All Information
    Examples:
      | searched_for                 | count_of_restaurant |
      | restaurant near me           | 5                  |
      | restaurant near marathahalli | 7                 |
