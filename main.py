import mood_responses

def main():
    mood = input("How are you feeling today? ").strip()
    print(mood_responses.mood_responses(mood))



if __name__ == "__main__":
    main()