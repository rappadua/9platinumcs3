# Questions
## a.) What is duck typing, as explained in the video?
Answer: Duck typing is a concept related to dynamic typing where an object's suitability is determined by the presence of certain methods and properties, rather than its actual type or inheritance relationship. In Python, this means if an object has the required method, you can use it, regardless of what class it belongs to.
## b.) What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
Answer: The Car class needed to have a method with the exact same name as the one being called in the loop, allowing it to exhibit the required behavior without needing a parent-child relationship.

# Python Code
[Code Implementation – Duck Typing and Polymorphism Without Inheritance](https://github.com/rappadua/9platinumcs3/blob/75b060e2c3c35f54be70fc7b626b51258057b9ed/quarter2/Code%3ADuckTyping%26PolymorphismWithoutInheritanceCode.py)

## c.) How does the code in 2.2 demonstrate polymorphism?
Answer: The code demonstrates polymorphism without inheritance, also known as Duck Typing. The start_trip() function can accept an instance of any class, as long as that class implements a move() method. Even though the three classes do not share a common parent class, the function interacts with them uniformly based on the shared behavior, letting different objects respond to the same action in their own unique ways.
