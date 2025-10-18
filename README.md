Perfect jani 💪 — neeche tera project ke liye **GitHub description + full professional README.md** ready hai (Gemini-based multi-agent system ke liye).

---

## 🏷️ **GitHub Repository Name:**

`gemini-multi-agent-system`

---

## 💬 **GitHub Short Description:**

> A Python-based multi-agent system powered by Google Gemini that uses dynamic instructions to handle specialized tasks like weather, flight, and hotel assistance — all configurable through external instruction files.

---

## 📘 **README.md**

```markdown
# 🌐 Gemini Multi-Agent System

A **Python-based multi-agent system** powered by **Google Gemini**, built to demonstrate how dynamic instructions can be used to manage multiple specialized AI agents — such as weather, flight, or hotel assistants.

This project is designed to be modular, clean, and easily extensible — just drop a new instruction file and spin up a new agent.

---

## 🚀 Features

✅ Uses **Gemini 1.5 Flash** (Google Generative AI)  
✅ Loads **dynamic instructions** from text files  
✅ Supports multiple specialized agents  
✅ Environment-safe key management using `.env`  
✅ Modular structure (easy to extend or integrate)

---

## 🧠 Concept

Instead of hardcoding agent behavior, each agent’s role and knowledge are defined in separate instruction files stored under the `instructions/` folder.

Example:
```

instructions/
│
├── weather.txt
├── flight.txt
└── hotel.txt

```

Each file contains simple text describing how that agent should behave.  
When the system runs, it reads the instruction file and dynamically configures the agent.

---

## 🧩 Folder Structure

```

dy_ins/
│
├── main.py
├── .env
└── instructions/
└── weather.txt

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/gemini-multi-agent-system.git
cd gemini-multi-agent-system
````

### 2️⃣ Create a Virtual Environment

```bash
uv venv
```

or

```bash
python -m venv .venv
```

### 3️⃣ Install Dependencies

```bash
uv pip install google-generativeai python-dotenv
```

or (if using pip)

```bash
pip install google-generativeai python-dotenv
```

### 4️⃣ Add Your API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 💡 Example Instruction File (`instructions/weather.txt`)

```text
You are a helpful weather assistant.
Answer questions about temperature, forecasts, and general climate information.
Do not use external web searches — respond based on your general knowledge.
```

---

## 🧰 Run the Application

```bash
python main.py
```

Example run:

```
🌤 Weather Assistant Ready!

You: What's the temperature in Dubai?
AI: Dubai is typically warm and dry, averaging around 35°C during the day.
```

---

## 🧱 Future Expansion

You can easily add more agents:

* ✈️ `flight.txt` → For travel or flight booking assistance
* 🏨 `hotel.txt` → For hotel search and booking recommendations
* 📰 `news.txt` → For summarizing or discussing recent topics

Each new file = new agent behavior. 🔥

---

## 🧑‍💻 Author

**Manas Shahid**
Developer • Digital Marketing Expert • AI Systems Enthusiast
🌍 [LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/)

---

## 📜 License

This project is open-source under the **MIT License**.

---

### 💬 Summary

> Build once, expand infinitely — this Gemini multi-agent framework lets you define new AI roles just by editing plain text files.

```

---

Would you like me to include an **example for multiple agents** in the same README (like `weather_agent`, `flight_agent`, etc.) so the repo looks more advanced and scalable?
```
