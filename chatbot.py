from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

# Define a function to correct spelling
def correct_spelling(input_text):
    words = input_text.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = ' '.join(corrected_words)
    return corrected_text

# Define a function to chat with the spelling correction chatbot
def chat_with_bot():
    print("SpellingCorrectionBot: Hello! I can correct your spelling. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("SpellingCorrectionBot: Goodbye!")
            break
        corrected_input = correct_spelling(user_input)
        print("SpellingCorrectionBot:", corrected_input)

if __name__ == "__main__":
    chat_with_bot()
