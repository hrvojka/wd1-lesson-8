mood = input("Enter your mood: ")

if mood == "happy":
    message = "It is great to see you happy!"
elif mood == "nervous":
    message = "Take a deep breath 3 times."
elif mood == "sad":
    message = "Smile, happiness is overrated :)"
elif mood == "excited":
    message = "It is great to see you excited!"
elif mood == "relaxed":
    message = "It is great to see you relaxed!"
else:
    message = "I don't recognize this mood."

print(message)