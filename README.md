# 🔮 Tarot Reading Using Generative AI

## 📌 About the Project
This is an interactive **Tarot Reading Web App** built with **Streamlit** and **Generative AI**. It allows users to draw tarot cards, view their meanings, and get **AI-powered interpretations** using Hugging Face's LLM models.

---
## 🎮 Live Demo  
[🔮 Try the Tarot App Here! 🚀](https://tarotreadingusinggenai-2e2ancsujokjrwq3j9spc2.streamlit.app/)  
*(Click the link to get your AI-powered tarot reading! 🔮✨)*

---

## 🚀 Features
✅ **Draw 3 Random Tarot Cards** (Past, Present, Future)
✅ **Displays Tarot Card Images**
✅ **AI-Generated Tarot Readings** using Falcon-7B
✅ **User Input for Personal Questions**
✅ **Fully Responsive & Interactive UI**

---
## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/VIKRAM-009/tarot_reading_Using_GEN_AI.git
cd tarot_reading_Using_GEN_AI
```

### 2️⃣ Create & Activate a Virtual Environment (Optional)
```bash
python -m venv env  # Create virtual environment
source env/bin/activate  # Activate (Mac/Linux)
env\Scripts\activate  # Activate (Windows)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run tarot_app.py
```

---

## 🔑 Setting Up API Keys
### **Using Hugging Face API**
1. Go to [Hugging Face Tokens](https://huggingface.co/settings/tokens) & create a new API key.
2. Store the key securely in **Streamlit Cloud Secrets**:
   - Go to **Streamlit Cloud** → **Settings** → **Secrets**
   - Add:
     ```
     HUGGINGFACE_API_KEY = hf_xxxxxxxxxxxxxxxxxxxxxx
     ```

---

## 🌐 Deployment on Streamlit Cloud
1. **Push Your Code to GitHub**
   ```bash
   git add .
   git commit -m "Deploying tarot app"
   git push origin main
   ```
2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
3. **Deploy the App** by selecting `tarot_app.py` as the main file
4. **Add API Key in Secrets** (as shown above)

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Falcon-7B (via Hugging Face API)
- **Libraries**: Requests, Pillow, JSON

---

## 📜 License
This project is **open-source** under the **MIT License**.

---

## 📬 Contact & Feedback
💡 **Have suggestions? Found a bug?**
- Open an issue on **GitHub**
🔮✨ **Enjoy Your Tarot Reading!** ✨🔮

