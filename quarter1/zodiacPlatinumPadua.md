# Chinese Zodiac Finder Exercise

**Name:** Rayne Ashree P. Padua  
**Section:** 9 - Platinum  
**Date:** August 20, 2026  

---

## 1. Problem Statement & Requirements
The goal of this exercise is to build a program that accepts a user's birth year and determines their Chinese Zodiac sign based on a baseline year of 1900.

**Requirements:**
* Baseline year is **1900** (Rat).
* Validate user input; input must not be earlier than 1900.
* Output an error message and terminate if the input is invalid.
* Zodiac signs repeat every 12 years in this exact cycle:
  1. Rat (鼠 / Shǔ)
  2. Ox (牛 / Niú)
  3. Tiger (虎 / Hǔ)
  4. Rabbit (兔 / Tù)
  5. Dragon (龙 / Lóng)
  6. Snake (蛇 / Shé)
  7. Horse (马 / Mǎ)
  8. Goat (羊 / Yáng)
  9. Monkey (猴 / Hóu)
  10. Rooster (鸡 / Jī)
  11. Dog (狗 / Gǒu)
  12. Pig (猪 / Zhū)

---

## 2. Python Code Solution

```python
def get_chinese_zodiac(year):
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]
    return zodiac_signs[(year - 1900) % 12]

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        
        if birth_year < 1900:
            print("Invalid Year, it should not be earlier than 1900")
            return
            
        zodiac_sign = get_chinese_zodiac(birth_year)
        print(f"Your Chinese Zodiac Sign is: {zodiac_sign}")

    except ValueError:
        print("Invalid Input! Please enter a valid numerical year.")

if __name__ == "__main__":
    main()