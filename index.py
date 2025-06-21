# 1. Define the chatbot's personality
bot_name = "CryptoBuddy"
bot_tone = "friendly"
bot_intro = (
    "Hey there! 🤖 I'm CryptoBuddy, your friendly AI sidekick for all things crypto. "
    "Let’s find you a green and growing coin! 🌱🚀"
)
crypto_data = {
    "Bitcoin": {
        "price_trend": "up",  # options: up, down, stable
        "energy_efficiency": "low",
        "project_viability": "high"
    },
    "Ethereum": {
        "price_trend": "up",
        "energy_efficiency": "medium",
        "project_viability": "high"
    },
    "Dogecoin": {
        "price_trend": "down",
        "energy_efficiency": "high",
        "project_viability": "low"
    },
    "Cardano": {
        "price_trend": "stable",
        "energy_efficiency": "high",
        "project_viability": "medium"
    }
}
def give_advice(coin):
    coin = coin.capitalize()
    
    if coin not in crypto_data:
        return f"Sorry, I don't have data on '{coin}'. Try another coin."

    data = crypto_data[coin]
    trend = data["price_trend"]
    energy = data["energy_efficiency"]
    viability = data["project_viability"]
    
    # Rule-based logic
    if trend == "up" and viability == "high":
        return f"{coin} looks profitable and viable. 👍 Advice: **Buy**"
    elif trend == "stable" and energy == "high":
        return f"{coin} is energy efficient and stable. 💡 Advice: **Hold**"
    elif trend == "down" or viability == "low":
        return f"{coin} might not be a good choice right now. 🚫 Advice: **Avoid**"
    else:
        return f"{coin} is a mixed bag. ⚖️ Advice: **Research More Before Investing**"
def start_chat():
    print("👋 Welcome to CryptoBot - Your AI-Powered Financial Sidekick! 🌟")
    print("Type the name of a cryptocurrency (e.g., Bitcoin, Ethereum) or 'quit' to exit.")
    
    while True:
        user_input = input("\n🔎 Which cryptocurrency are you curious about? ")
        
        if user_input.lower() == "quit":
            print("👋 Goodbye! Invest wisely!")
            break
            
        advice = give_advice(user_input)
        print(f"\n🤖 CryptoBot: {advice}")
