import streamlit as st
from huggingface_hub import InferenceClient
import requests

# ==============================================================================
# 📄 BİTA AI - RESMİ LİSANS VE TELİF HAKKI BİLDİRİMİ (PROPRIETARY LICENSE)
# ==============================================================================
# Copyright (c) 2026 sahinlibilaltaha-tech. All rights reserved.
# Bu yazılımın ve "BİTA AI" markasının tüm hakları saklıdır. İzinsiz taklit edilemez.
# ==============================================================================

# Üst Düzey Kurumsal Sayfa Ayarları
st.set_page_config(
    page_title="BITA AI | Enterprise Intelligent System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🔒 GÜVENLİK DUVARI AŞMA AYARI (Şifreyi gizli sistem değişkeninden güvenle okuyoruz)
import os
HF_TOKEN = os.getenv("HF_TOKEN", "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")
MODEL_NAME = "Qwen/Qwen2.5-Coder-7B-Instruct"

# 👑 GOOGLE'DAN ALDIĞIN RESMİ ANAHTARLAR
GOOGLE_CLIENT_ID = "://googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
REDIRECT_URI = "https://onrender.com" 

# 👑 KİLİTLİ ÖZELLİKLERİ SADECE SENİN EKRANINDA AÇACAK OLAN PATRON MAİLİ
ADMIN_EMAIL = "sahinlibilaltaha@gmail.com"

@st.cache_resource
def get_client(token):
    return InferenceClient(model=MODEL_NAME, token=token)

# --- SİSTEM HAFIZASI VE OTURUM YÖNETİMİ ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "language" not in st.session_state:
    st.session_state.language = "TR"
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- PROFESYONEL MULTI-LANGUAGE DİL PAKETLERİ ---
LANG_DATA = {
    "TR": {
        "welcome": "BITA AI Sistem Çekirdeği", "sub": "Gelişmiş kurumsal yapay zeka istasyonu.",
        "input_placeholder": "Sisteme talimat gönderin...", "new_chat": "Yeni Oturum Başlat",
        "logout": "Güvenli Çıkış", "status": "Sistem: Çevrimiçi", "license": "Lisans: Ticari Mülk Koruma Altında",
        "login_title": "BITA AI | Merkezi Kimlik Doğrulama", "login_sub": "Devam etmek için Google (Gmail) hesabınızla güvenli giriş yapın.",
        "login_btn": "Gmail Hesabı ile Giriş Yap", "thinking": "BITA AI veriyi işliyor...",
        "admin_panel": "🔒 YÖNETİCİ ÖZEL SİSTEM PANELİ", "admin_feature_1": "🚀 Gelişmiş Kod Analitiği",
        "admin_feature_2": "🧠 Derin Veri Madenciliği Modu", "admin_feature_3": "📁 Sunucu Sistem Logları (Kilitli)"
    },
    "EN": {
        "welcome": "BITA AI Core System", "sub": "Advanced enterprise AI station.",
        "input_placeholder": "Send instructions to system...", "new_chat": "Start New Session",
        "logout": "Secure Sign Out", "status": "System: Online", "license": "License: Commercial Property Protected",
        "login_title": "BITA AI | Central Authentication", "login_sub": "Sign in with your Google (Gmail) account to proceed.",
        "login_btn": "Sign In with Gmail", "thinking": "BITA AI processing data...",
        "admin_panel": "🔒 ADMIN EXCLUSIVE PANEL", "admin_feature_1": "🚀 Advanced Code Analytics",
        "admin_feature_2": "🧠 Deep Data Mining Mode", "admin_feature_3": "📁 Server System Logs (Locked)"
    }
}

L = LANG_DATA[st.session_state.language]

# --- GOOGLE OAUTH GİRİŞ SÜRECİ ---
query_params = st.query_params
if "code" in query_params and not st.session_state.authenticated:
    try:
        auth_code = query_params["code"]
        token_url = "https://googleapis.com"
        token_data = {
            "code": auth_code, "client_id": GOOGLE_CLIENT_ID, "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI, "grant_type": "authorization_code"
        }
        r_token = requests.post(token_url, data=token_data).json()
        
        if "access_token" in r_token:
            user_info = requests.get("https://googleapis.com", headers={"Authorization": f"Bearer {r_token['access_token']}"}).json()
            st.session_state.user_email = user_info.get("email")
            st.session_state.authenticated = True
            if st.session_state.user_email == ADMIN_EMAIL:
                st.session_state.is_admin = True
            st.rerun()
    except:
        pass

# --- 1. AŞAMA: PROFESYONEL GİRİŞ EKRANI (LOGIN) ---
if not st.session_state.authenticated:
    st.markdown(f"<h1 style='text-align: center; margin-top: 8%; color: #FFFFFF; font-weight: 400; letter-spacing: 1px;'>{L['login_title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666666;'>{L['login_sub']}</p>", unsafe_allow_html=True)
    
    auth_url = f"https://google.com{GOOGLE_CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=https://googleapis.com"
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown(f"<a href='{auth_url}' target='_self' style='text-decoration: none;'><button style='width: 100%; padding: 14px; background-color: #EA4335; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 16px; box-shadow: 0px 4px 12px rgba(0,0,0,0.4); transition: 0.3s;'>{L['login_btn']}</button></a>", unsafe_allow_html=True)
    st.stop()

# --- 2. AŞAMA: KURUMSAL SADE YAN MENÜ ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FFFFFF; letter-spacing: 2px; margin-bottom: 2px;'>BITA AI</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666666; font-size: 11px;'>USER: {st.session_state.user_email}</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Profesyonel Dil Seçimi
    lang_choice = st.selectbox("🌐 System Language / Dil", ["TR", "EN"], index=0 if st.session_state.language == "TR" else 1)
    if lang_choice != st.session_state.language:
        st.session_state.language = lang_choice
        st.rerun()
        
    st.write("---")
    
    # ==============================================================================
    # 👑 KİLİTLİ YASAKLI ÖZELLİKLER (Sadece senin Gmail adresinle girilirse açılır)
    # ==============================================================================
    if st.session_state.is_admin:
        st.markdown(f"<p style='color: #FF4B4B; font-weight: bold; margin-bottom: 2px; font-size: 13px;'>{L['admin_panel']}</p>", unsafe_allow_html=True)
        st.checkbox(L['admin_feature_1'], value=True)
        st.checkbox(L['admin_feature_2'], value=True)
        if st.button(L['admin_feature_3'], use_container_width=True):
            st.toast("Ana sunucu kilitli sistem logları başarıyla yüklendi.", icon="⚙️")
        st.write("---")
    # ==============================================================================
    
    if st.button(f"📊 {L['new_chat']}", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
        
    if st.button(f"🚪 {L['logout']}", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.is_admin = False
        st.session_state.user_email = None
        st.session_state.messages = []
        st.rerun()
        
    st.write("---")
    st.caption(f"🟢 {L['status']}")
    st.caption(f"🔒 {L['license']}")

# --- 3. AŞAMA: SOHBET ARANÜZÜ ---
if len(st.session_state.messages) == 0:
    st.markdown(f"<h1 style='text-align: center; margin-top: 10%; color: #FFFFFF; font-weight: 300; letter-spacing: 1px;'>{L['welcome']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #555555;'>{L['sub']}</p>", unsafe_allow_html=True)

# ChatGPT Tarzı Yalın Mesaj Akışı
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Giriş Alanı
if prompt := st.chat_input(L["input_placeholder"]):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown(f"*{L['thinking']}*")
        
        try:
            client = get_client(HF_TOKEN)
            system_prompt = f"You are BITA AI, an elite enterprise artificial intelligence system developed by sahinlibilaltaha-tech. User context: {st.session_state.user_email}. Is Founder: {st.session_state.is_admin}. Respond sharply and professionally in Turkish."
            
            payload_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages
            response = client.chat_completion(messages=payload_messages, max_tokens=1500, temperature=0.2)
            
            bot_cevabi = response.choices.message.content
            message_placeholder.markdown(bot_cevabi)
            st.session_state.messages.append({"role": "assistant", "content": bot_cevabi})
        except Exception as e:
            message_placeholder.markdown("System core connection timeout. Please try again.")
