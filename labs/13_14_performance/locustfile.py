from locust import HttpUser, task, between
import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

class AppUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        """Setup: Create and login user"""
        username = f"loadtest_{random_string()}"
        password = "test1234"
        
        # Signup
        self.client.post("/signup", json={
            "username": username,
            "password": password
        })
        
        # Login
        response = self.client.post("/login", json={
            "username": username,
            "password": password
        })
        
        if response.status_code == 200:
            self.token = response.json()["access_token"]
        else:
            self.token = None
    
    @task(5)
    def view_products(self):
        """Most common: viewing products"""
        if self.token:
            self.client.get("/products", 
                headers={"Authorization": f"Bearer {self.token}"},
                name="/products")
    
    @task(2)
    def view_user_profile(self):
        """Check own products"""
        if self.token:
            self.client.get("/user",
                headers={"Authorization": f"Bearer {self.token}"},
                name="/user")
    
    @task(1)
    def add_product_to_cart(self):
        """Less frequent: adding products"""
        if self.token:
            product_id = random.randint(1, 10)
            self.client.post(f"/user/product/{product_id}",
                headers={"Authorization": f"Bearer {self.token}"},
                name="/user/product/[id]")