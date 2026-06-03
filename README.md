# 🖼️ AI Image Caption Generator

An intelligent web app built with **Streamlit** that generates multiple types of captions for uploaded images using Google's Gemini AI.

---

## ✨ Features

* 📘 **Formal Caption** – Professional, descriptive tone
* 💬 **Casual Caption** – Friendly and conversational
* 📈 **SEO Caption** – Optimized with relevant keywords
* ♿ **Alt Text** – Accessibility-focused description (<125 chars)

---

## 🚀 Demo

Upload any image and instantly get AI-generated captions in multiple styles.

### 📸 App Preview

<p align="center">
  <img src="assets/demo.png" width="700"/>
</p>

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **AI Model:** Google Gemini API
* **Image Processing:** Pillow (PIL)
* **Language:** Python

---

## 📂 Project Structure

```
ai-caption-generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── demo.png
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/Pawan-145/ai-caption-generator.git
cd ai-caption-generator
```

---

### 2. Create Virtual Environment (Optional)

```
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Locally

To run locally, you can still use environment variables:

```
export GEMINI_API_KEY=your_api_key_here   # Mac/Linux
set GEMINI_API_KEY=your_api_key_here      # Windows
```

Then run:

```
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

This app uses **Streamlit Secrets** for secure API key management.

### Steps:

1. Deploy your app on Streamlit Cloud
2. Go to **App Settings → Secrets**
3. Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

---

## 🔑 Environment Variables

| Variable       | Description                |
| -------------- | -------------------------- |
| GEMINI_API_KEY | Your Google Gemini API key |

---

## 🧠 How It Works

1. User uploads an image
2. Image is processed using PIL
3. Prompt is sent to Gemini API
4. AI generates multiple caption styles
5. Results are displayed in the UI

---

## 🎨 UI Features

* Image preview before processing
* Loading spinner during generation
* Clean and minimal interface

---

## 🔒 Security Best Practices

* API keys are stored securely using **Streamlit Secrets**
* No secrets are exposed in the codebase
* `.env` is not required for deployment

---

## 📌 Future Improvements

* 🌍 Multi-language captions
* 🎯 Custom tone selection
* 💾 Download captions
* 📱 Mobile responsiveness

---


## 📄 License

MIT License

---

## 🙌 Author

Built by *Pawan Kumar Ray*
