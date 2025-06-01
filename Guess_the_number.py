import random

target = random.randint(1, 100)
negative_count = 0
xp = 0
level = 1
xp_to_next_level = 100
attempts = 0

def show_xp_bar(current_xp, xp_needed, level):
    bar_length = 20
    filled_length = int(bar_length * current_xp // xp_needed)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    print(f"XP: [{bar}] {current_xp}/{xp_needed} | Level: {level}")

while True:
    user_input = input("Guess the target or Quit(Q): ")

    if user_input.upper() == "Q":
        break

    try:
        user_choice = int(user_input)

        if user_choice < 0:
            negative_count += 1
            if negative_count == 3:
                print("Trying to break the game with negatives? Not that easy!")
            else:
                print("Oops! Negative numbers aren't allowed. Try guessing a positive number!")
            continue

        attempts += 1

        if user_choice == target:
            
            if attempts < 4:
                print("🏆 You guessed it in less than 4 attempts! Bonus XP awarded!")
                xp += 20
            else:
                print("✅ Correct guess! XP awarded.")
                xp += 10

           
            while xp >= xp_to_next_level:
                xp -= xp_to_next_level
                level += 1
                print(f"🎉 Level up! You're now Level {level}!")

            show_xp_bar(xp, xp_to_next_level, level)
            print("✅ Success: Correct Guess!!")
            break

        else:
            if user_choice < target:
                print("📉 Number too small. Try a bigger guess.")
            else:
                print("📈 Number too large. Try a smaller guess.")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number or 'Q' to quit.")

print("-----GAME OVER-----")
