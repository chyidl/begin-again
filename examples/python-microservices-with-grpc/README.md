# Microservice gRPC Python

## The Goal
    * Implement microservices in Python that communicate with one another over gRPC
    * Implement middleware to monitor microservices
    * Unit test and integration test your microservices and middleware
    * Deploy microservices to a Python production environment with Kubernetes

## Why Microservices?
    * Modularity: 
    * Flexibility:
    * Robustness:
    * Ownership

## The Microservice-Monolith Trade-Off?
> The typical Silicon Valley startup cycle is to begin with a monolith to enable quick iteration as the business finds a product fit with customers. After the company has a successful product and hires more engineers, it's time to start thinking about microservices. Don't implement them too soon, but don't wait too long.

## Online bookstore Microservices:
    * Marketplace: serves the logic for the user to navigate around the site
    * Cart: keeps track of what the user has put in their cart and the checkout flow.
    * Transactions handles payment processing and sending receipts.
    * Inventory: provides data about which books are in stock.
    * User Account: manages user signup and account details, such as changing their password.
    * Reviews: stores book ratings and reviews entered by users.

## Define two microservices
| Microservices| Detail|
|:-------------|:------|
|[Marketplace](./marketplace/README.md)|display a list of books to the user|
|[Recommendations](./recommendations/README.md)|provides a list of books in which the user may be interested|