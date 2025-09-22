Feature: User Products

    Scenario: User with no products can see it has no products
        Given a User with username "USERNAME1" and password "PASS_USER1"
        When the user logs in
        Then the user should see no products

    
    Scenario: User with products can see their products
        Given a user with username "USERNAME2" and password "PASS_USER2"
        When the user logs in
        Then the user should see their products
        And the product list should contain "Laptop" 