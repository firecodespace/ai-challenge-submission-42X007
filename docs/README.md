# PrismBot: AI-Powered On-Device Chatbot for Samsung EnnovateX 2025

![PrismBot Demo](docs/chat-demo.gif)

---

## 🚀 Project Overview

PrismBot is an **Active AI Powered Android Monitoring Overlay System** designed for **privacy, personalization, and efficiency**. Unlike cloud-dependent bots, it runs the **LLAMA language model directly on-device**, ensuring all conversations and user data remain private.

At its core, PrismBot uses a **lightweight base model optimized for mobile devices** together with a modular **adapter system** that allows instant switching between specialized roles such as study help, coding assistant, travel planner, or wellness coach — all without retraining.

The app also features **smart fine-tuning** which updates active adapters automatically during idle or charging states, making the chatbot contextually aware and personalized over time.

---

## 🌟 What Makes PrismBot Special?

- 🧩 **Adapters for flexibility:** instant domain-specific role switching  
- ⚡ **Smart fine-tuning:** automatic background improvement  
- 📱 **UI Overlay Mode:** chatbot floating above apps for instant access  
- 🔒 **Strict on-device privacy:** no user data leaves device  
- 🎨 **Modern, minimal mobile-first UI:** optimized for usability and aesthetics  

---

## 🏗️ Technical Architecture

![Architecture Diagram](docs/architecture.png)

**Key Layers & Components:**

- **User Interface Layer:** Adaptive chat UI with overlay for seamless usage anywhere  
- **Service & Orchestration Layer:** Android foreground services for persistent operation  
- **Model Interaction Layer:** Interfaces with optimized LLAMA backends via JNI or container runtimes  
- **Fine-Tuning Worker:** Background jobs scheduled during idle/charging for efficient updates  
- **Data Privacy Layer:** On-device data sandboxing, encryption, and persona isolation  

---

## 🛠️ Technical Stack

| Component               | Technology                                | Link                                       |
|------------------------|------------------------------------------|--------------------------------------------|
| Frontend Web Application | React, Next.js, TypeScript, Tailwind CSS | [Next.js](https://nextjs.org/)              |
| Backend Service          | Python, FastAPI                          | [FastAPI](https://fastapi.tiangolo.com/)   |
| LLAMA Model Runner       | llama.cpp, Ollama Backend APIs           | [Ollama](https://github.com/ollama/ollama) |
| Fine-Tuning Framework    | LoRA, QLoRA, Unsloth                      | [Unsloth](https://github.com/unslothai/unsloth) |
| Overlay & Accessibility  | Android Accessibility Service, Web Workers | [Android Docs](https://developer.android.com/guide/topics/ui/accessibility) |

---

## ⚙️ Installation & Setup

### Prerequisites

- Android device with 4GB+ RAM, running Android 8.0 or higher  
- At least 4GB free disk space for models & adapters  

### Steps

1. Open the PrismBot WebApp ([Demo here](https://samsung-prism-frontend.vercel.app/chatbot)) and grant overlay and accessibility permissions.  
2. Run the backend locally: uvicorn main:app --host 127.0.0.1 --port 8000
3. Start Ngrok tunnel: ngrok http 8000
4. Set `NEXT_PUBLIC_MOBILE_API_BASE` environment variable in Vercel to Ngrok URL and deploy frontend.  
5. Download base model and adapters in-app.  
6. Complete setup wizard for preferences and enjoy.

---

## 📖 User Guide

- Launch the app and enjoy a sleek modern chat interface.  
- Type or voice your questions and get instant AI responses.  
- Enable **Overlay Mode** to float the chatbot anywhere on your device.  
- Switch between specialized roles via adapter system without delays.  
- Benefit from automatic, device-friendly background fine-tuning — no effort needed.

---

## ✨ Features & Demo

- True on-device AI processing — no cloud dependency.  
- Modular adapters for rapid role customization.  
- Smart fine-tuning triggered by idle or charging states.  
- Animated “Responding…” skeleton loader ensures smooth interaction feedback.  
- Swipe-enabled navigation and clean UX design focused on usability.  
- Rigorous privacy and security with fully sandboxed data and model components.

![Skeleton Loading Demo](docs/skeleton-demo.gif)

---

## 📽️ Demo Video

[![Watch Demo](docs/demo-thumbnail.png)](https://youtu.be/your-demo-video-link)

---

## ⚠️ Ethical Considerations & Scalability

- Privacy-first design: all user data remains on device.  
- Fine-tuning respects battery and thermal constraints.  
- Adapter sandboxing prevents data leakage between contexts.  
- Easily scalable to other mobile devices or cloud backend deployments.

---

## 📂 Documentation

Find detailed docs in the `/docs` folder:

- Architecture overview, technical design docs  
- Installation instructions  
- User guide with screenshots and GIFs  
- Features breakdown and technical stack  

---

## 📜 Attribution

This project leverages the following OSS:

- [Next.js](https://nextjs.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [llama.cpp](https://github.com/ollama/ollama)  
- [LoRA/QLoRA/Unsloth](https://github.com/unslothai/unsloth)  
- [Ngrok](https://ngrok.com/)  
- [Tailwind CSS](https://tailwindcss.com/)  

---

Made with 💡 and ⚙️ by **Your Team Name**

---

Feel free to ask if you want me to generate your `/docs/*.md` files or help prepping visuals and GIFs for this too!
