# **Emarket API Documentation**

## Documentation

For detailed documentation, please [click here](https://drive.google.com/file/d/1BEq6rNTqfNYjr8zezsuOVz8kvXz08ouO/view?usp=sharing).


## **Overview**

Emarket is an e-commerce platform built with Django, supporting the following functionalities:
1. User Account Management
2. Order Processing
3. Product Management
4. Review System
5. JWT Authentication for secure API access

## **Apps Overview**

The project contains three primary apps:

1. **Account App**: Manages user registration, login, profile updates, and password resets.
2. **Order App**: Handles orders, including order creation, updates, and order item management.
3. **Product App**: Manages products, categories, and user reviews.

---

## **Account App**

### **URLs**

- `/register/` - **Register a new user**
  - **Method**: POST
  - **Description**: Registers a new user in the system.
  
- `/userinfo/` - **Get current user information**
  - **Method**: GET
  - **Description**: Retrieves information about the currently logged-in user.
  
- `/userinfo/update/` - **Update user information**
  - **Method**: PUT
  - **Description**: Allows the user to update their profile.
  
- `/forgot_password/` - **Request password reset**
  - **Method**: POST
  - **Description**: Sends a password reset token to the user's email.
  
- `/reset_password/<str:token>/` - **Reset password**
  - **Method**: POST
  - **Description**: Resets the user’s password using the provided token.

### **Models**

- **Profile Model**
  - **Fields**:
    - `user`: One-to-one relationship with Django's built-in `User` model.
    - `reset_password_token`: Stores the token for resetting passwords.
    - `reset_password_expire`: Stores the expiration time of the token.
    
  - **Signals**:
    - A `post_save` signal is used to create a `Profile` whenever a new `User` is created.

---

## **Order App**

### **URLs**

- `/orders/new/` - **Create a new order**
  - **Method**: POST
  - **Description**: Creates a new order for the authenticated user.
  
- `/orders/` - **Get all orders**
  - **Method**: GET
  - **Description**: Retrieves all orders of the authenticated user.
  
- `/orders/<str:pk>/` - **Get order details**
  - **Method**: GET
  - **Description**: Retrieves a specific order by its ID.
  
- `/orders/<str:pk>/process/` - **Process an order**
  - **Method**: PUT
  - **Description**: Updates the status of an order to `Shipped` or `Delivered`.
  
- `/orders/<str:pk>/delete/` - **Delete an order**
  - **Method**: DELETE
  - **Description**: Deletes an order by its ID.

### **Models**

- **Order Model**
  - **Fields**:
    - `city`, `zip_code`, `street`, `state`, `country`, `phone_no`: Address and contact details.
    - `total_amount`: Total cost of the order.
    - `payment_status`: Payment status (`Paid`, `Unpaid`).
    - `payment_mode`: Payment method (`COD`, `Card`).
    - `status`: Order status (`Processing`, `Shipped`, `Delivered`).
    - `user`: Foreign key linking the order to a user.
    - `createAt`: Date when the order was created.
    
- **OrderItem Model**
  - **Fields**:
    - `product`: Reference to the ordered product.
    - `order`: Reference to the related order.
    - `name`, `quantity`, `price`: Details about the product in the order.
    
---

## **Product App**

### **URLs**

- `/products/` - **Get all products**
  - **Method**: GET
  - **Description**: Retrieves all products available in the store.
  
- `/products/<str:pk>/` - **Get product by ID**
  - **Method**: GET
  - **Description**: Retrieves details of a specific product by its ID.
  
- `/products/new` - **Create a new product**
  - **Method**: POST
  - **Description**: Adds a new product to the database.
  
- `/products/update/<str:pk>/` - **Update a product**
  - **Method**: PUT
  - **Description**: Updates the details of an existing product.
  
- `/products/delete/<str:pk>/` - **Delete a product**
  - **Method**: DELETE
  - **Description**: Deletes a specific product by its ID.
  
- `/products/<str:pk>/reviews` - **Create a product review**
  - **Method**: POST
  - **Description**: Allows users to create a review for a product.
  
- `/products/<str:pk>/reviews/delete` - **Delete a product review**
  - **Method**: DELETE
  - **Description**: Deletes a review for a specific product.

### **Models**

- **Product Model**
  - **Fields**:
    - `name`, `description`, `price`, `brand`: Basic product information.
    - `category`: Product category (`Computers`, `Food`, `Kids`, `Home`).
    - `ratings`: Product ratings.
    - `stock`: Number of items available.
    - `user`: Foreign key linking the product to its creator.
    
- **Review Model**
  - **Fields**:
    - `product`: Foreign key to the product.
    - `user`: Foreign key to the user who made the review.
    - `rating`, `comment`: Rating and comment of the product.
    - `createAt`: Date the review was created.

---

## **Authentication**

The project uses **JWT (JSON Web Token)** for authentication, ensuring secure API communication.

- **Token URL**: `/api/token/`
  - **Method**: POST
  - **Description**: Returns a JWT token for authentication.
  - **Required Fields**: `username`, `password`.

---

## **Error Handling**

Custom error handling views are defined in the `utils` app:
- **404 Error**: `handler404 = 'utils.error_view.handler404'`
- **500 Error**: `handler500 = 'utils.error_view.handler500'`

---

## **Installation & Setup**

1. Clone the repository and navigate into the project directory.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the migrations using:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser using:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## **API Endpoints Overview**

- **Account**: `/api/account/`
- **Orders**: `/api/orders/`
- **Products**: `/api/products/`
- **JWT Token**: `/api/token/`

