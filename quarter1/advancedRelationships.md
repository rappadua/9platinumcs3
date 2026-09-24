# Advanced Class Relationships

## Previous Activities
[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)

## Existing System Description: 
The previous system managed user accounts and smartwatches. However, general device properties, like device_id and brand, were tied exclusively to the smartwatch, limiting expandability. Additionally, sensor hardware was modeled as a simple boolean flag rather than an internal component.

## Inheritance Relationship
Parent: Device

Child: SmartWatch

Explanation: SmartWatch IS-A specific type of Device. It inherits universal hardware attributes (device_id and brand) and methods (get_device_info()) from Device while extending functionality with step counting and sensor management.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Composition, Strong HAS-A, between SmartWatch and HeartRateSensor.

Explanation: A SmartWatch owns a HeartRateSensor. The HeartRateSensor is instantiated directly inside the SmartWatch initializer (__init__). If the SmartWatch object is destroyed, its internal HeartRateSensor instance is also destroyed.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:

## 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
I chose an inheritance relationship between Device and SmartWatch because a smartwatch fundamentally IS-A generic hardware device. Universal parameters such as hardware identification codes and manufacturer brand names apply to all smart hardware, making Device the ideal parent base class. SmartWatch inherits these general traits and adds specific behavior like fitness step counting.

## 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance eliminated the need to redefine core identifying attributes (device_id and brand) and display logic (get_device_info()) inside SmartWatch. By invoking super().__init__(device_id, brand), SmartWatch reuses the parent constructor directly, avoiding duplicate field assignments and allowing future device types (like smart rings or scales) to share the same base code.

## 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
My HAS-A relationship is Composition because the HeartRateSensor is built directly into the SmartWatch upon creation. In this system model, the sensor component cannot exist independently of the watch body. When a SmartWatch instance is initialized, it instantiates its own HeartRateSensor, and if the smartwatch object is deleted from memory, its internal sensor instance is destroyed along with it.

## 4. What is the difference between Association from Part III and the advanced relationship you implemented?
The Association in Part III represented a loose relationship where a UserAccount managed SmartWatch instances that were created independently outside the account. In contrast, the Composition relationship implemented in Part IV represents strong ownership, where SmartWatch directly manages the lifecycle and instantiation of HeartRateSensor. Furthermore, Inheritance is an IS-A relationship that shares structure, whereas Association is a HAS-A relationship between distinct objects.

## 5. How does your design follow the DRY principle?   
The design adheres to the DRY (Don't Repeat Yourself) principle by delegating general hardware property handling to Device and sensor toggling logic to HeartRateSensor. Instead of writing repetitive code across multiple classes for hardware identification or sensor tracking, each responsibility is centralized within its respective class.
