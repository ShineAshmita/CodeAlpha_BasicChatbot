# ============================================================
#   CodeAlpha Internship — Task 4: Basic Chatbot
#   Author  : (Your Name)
#   GitHub  : CodeAlpha_BasicChatbot
# ============================================================

import random
import time

# ──────────────────────────────────────────────────────────
#  Response rules — keyword : list of possible replies
# ──────────────────────────────────────────────────────────

RESPONSES = {
    # Greetings
    "hello":         ["Hello! 👋 How can I help you today?",
                      "Hi there! Great to see you!",
                      "Hey! What can I do for you?"],
    "hi":            ["Hi! 😊 How are you doing?",
                      "Hello! Nice to meet you!"],
    "hey":           ["Hey! What's up?",
                      "Hey there! How can I assist?"],
    "good morning":  ["Good morning! ☀️ Hope you have a wonderful day!",
                      "Morning! Ready to take on the day? 🌅"],
    "good evening":  ["Good evening! 🌙 How was your day?",
                      "Evening! Hope your day went well!"],
    "good afternoon":["Good afternoon! 🌤️ Hope you're having a great day!"],

    # How are you
    "how are you":   ["I'm doing great, thanks for asking! 😊 How about you?",
                      "I'm just a bot, but I feel fantastic! 🤖",
                      "All systems running smoothly! How are you?"],
    "how r you":     ["Doing awesome! Thanks for checking in! 😄"],
    "what's up":     ["Not much, just here to chat! What about you?",
                      "All good on my end! 😎 What's on your mind?"],
    "wassup":        ["Hey! Just chillin' and ready to help 😄"],

    # Name / identity
    "what is your name": ["My name is CodeBot 🤖 — your friendly CodeAlpha assistant!",
                           "I'm CodeBot, built with ❤️ during a CodeAlpha internship!"],
    "who are you":        ["I'm CodeBot, a simple rule-based chatbot built in Python! 🐍",
                           "I'm your helpful assistant — CodeBot!"],
    "who made you":       ["I was created as part of the CodeAlpha Python internship program! 👨‍💻",
                           "A Python intern at CodeAlpha built me!"],
    "are you a bot":      ["Yes! I'm a bot — but I promise I'm a friendly one 😄",
                           "100% bot, 100% helpful! 🤖"],
    "are you human":      ["Nope! I'm a Python-powered chatbot 🐍",
                           "I wish! But I'm just a bot. A very cool bot though 😎"],

    # Mood / feelings
    "i am fine":     ["That's great to hear! 😊",
                      "Glad to know you're doing well!"],
    "i am good":     ["Wonderful! 🙌 What can I help you with?"],
    "i am sad":      ["I'm sorry to hear that 😢 Hope things get better soon!",
                      "Sending virtual hugs 🤗 Want to talk about it?"],
    "i am happy":    ["That's awesome! 🎉 Happiness is contagious!",
                      "Love to hear that! Keep smiling 😁"],
    "i am tired":    ["Take some rest! 😴 You deserve it.",
                      "Rest up! Your wellbeing matters 💙"],
    "i am bored":    ["Let's chat then! Ask me anything 😄",
                      "I can tell you a joke! Type 'joke' 😂"],

    # Small talk
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything! 😄",
                       "What do you call a fish without eyes? A fsh! 🐟",
                       "I told my computer I needed a break... now it won't stop sending me Kit-Kat ads 🍫",
                       "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"],
    "joke":           ["Why did the programmer quit his job? Because he didn't get arrays! 😂",
                       "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?' 😄",
                       "Why do Java developers wear glasses? Because they don't C# ! 🤓"],
    "fun fact":       ["🐍 Python was named after Monty Python, not the snake!",
                       "🌐 The first website ever is still live at info.cern.ch!",
                       "💾 The first computer bug was an actual bug — a moth found in a relay in 1947!"],

    # Python / coding
    "python":         ["Python is awesome! 🐍 Great choice for beginners and pros alike.",
                       "I was built in Python! It's clean, readable, and powerful 💪"],
    "coding":         ["Coding is a superpower! 🦸 Keep practicing and you'll go far.",
                       "Every expert was once a beginner. Keep coding! 💻"],
    "programming":    ["Programming is problem-solving made fun! 🧩",
                       "Love programming! It lets you build anything you can imagine 🚀"],

    # CodeAlpha
    "codealpha":      ["CodeAlpha is a great platform to grow your skills! 🚀",
                       "Proud to be part of the CodeAlpha internship program! 🎓"],
    "internship":     ["Internships are the best way to gain real-world experience! 📚",
                       "The CodeAlpha internship teaches you practical Python skills 🐍"],

    # Time / date
    "what time is it": ["I don't have a real-time clock, but Python's datetime module can help! ⏰"],
    "what is today":   ["I don't have live date access, but Python's datetime.date.today() does! 📅"],

    # Help
    "help":           ["I can chat with you! Try: 'hello', 'joke', 'fun fact', 'python', 'how are you', or 'bye' 😊"],
    "what can you do": ["I can: chat 💬, tell jokes 😂, share fun facts 🤓, talk about Python 🐍, and more! Just talk to me!"],

    # Bye / exit
    "bye":            ["Goodbye! 👋 Have a wonderful day!",
                       "See you later! Take care 😊",
                       "Bye! It was great chatting with you! 🌟"],
    "goodbye":        ["Goodbye! Come back anytime 😊",
                       "Farewell! Keep coding! 🐍"],
    "see you":        ["See you soon! 👋",
                       "Take care! Bye bye 😄"],
    "exit":           ["Closing chat... Goodbye! 👋"],
    "quit":           ["Quitting... Hope to chat again soon! 😊"],

    # Thanks
    "thank you":      ["You're welcome! 😊 Anytime!",
                       "Happy to help! 🙌"],
    "thanks":         ["No problem! 😄",
                       "Glad I could help! 🤗"],

    # Compliments
    "you are great":  ["Aw, thank you! 😊 You're great too!"],
    "you are smart":  ["Thanks! I'm only as smart as my code 🤓"],
    "good bot":       ["Thank you! I try my best 🤖❤️"],
}

