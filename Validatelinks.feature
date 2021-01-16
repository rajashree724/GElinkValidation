Feature: GE links validation

  Background: common steps
    Given start chrome browser
    When open GE homepage

  Scenario: Our Products Link validation
    Then click Our Products link
    And verify title

  Scenario: Our Approach Link validation
    Then click Our Approach link
    And verify page title

  Scenario: Resources Link validation
    Then click Resources link
    And verify ptitle

  Scenario: About Us Link validation
    Then click About Us link
    And verify titlep

  Scenario: contact Link validation
    Then click contact link
    And verify title of page
