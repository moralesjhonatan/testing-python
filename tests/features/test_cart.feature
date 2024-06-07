Feature: Add product for products over $100

    Scenario: Add product with price greater than $100
        Given a cart
        When I add a product with a price of $150
        Then the total should be $135