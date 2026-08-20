# ILA 3-1: Applying the Four Pillars of OOP

**Name:** Rayne Ashree P. Padua  
**Section:** 9 - Platinum  
**Date:** August 20, 2026

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation bundles product properties—such as `productName`, `price`, and `stockQuantity`—together within a single `Product` class while restricting direct external access to them by making fields private. Changes to data are made exclusively through public methods like `updateStock()` or `setPrice()`, preventing invalid states such as negative inventory counts. This improves system integrity and program organization by centralizing product validation logic inside the class itself.

### 2. Abstraction
Abstraction hides complex backend implementation details and exposes only essential operations to the store manager. For instance, an `InventoryManager` class can provide a simple public method like `restockItem(productID, quantity)` without revealing how internal array manipulation or database updates take place under the hood. This reduces overall system complexity, making the codebase easier to maintain and interface with without worrying about low-level operations.

### 3. Inheritance
Inheritance allows specialized product types to inherit general properties and behaviors from a base `Product` class. For example, a `PerishableProduct` class can inherit attributes like `productName` and `price` from `Product` while adding its own specific property, `expirationDate`. This eliminates duplicate code, promotes reusability, and keeps the inventory structure neat as new product categories are introduced.

### 4. Polymorphism
Polymorphism allows different product types to implement shared methods in their own unique ways. For example, both `StandardProduct` and `PerishableProduct` can inherit a `calculateDiscount()` method, but `PerishableProduct` can override it to apply larger discounts to items nearing expiration. This enhances flexibility, enabling the main inventory system to process diverse product objects uniformly through a single interface call.

## Reflection
Among the four pillars, Encapsulation would be the most useful for improving the sari-sari store inventory system. Since store inventory relies heavily on accurate stock counts and pricing, bundling these variables within a class and enforcing access restrictions via setter methods prevents accidental corruption, such as setting a negative stock value or invalid price. This direct control ensures data consistency and stability across daily store transactions.