import os
from dotenv import load_dotenv
from google import genai
# TODO: Import SYSTEM_PROMPT from utils.config

# TODO: Load environment variables

class ChatAssistant:
    
    def __init__(self, api_key=None):
        # TODO: Initialize API key from parameter or env var GEMINI_API_KEY
        # TODO: Raise ValueError if no key found
        # TODO: Initialize Gemini client
        # TODO: Initialize conversation history storage
        pass
    
    def add_to_history(self, role, content):
        # TODO: Add message to conversation history
        # TODO: Handle role types: "user", "assistant", "system"
        # TODO: Manage history length limits (keep last N messages)
        pass
    
    def get_conversation_context(self):
        # TODO: Format conversation history for API call
        # TODO: Include system prompt and recent conversation
        # TODO: Return formatted conversation string
        pass
    
    def chat(self, user_input):
        # TODO: Add user input to conversation history
        # TODO: Get formatted conversation context
        # TODO: Call Gemini API with full conversation context
        # TODO: Add assistant response to conversation history
        # TODO: Return response text
        pass
    
    def reset_conversation(self):
        # TODO: Clear conversation history
        # TODO: Keep system prompt but remove user/assistant messages
        pass

def answer_fitness_query(query, assistant=None):
    # TODO: Create ChatAssistant instance if not provided
    # TODO: Call assistant.chat(query)
    # TODO: Handle exceptions and return error message
    pass

def main():
    """Main function to demonstrate the fitness coach assistant."""
    print("Personal Fitness Coach - Multi-Turn Chat")
    print("Type 'quit' to exit, 'reset' to start new conversation")
    print("=" * 50)
    
    sample_conversations = [
        [
            "I'm new to working out and want to build muscle. Where should I start?",
            "I can work out 3 days a week.",
            "I can't do pull-ups yet, what alternatives do you suggest?"
        ],
        [
            "I want to lose weight but don't know what to eat.",
            "I eat out a lot and drink soda daily.",
            "I like Italian and Mexican food."
        ]
    ]
    
    # Demonstrate conversation examples
    assistant = None  # TODO: Initialize assistant
    
    for i, conversation in enumerate(sample_conversations):
        print(f"\n--- Sample Conversation {i+1} ---")
        for query in conversation:
            print(f"\nUser: {query}")
            response = answer_fitness_query(query, assistant)
            print(f"Coach: {response}")
        assistant.reset_conversation() if assistant else None

if __name__ == "__main__":
    main()
