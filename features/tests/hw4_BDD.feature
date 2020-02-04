# Created by VitalyT1000 at 2/4/20
Feature: Test Scenarios for Amazon Shopping Cart is empty

  Scenario: Add items to the Cart and Verifies it there
    Given Open Amazon web-site
    When Search input fill Toys
    And Click search button
    And Choose the first item
    And Add Toys to the Cart
    When Click Cart icon
    Then Check the Cart is NOT empty