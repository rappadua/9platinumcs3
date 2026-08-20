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
    
    zodiac_index = (year - 1900) % 12
    return zodiac_signs[zodiac_index]

def main():
    try:
        user_input = input("Enter your birth year: ")
        birth_year = int(user_input)
        
        if birth_year < 1900:
            print("Invalid Year, it should not be earlier than 1900")
            return
            
        zodiac_sign = get_chinese_zodiac(birth_year)
        print(f"Your Chinese Zodiac Sign is: {zodiac_sign}")

    except ValueError:
        print("Invalid Input! Please enter a valid numerical year.")

if __name__ == "__main__":
    main()