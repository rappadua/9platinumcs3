# Represents general library materials containing common attributes
class Publication:

  def __init__(self, title, author):
    # Private attributes using name mangling for encapsulation
    self.__title = title
    self.__author = author  
  def get_title(self):
    return self.__title
  def set_title(self, title):
    self.__title = title  
  def get_author(self):
    return self.__author
  def set_author(self, author):
    self.__author = author
  def display_info(self):
    print(f"Title: {self.__title}")
    print(f"Author: {self.__author}")

# Inherits from Publication and adds a specialized attribute
class Book(Publication):

  def __init__(self, title, author, number_of_pages):
    # Call parent constructor
    super().__init__(title, author)
    self.__number_of_pages = 0
    # Use setter to initialize with validation check
    self.set_number_of_pages(number_of_pages)
  # Getter method for number of pagesages)
  def get_number_of_pages(self):
    return self.__number_of_pages
  # Setter method with data validation requirement
  def set_number_of_pages(self, number_of_pages):
    if number_of_pages <= 0:
      print("Number of pages must be positive.")
    else:
      self.__number_of_pages = number_of_pages
  # Overriden display method leveraging the parent's display_info()
  def display_info(self):
    super().display_info()
    print(f"Number of pages: {self.__number_of_pages}")

# Inherits from Publication and adds specialized attributes
class Magazine(Publication):

  def __init__(self, title, author, issue_number):
    # Call parent constructor
    super().__init__(title, author)
    self.__issue_number = issue_number
  # Getter method for issue number
  def get_issue_number(self):
    return self.__issue_number
  # Setter method for issue number 
  def set_issue_number(self, issue_number):
    self.__issue_number = issue_number
  def display_info(self):
    super().display_info()
    print(f"Isssue number: {self.__issue_number}")

# Creating objects for each class type
pub1 = Publication(
  "Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H."
)
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# Printing Publication Information
print("Publication Information:")
pub1.display_info()

# Printing Book Information
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

# Printing Magazine Information
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
