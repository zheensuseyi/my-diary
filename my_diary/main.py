import random
from pathlib import Path

# Define the required lists
greetings = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']
daily_wisdom = [
        "As you sow, so shall you reap.",
        "You get what you give.",
        "Life is a boomerang; what you send out, you get back.",
        "The energy you put out is the energy you receive.",
        "What we do today echoes in eternity.",
        "Character is who you are when no one is watching.",
        "We rise by lifting others.",
        "Treat others as you wish to be treated.",
        "Success is not measured by what you achieve, but by the impact you make.",
        "Every action has an equal and opposite reaction.",
        "When you light a lamp for someone, it brightens your path too.",
        "If you want to go fast, go alone. If you want to go far, go together.",
        "The journey of a thousand miles begins with a single step.",
        "Hurt people hurt people; healed people heal people.",
        "In the end, we only regret the chances we didn’t take.",
        "It’s not what happens to you, but how you react to it that matters.",
        "A kind word is never lost; it keeps going and growing.",
        "Integrity is doing the right thing, even when no one is watching.",
        "If you don’t stand for something, you’ll fall for anything.",
        "Patience is bitter, but its fruit is sweet.",
        "In helping others, we help ourselves.",
        "The best way to predict your future is to create it.",
        "When one door closes, another opens.",
        "Gratitude turns what we have into enough.",
        "Do what is right, not what is easy.",
        "One small act of kindness can make a big difference.",
        "When you stop chasing the wrong things, the right things catch up to you.",
        "A wise man learns more from his enemies than a fool from his friends.",
        "Peace begins with a smile.",
        "Life is a mirror; it reflects what you project.",
        "No act of kindness, no matter how small, is ever wasted.",
        "You cannot control the wind, but you can adjust your sails.",
        "Your vibe attracts your tribe.",
        "Success is not final; failure is not fatal: it is the courage to continue that counts.",
        "Don't count the days; make the days count.",
        "Dream big, start small, act now.",
        "Don’t watch the clock; do what it does. Keep going.",
        "Fall seven times, stand up eight.",
        "What you seek is seeking you.",
        "Growth is uncomfortable because you’ve never been here before.",
        "Don't just aspire to make a living; aspire to make a difference.",
        "The best way out is always through.",
        "It’s not how far you fall, but how high you bounce that counts.",
        "Do not wait to strike till the iron is hot, but make it hot by striking.",
        "A journey of a thousand miles begins with a well-defined path.",
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Every day is a second chance.",
        "The only limit to our realization of tomorrow is our doubts of today.",
        "The best view comes after the hardest climb.",
        "You don’t need to see the whole staircase; just take the first step.",
        "Stay committed to your decisions, but flexible in your approach.",
        "Great things never come from comfort zones.",
        "Sometimes you win, sometimes you learn.",
        "Don't be pushed by your problems. Be led by your dreams.",
        "Your only limit is you.",
        "Be stubborn about your goals, and flexible about your methods.",
        "A diamond is a chunk of coal that did well under pressure.",
        "Do not let what you cannot do interfere with what you can do.",
        "The secret of getting ahead is getting started.",
        "A river cuts through rock, not because of its power but because of its persistence.",
        "Happiness is not by chance, but by choice.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "When things go wrong, don’t go with them.",
        "Believe you can and you're halfway there.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Life isn't about finding yourself. Life is about creating yourself.",
        "Your life does not get better by chance, it gets better by change.",
        "You don’t have to be great to start, but you have to start to be great.",
        "Start where you are. Use what you have. Do what you can.",
        "Success usually comes to those who are too busy to be looking for it.",
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Difficult roads often lead to beautiful destinations.",
        "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "We cannot solve our problems with the same thinking we used when we created them.",
        "Opportunities don't happen. You create them."
    ]
def choice_one():
    entry_title = input("Enter Entry Title (Only Use Letters For Your Title):\n")
    if entry_title.isalpha():
        random_greeting = random.choice(greetings)
        desktop = Path.home() / 'Desktop'
        folder_path = desktop / 'Diary Entries'
        folder_path.mkdir(exist_ok=True)
        file_path = folder_path / entry_title
        print("")
        print("Soda Says: " + random_greeting)
        user_entry = input("Type Your Entry, Press Enter Once Finished: \n")
        print("Entry Added to Diary!")
        with open(file_path, 'w') as file:
            file.write(user_entry)
        print(f"File saved at: {file_path}")
    else:
        print("")
        print("Soda Says: Please Enter a Valid Entry Title That Only Contains Letters.\n")

