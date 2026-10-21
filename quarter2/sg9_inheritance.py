#define the parent class as "Publication"
class Publication:
  #the constructor method is used to initialize the title and the author attributes
  def __init__(self, title, author):
    #intializing a private title attribute for encapsulation
    self.__title = title
    self.__author = author 
  #define rhe getter method in order to retrieve the private title
  def get_title(self):
    return self.__title
  #define the setter method to update the private title
  def set_title(self, title):
    #next, assign the new title parameter to the private title attribute
    self.__title = title
  #define another getter method to retrieve the private author
  def get_author(self):
    return self.__author
  #define a setter method to update the private author
  def set_author(self, author):
    #assugn the new author parameter to the private author attribute
    self.__author = author
  #define method to print publication details
  def display_info(self):
    print(f"Title: {self.__title}")
    print(f"Author: {self.__author}")

#define the Book child class that inherits from Publication
class Book(Publication):
  #add a constructor method for Book, accepting title, author, and number_of_pages
  def __init__(self, title, author, number_of_pages):
    #cal the parent constructor
    super().__init__(title, author)
    self.__number_of_pages = 0
    #use the setter to initialize with validation check
    self.set_number_of_pages(number_of_pages)
  #use the getter method for the number of pagesages
  def get_number_of_pages(self):
    return self.__number_of_pages
  #another setter method with the data validation requirement
  def set_number_of_pages(self, number_of_pages):
    if number_of_pages <= 0:
      print("Number of pages must be positive.")
    else:
      self.__number_of_pages = number_of_pages
  #the overiden display method leveraging the parent's display_info()
  def display_info(self):
    super().display_info()
    print(f"Number of pages: {self.__number_of_pages}")

#next, the Magazine child class inherits from Publication and adds specialized attributes
class Magazine(Publication):

  def __init__(self, title, author, issue_number):
    # Call parent constructor
    super().__init__(title, author)
    self.__issue_number = issue_number
  #the getter method to retrieve the issue number
  def get_issue_number(self):
    return self.__issue_number
  #then the setter method for the issue number 
  def set_issue_number(self, issue_number):
    self.__issue_number = issue_number
  #define the method to display magazine-specific information
  def display_info(self):
    super().display_info()
    print(f"Isssue number: {self.__issue_number}")

#create objects for each class type
pub1 = Publication(
  "Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H."
)
#create a Book object with a sample title, author, and page count
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#print the Publication Information and setting invalid output for testing
print("Publication Information:")
pub1.display_info()

#gotta print the Book Information
print("\nBook Information:")
#call the set_number_of_pages with an invalid negative value to test error handling
book1.set_number_of_pages(-310)
#call the display info() on the Book object to show its details
book1.display_info()
#time to retrieve and print the valid number of pages using the getter method
print(book1.get_number_of_pages())

#print a header label for the Magazine information section
print("\nMagazine Information:")
#call the display_info() on the Magazine object to be able to show its details
mag1.display_info()
#retrieve and then print the issue number using the getter method
print(mag1.get_issue_number())
