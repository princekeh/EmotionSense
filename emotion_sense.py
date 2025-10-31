# EmotionSense - Simple Emotion Detection System
# Author: Prince S. Agoabuike
# Description: An amateur-level Python project that detects basic emotions in text using keyword matching.

# Define a simple emotion dictionary
emotions = {
    "happy": ["joy", "glad", "excited", "great", "wonderful", "cheerful"],
    "sad": ["unhappy", "down", "depressed", "cry", "upset", "hurt"],
    "angry": ["mad", "furious", "irritated", "annoyed", "rage", "hate"],
    "fear": ["scared", "afraid", "terrified", "nervous", "worried", "anxious"],
    "surprised": ["wow", "amazed", "shocked", "astonished", "unexpected"]
}

def detect_emotion(text):
    text = text.lower()
    scores = {emotion: 0 for emotion in emotions}

    for emotion, words in emotions.items():
        for word in words:
            if word in text:
                scores[emotion] += 1

    detected = max(scores, key=scores.get)
    return detected if scores[detected] > 0 else "neutral"

# Run the program
if __name__ == "__main__":
    print("Welcome to EmotionSense!")
    while True:
        user_input = input("Enter a sentence (or type 'quit' to exit): ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        emotion = detect_emotion(user_input)
        print(f"Detected emotion: {emotion}\n")
