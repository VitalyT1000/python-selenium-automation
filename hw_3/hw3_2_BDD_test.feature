# Created by VitalyT1000 at 2/1/20

Feature: Test Scenarios for Search functionality

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon web-site
    Given Click Help button
    When Input Cancel order into Find more solution field
    And Click on button Go
    Then Product results for Cancel order are shown
    And Results on the page contains Cancel Items or Orders