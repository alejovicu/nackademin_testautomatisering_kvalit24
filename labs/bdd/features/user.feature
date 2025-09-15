Feature: User
    A site where you can publish your articles 

    Scenario: Login as valid user
        Given i am an authenticated user 
        When i log in into the application 
        Then i should see all my products
        
    