import pyttsx3

# Print Welcome to GitHub Universe 2022!
print("Welcome to GitHub Universe 2022!")

# Create function to speak Welcome to GitHub Universe 2022!
def speak():
    engine = pyttsx3.init()
    engine.say("Welcome to GitHub Universe 2022!")
    engine.runAndWait()

# Call function speak()
speak()





