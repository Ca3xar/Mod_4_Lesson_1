def mood_responses(mood):
    mood = mood.lower()
    if mood == "happy":
        return "Yay! Keep it up."
    elif mood == "sad":
        return "I'm sorry to hear that. Be kind to yourself today."
    elif mood == "excited":
        return "That's great!"
    elif mood == "angry":
        return "Take a deep breath."
    else:
        return "I'm not sure what that means."