# Default replies when no keyword matches
DEFAULT_REPLIES = [
    "Hmm, I'm not sure about that. Could you rephrase? 🤔",
    "Interesting! Tell me more? 😊",
    "I'm still learning! Try asking me something else 🤖",
    "I didn't quite catch that. Type 'help' to see what I can do!",
    "That's a tough one for me! Try 'joke' or 'fun fact' instead 😄",
]

EXIT_KEYWORDS = {"bye", "goodbye", "exit", "quit", "see you"}


# ──────────────────────────────────────────────────────────
#  Core chatbot logic
# ──────────────────────────────────────────────────────────

def get_response(user_input: str) -> str:
    """Return the best matching response for the given input."""
    text = user_input.lower().strip()

    # Exact / substring match — longest key wins to avoid partial over-match
    matched_key = None
    matched_len = 0
    for key in RESPONSES:
        if key in text and len(key) > matched_len:
            matched_key = key
            matched_len = len(key)

    if matched_key:
        return random.choice(RESPONSES[matched_key])

    return random.choice(DEFAULT_REPLIES)


def is_exit(user_input: str) -> bool:
    """Return True if the user wants to leave."""
    text = user_input.lower().strip()
    return any(kw in text for kw in EXIT_KEYWORDS)


def typing_effect(text: str, delay: float = 0.03) -> None:
    """Print text with a typewriter effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ──────────────────────────────────────────────────────────
#  Main chat loop
# ──────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 56)
    print("   🤖  CodeAlpha — Python Chatbot  🤖")
    print("=" * 56)
    typing_effect("  CodeBot: Hello! I'm CodeBot 🤖 Type 'help' for tips.\n"
                  "           Type 'bye' whenever you want to leave!\n")

    while True:
        try:
            user_input = input("  You     : ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            user_input = "bye"

        if not user_input:
            print("  CodeBot : Please say something! I'm listening 😊")
            continue

        # Simulate thinking
        time.sleep(0.4)
        response = get_response(user_input)
        typing_effect(f"  CodeBot : {response}")

        if is_exit(user_input):
            break

    print("\n" + "=" * 56 + "\n")


if __name__ == "__main__":
    main()
