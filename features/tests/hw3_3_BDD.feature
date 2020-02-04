# Created by VitalyT1000 at 2/3/20
Feature: Test Scenarios for Your Shopping Cart is empty

  Scenario: Verifies that Your Amazon Shopping Cart is empty
    Given Open Amazon web-site
    When Click Cart icon
    Then Check the Cart have to be empty
