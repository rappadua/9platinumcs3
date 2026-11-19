# create parent class named "Patient"
class Patient: 
# define and initialize self, name, and bill_amount 
  def __init__(self, name, bill_amount):
# encapsulate the private attributes by using underscores
    self.__name = name
    self.__bill_amount = bill_amount

# input the getter methods for name
  def get_name(self):
    return self.__name

# inout the setter methods for name
  def set_name(self):
    self.__name = name

# input the getter methods for bill amount
  def get_bill_amount(self):
    return self.__bill_amount

# input the setter methods for bill amount
  def set_bill_amount(self):
    self.__bill_amount = bill_amount

# add the base calculation method, no discounts for regular patients
  def calculate_bill(self):
    return self.__bill_amount

# this is the method that displays the patient type for regular patients
  def display_patient_type(self):
    print("Patient Type: Regular Patient")

# create child class 1
class SeniorPatient(Patient):
# override the calculate_bill to apply a 20% discount for the senior patient
  def calculate_bill(self):
#the original bill amount is multiplied by (1-0.20)
    return self.get_bill_amount() * 0.80

# override the display_patient_type for senior citizens/patients
  def display_patient_type(self):
    print("Patient Type: Senior Patient")

# create child class 2
class PhilHealthPatient(Patient):
# override the calculate_bill to apply a 15% discount for the phil health patient
  def calculate_bill(self):
# the original bill amount is multiplied by (1-0.15)

# testing or execution
if __name__ == "__main__":
    print("Hospital Billing System")
    print("-----------------------")

    # this creates the patient's instances with a base bill of ₱15,000.00
    # each object represents a different patient type with an original bill of ₱15,000.00 (Regular, Senior, or PhilHealth)
    patients = [
        Patient("Juan Dela Cruz", 15000.00),
        SeniorPatient("Maria Santos", 15000.00),
        PhilHealthPatient("Pedro Reyes", 15000.00)
    ]

    # next, loop through each patient object in the "patients" list one by one
    for p in patients:
        # here, retrieve and print the patient's name using the getter method
        print(f"Patient Name:  {p.get_name()}")
        # polymorphism is in action here, python automatically calls the correct 'display_patient_type()' method 
        p.display_patient_type()
        # retrieve the original bill amount using the getter, then then format it as currency by using ₱ with commas and 2 decimal places
        print(f"Original Bill: ₱{p.get_bill_amount():,.2f}")
        # we call "calculate_bill()" then the result is formatted as currency and printed with a blank line underneath
        print(f"Final Bill: ₱{p.calculate_bill():,.2f}\n")
