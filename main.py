import google.generativeai as genai
from dotenv import load_dotenv
import os

# ------------------ Load environment variables ------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("🚨 GEMINI_API_KEY not found in .env file!")

# ------------------ Configure Gemini ------------------
genai.configure(api_key=api_key)

# ------------------ Helper function ------------------
def load_instruction(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# ------------------ Load dynamic instructions ------------------
weather_instruction = load_instruction("instructions/weather.txt")
flight_instruction = load_instruction("instructions/flight.txt")
hotel_instruction = load_instruction("instructions/hotel.txt")

# ------------------ Create agents ------------------
weather_agent = genai.GenerativeModel("gemini-2.5-flash", system_instruction=weather_instruction)
flight_agent = genai.GenerativeModel("gemini-2.5-flash", system_instruction=flight_instruction)
hotel_agent = genai.GenerativeModel("gemini-2.5-flash", system_instruction=hotel_instruction)

agents = {
    "weather": weather_agent,
    "flight": flight_agent,
    "hotel": hotel_agent
}

print("✅ Gemini Agents initialized successfully!")


# ------------------ Query Routing & Fallback ------------------
def handle_query(query):
    """Send query to the relevant Gemini agent or fallback to generic answer."""
    q = query.lower()

    if any(word in q for word in ["weather", "temperature", "rain", "forecast"]):
        response = agents["weather"].generate_content(query)
        return response.text

    elif any(word in q for word in ["flight", "ticket", "airport", "plane"]):
        response = agents["flight"].generate_content(query)
        return response.text

    elif any(word in q for word in ["hotel", "room", "stay", "booking"]):
        response = agents["hotel"].generate_content(query)
        return response.text

    else:
        fallback_agent = genai.GenerativeModel("gemini-2.5-flash")
        response = fallback_agent.generate_content(
            "I'm not sure which topic that fits into. Could you clarify if it's about weather, flights, or hotels?"
        )
        return response.text


# ------------------ Interactive Loop ------------------
if __name__ == "__main__":
    print("\n🌟 Gemini Multi-Agent System ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        output = handle_query(user_input)
        print(f"🤖 {output}\n")
