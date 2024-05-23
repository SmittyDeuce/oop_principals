# OOP Principles

## Overview

here is my attempt at Coding Temple's Object-Oriented Programming (OOP) principles, including encapsulation, inheritance, and method overriding, using Python. The assignment is divided into two main parts: Personal Budget Management and an E-commerce Product Catalog System.

### Table of Contents
1. [Personal Budget Management](#personal-budget-management)
    - [BudgetCategory Class](#budgetcategory-class)
    - [Usage Examples](#usage-examples)
2. [E-commerce Product Catalog System](#e-commerce-product-catalog-system)
    - [Product Class and Subclasses](#product-class-and-subclasses)
    - [Usage Examples](#usage-examples-1)

## Personal Budget Management

### BudgetCategory Class

This part of the project focuses on encapsulation, demonstrating how to manage budget categories securely. The `BudgetCategory` class includes private attributes for category name and budget amount, accessible and modifiable through public methods (getters and setters). Additionally, it includes methods to add expenses and display category details.

#### Getters and Setters

- `get_category`: Returns the name of the budget category.
- `get_budget`: Returns the allocated budget for the category.
- `set_budget`: Allows updating the budget with validation to ensure it's a positive integer.
- `set_category`: Allows updating the category name with validation to ensure it's non-empty and contains no digits.

#### Expense Management

- `get_expenses`: Returns a dictionary of all expenses added to the category.
- `add_expenses`: Adds a new expense to the category, updates the remaining budget, and validates that the expense does not exceed the budget.

#### Display Details

- `display_details`: Prints the category name, remaining budget, and a list of expenses.

### Usage Examples

- Create a `BudgetCategory` instance for "vacation" with a budget of 1000.
- Add an expense for "gas" costing 800.
- Display the remaining budget and details of all expenses.

## E-commerce Product Catalog System

### Product Class and Subclasses

This part of the project demonstrates inheritance and method overriding. A base `Product` class is created with common attributes, and subclasses for specific product types are implemented with additional attributes and overridden methods.

#### Product Class

- Common attributes: product ID, name, price.
- Method to display product information.

#### Book Subclass

- Inherits from `Product`.
- Additional attributes: genre, author.
- Overridden method to display product information, including the genre and author.

#### Electronic Subclass

- Inherits from `Product`.
- Additional attributes: built-in Wi-Fi, type.
- Overridden method to display product information, including Wi-Fi capability and type.

#### Clothing Subclass

- Inherits from `Product`.
- Additional attributes: size, color.
- Overridden method to display product information, including size and color.

### Usage Examples

- Create a `Clothing` instance for a "Pro Club" shirt with size "Large" and color "White".
- Create an `Electronic` instance for a "SideKick" phone with built-in Wi-Fi.
- Create a `Book` instance for "Hunger Games" with genre "dystopian" and author "Collins".
- Display information for each product using the overridden methods to show both common and specific attributes.