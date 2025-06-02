# 👋 CryptoBuddy: Your AI Crypto Sidekick

Welcome to **CryptoBuddy**, a simple rule-based Python chatbot that helps you analyze cryptocurrency trends and sustainability!

🪙💹🌱

## 🔍 What is CryptoBuddy?

CryptoBuddy is a console-based chatbot built in Python that provides recommendations based on:

- 📈 **Price Trends**
- 🪙 **Market Capitalization**
- 🌱 **Energy Use and Sustainability Score**

It uses a small predefined database of popular cryptocurrencies—**Bitcoin**, **Ethereum**, and **Cardano**—to provide insightful responses to user queries.

---

## 🚀 Features

- Ask questions like:
  - *"Which crypto is trending up?"*
  - *"What’s the most sustainable coin?"*
  - *"Which should I buy for long-term?"*

- Get friendly, emoji-enhanced responses.
- Offers basic decision logic based on predefined data.
- Includes a disclaimer encouraging responsible crypto investing.

---

## 🧠 How It Works

The script uses a `while` loop to continuously take user input and responds based on:

| Condition                      | Response                                                                 |
|-------------------------------|--------------------------------------------------------------------------|
| Query mentions “sustainable”  | Recommends the coin with the highest sustainability score               |
| Query mentions “trending”     | Lists all coins with a "rising" price trend                             |
| Query mentions “long-term”    | Suggests coins with both "rising" trend and "high" market cap           |
| Anything else                 | Responds with an "I'm not sure" message                                 |

---

## 🖥️ How to Run

### Option 1: Locally (Recommended)

1. Make sure you have Python 3.x installed.
2. Clone or download this repository.
3. Open a terminal and run the file:

```bash
python cryptobuddy.py
