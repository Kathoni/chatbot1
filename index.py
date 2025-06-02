
bot_name = "CryptoBuddy"
print(f"\U0001F44B Hey, I’m {bot_name}, your AI crypto sidekick!")
print("\U0001F4B0 Let's find the best coin based on trends and sustainability! \U0001F331")

# \U0001F44B is a Unicode escape sequence in Python that represents the waving hand emoji (👋).

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}
while True:
    try:
        user_query = input("\nAsk me something like:\n- Which crypto is trending up?\n- What’s the most sustainable coin?\n- Which should I buy for long-term?\n(Type 'exit' to quit)\n\n👉 Your question: ").lower()

        if user_query == "exit":
            print("👋 Bye! Stay smart and safe in your crypto journey!")
            break

        if "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"\U0001F331 {recommend} is the greenest pick with a sustainability score of {crypto_db[recommend]['sustainability_score']}/10!")

        elif "trending" in user_query or "rising" in user_query:
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            print("\U0001F4C8 These cryptos are trending up: " + ", ".join(trending))

        elif "long-term" in user_query or "buy" in user_query:
            found = False
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] == "high":
                    print(f"\U0001F680 {coin} is a strong long-term choice with rising trends and high market cap.")
                    found = True
                    break
            if not found:
                print("\U0001F914 Hmm… none match both conditions perfectly right now.")

        else:
            print("❓ I'm not sure how to answer that. Try asking about trends or sustainability.")

    except OSError:
        print("⚠️ Oops! Input isn’t supported in this environment. Please run this in a local IDE like VSCode or Jupyter.")
        break

print("\n⚠️ Disclaimer: Crypto is risky—always DYOR (Do Your Own Research)! \U0001F9E0\U0001F4C9")
