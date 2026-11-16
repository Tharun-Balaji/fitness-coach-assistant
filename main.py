import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

from utils.config import SYSTEM_PROMPT

load_dotenv()

class ChatAssistant:
    MAX_HISTORY_MESSAGES = 20
    FRIENDLY_API_ERROR = (
        "I'm having trouble reaching the coaching service right now. "
        "Please try again in a little while."
    )

    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("GEMINI_API_KEY")
        if not isinstance(api_key, str) or not api_key.strip():
            raise ValueError(
                "A Gemini API key is required. Set GEMINI_API_KEY or pass api_key."
            )

        self.client = genai.Client(api_key=api_key.strip())
        self.conversation_history = []
    
    def add_to_history(self, role, content):
        if role not in {"user", "assistant", "system"}:
            raise ValueError("role must be 'user', 'assistant', or 'system'")
        self.conversation_history.append({"role": role, "content": str(content)})
        self.conversation_history = self.conversation_history[
            -self.MAX_HISTORY_MESSAGES:
        ]
    
    def get_conversation_context(self):
        messages = [
            f"{message['role'].capitalize()}: {message['content']}"
            for message in self.conversation_history
        ]
        context = "\n".join(messages)
        if context:
            return f"{SYSTEM_PROMPT}\n\nConversation history:\n{context}"
        return SYSTEM_PROMPT

    def chat(self, user_input):
        if not isinstance(user_input, str) or not user_input.strip():
            raise ValueError("user_input must be a non-empty string")

        self.add_to_history("user", user_input.strip())
        fullprompt = self.get_conversation_context()
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=fullprompt,
            )
        except APIError:
            return self.FRIENDLY_API_ERROR

        response_text = getattr(response, "text", None)
        if not isinstance(response_text, str) or not response_text.strip():
            response_text = (
                "I couldn't generate a response just now. Please try asking again."
            )
        else:
            response_text = response_text.strip()
        self.add_to_history("assistant", response_text)
        return response_text

    def reset_conversation(self):
        self.conversation_history.clear()

def answer_fitness_query(query, assistant=None):
    if assistant is None:
        assistant = ChatAssistant()
    return assistant.chat(query)

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
    assistant = ChatAssistant()
    
    for i, conversation in enumerate(sample_conversations):
        print(f"\n--- Sample Conversation {i+1} ---")
        for query in conversation:
            print(f"\nUser: {query}")
            response = answer_fitness_query(query, assistant)
            print(f"Coach: {response}")
        assistant.reset_conversation() if assistant else None

if __name__ == "__main__":
    main()