def choice_two():
    desktop = Path.home() / 'Desktop'
    folder_path = desktop / 'Diary Entries'
    if not folder_path.exists():
        print(f"The folder '{folder_path}' does not exist.")
        print("Please Create a New Entry First!\n")
    else:
        for file_path in folder_path.iterdir():
            if file_path.is_file():
                print(f"Entry Title: {file_path.name}")
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"Content: {content}")  # Print content

def choice_three():
    random_wisdom = random.choice(daily_wisdom)
    print("")
    print("Soda Says: " + random_wisdom)
    print("")

def choice_four():
    print("++++++++++++++++++++++COMMON QUESTIONS++++++++++++++++++++++")
    print("Question: Where Are My Diary Entries!")
    print("Soda Says: They should be on your desktop in a folder called 'Diary Entries'. Once you have opened that folder you can view all of the entries you have created!\n")
    print("Question: How Do I Delete or Edit an Entry?")
    print("Soda Says: The easiest way to do that would be to go to the 'Diary Entries' folder in your desktop and then either delete or edit the desired entry from there!\n")
    print("Question: How Do I Contact the Creator of This Program?")
    print("Soda Says: I believe the creator can be reached at suseyihzheen@gmail.com!")
    print("++++++++++++++++++++++COMMON QUESTIONS++++++++++++++++++++++\n")

def main():
    art = """⢰⣾⣿⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣏⣿⣿
⠸⣿⣿⣿⣇⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣿⣿⠿⠋
⠀⠀⠉⢻⡅⠈⠉⠙⠓⠶⢦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠶⠚⠛⠉⠁⠠⣾⠇⠀⠀
⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠓⠲⠦⢤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀
⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀
⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⣀⣀⣤⡴⠶⠶⠶⠶⠶⠦⣤⣀⣀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠉⠁⠀⠀⠂⠀⠀⠀⠀⠀⠒⠀⠉⠙⠛⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣴⠶⠛⠉⠉⠉⠛⠷⣤⡀⠀⠀⠀⠀⠙⢷⣄⠀⡀⠀⠀⢸⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢡⣶⣶⡄⠀⠀⢠⡶⣮⢻⣆⠀⠀⠀⠀⠀⠻⣦⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣸⣿⣿⠃⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠙⣷⠶⠿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⠶⣶⣶⡶⠄⠀⠀⠀⠀⠀⠀⠀⣀⡴⠾⠿⢯⣽⣿⣷⣤⢠⡆⠠⡄⣽⣿⣿⡿⠟⠛⢿⣆⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠁⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠉⠉⠻⠿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⢙⢷⣄⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⢀⡴⠋⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⡍⣈⣿⣆⠀⠼⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢰⡟⠁⢀⣀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⢀⠀⢀⠀⠀⠀⢸⣿⣿⣿⣿⡅⠀⢻⡆⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⢰⡟⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⢀⠄⡰⠋⡴⠃⡴⠁⠀⠘⣿⣿⣿⣿⡇⠀⠀⣿⡞⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⠀⠀⠀⣾⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠃⠀⠀⢀⠞⠀⠊⢀⣈⣀⠀⠀⠀⠙⠿⠿⠟⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣎⠀⠀⣿⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠘⠻⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡂⣀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠖⠒⠒⠒⠒⠒⠒⠒⠒⠒⠶⠶⡦⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢯⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣧⣄⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣷⠚⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠛⢲⣴⣾⣿⡿⠿⣶⡶⠖⠉⠉⠉⠙⢦⠀⠀⠀⠀⠀⠀⣠⠞⠉⠙⠻⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⠟⠁⢠⠏⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠙⣿⢿⡏⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⢸⠀⠛⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠈⠦⣀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⣀⡀⣀⣠⠴⠊⠳⠶⠶⠶⠶⠶⠶⠤⠤⠤⠤⠼⢹⠒⠒⠋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠤⠤⠤⣤⠀⠀⠀⢀⣿⠀⠉⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    print(art)
    game_loop = True
  
    while game_loop:
        print("****************Menu****************")
        print("1. New Entry")
        print("2. View Previous Entries")
        print("3. Words Of Wisdom")
        print("4. FAQ")
        print("****************Menu****************")
        print("Press 'Q' to Exit\n")
        n = input("Enter Your Choice: \n").lower()
        if n == '1':
            choice_one()
        elif n == '2':
            choice_two()
        elif n == '3':
            choice_three()
        elif n == '4':
            choice_four()
        elif n == 'q':
            game_loop = False
        else:
            print("Please enter a valid choice!")

main()

