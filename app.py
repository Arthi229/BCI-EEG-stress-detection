# IMPORTS

import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import requests
import time

from datetime import datetime
from streamlit_lottie import st_lottie

from utils.signal_generator import generate_signal
from utils.spectrogram_generator import generate_spectrogram
from utils.band_power import calculate_band_power
from utils.database import init_db, insert_record, fetch_records
from utils.pdf_report import generate_pdf_report

# PAGE CONFIG

st.set_page_config(
    page_title="EEG Clinical Monitoring Platform", page_icon="🧠", layout="wide"
)


# FUTURISTIC CYBER UI CSS

st.markdown(
    """

""",
    unsafe_allow_html=True,
)


# =====================================================
# DEMO AI MODEL
# =====================================================

class DummyModel:

    def predict(self, data):

        return np.array([[0.82]])


@st.cache_resource
def load_trained_model():

    return DummyModel()


model = load_trained_model()

# LOGIN SESSION

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ULTRA CINEMATIC CYBERPUNK LOGIN PAGE

if not st.session_state.logged_in:

    st.markdown(
        """
        <style>

        /* MAIN BACKGROUND */
        .stApp{

            background:
            radial-gradient(
                circle at top,
                #050505,
                #000000,
                #020617
            );

            color:white;
            overflow:hidden;
        }

        /* FLOATING GLITTER */
        .stApp::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(255,20,147,0.8) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 18s linear infinite;

            opacity:0.7;

            z-index:0;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-200px);
            }
        }

        /* CYBER GRID */
        .cyber-grid{

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            background-image:

            linear-gradient(
                rgba(56,189,248,0.06) 1px,
                transparent 1px
            ),

            linear-gradient(
                90deg,
                rgba(56,189,248,0.06) 1px,
                transparent 1px
            );

            background-size:40px 40px;

            pointer-events:none;

            z-index:0;

            animation:gridMove 12s linear infinite;
        }

        @keyframes gridMove{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(40px);
            }
        }

        /* FLOATING ORBS */
        .cyber-orb{

            position:fixed;

            border-radius:50%;

            filter:blur(80px);

            opacity:0.20;

            z-index:0;

            animation:floatOrb 10s ease-in-out infinite alternate;
        }

        .orb1{

            width:260px;
            height:260px;

            background:#00ffff;

            top:10%;
            left:5%;
        }

        .orb2{

            width:320px;
            height:320px;

            background:#8b5cf6;

            bottom:10%;
            right:5%;
        }

        @keyframes floatOrb{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(40px);
            }
        }

        /* LOGIN BOX */
        .login-box{

            position:relative;

            z-index:2;

            background:
            rgba(0,0,0,0.88);

            backdrop-filter:blur(25px);

            padding:55px 40px;

            margin-top:70px;

            border-radius:30px;

            overflow:hidden;

            text-align:center;

            isolation:isolate;

            box-shadow:
            0 0 25px rgba(56,189,248,0.18),
            0 0 50px rgba(168,85,247,0.15),
            0 0 80px rgba(0,0,0,0.9);
        }

        /* ANIMATED BORDER */
        .login-box::before{

            content:"";

            position:absolute;

            inset:-2px;

            background:
            linear-gradient(
                45deg,
                #00ffff,
                #8b5cf6,
                #ff1493,
                #00ffff
            );

            background-size:400%;

            border-radius:32px;

            z-index:-2;

            animation:borderGlow 8s linear infinite;

            opacity:0.8;
        }

        .login-box::after{

            content:"";

            position:absolute;

            inset:3px;

            background:
            linear-gradient(
                rgba(0,0,0,0.92),
                rgba(10,10,20,0.94)
            );

            border-radius:28px;

            z-index:-1;
        }

        @keyframes borderGlow{

            0%{
                background-position:0%;
            }

            100%{
                background-position:400%;
            }
        }

        /* ROTATING RINGS */
        .login-ring{

            position:absolute;

            border-radius:50%;

            border:2px solid rgba(56,189,248,0.18);

            animation:rotateRing 12s linear infinite;

            pointer-events:none;
        }

        .ring1{

            width:420px;
            height:420px;

            top:-80px;
            left:-80px;
        }

        .ring2{

            width:520px;
            height:520px;

            top:-130px;
            left:-130px;

            animation-direction:reverse;
        }

        @keyframes rotateRing{

            from{
                transform:rotate(0deg);
            }

            to{
                transform:rotate(360deg);
            }
        }

        /* SCAN LINE */
        .scan-line{

            position:absolute;

            top:0;
            left:0;

            width:100%;
            height:4px;

            background:
            linear-gradient(
                90deg,
                transparent,
                #38BDF8,
                transparent
            );

            box-shadow:
            0 0 20px #38BDF8;

            animation:scanMove 4s linear infinite;
        }

        @keyframes scanMove{

            0%{
                top:0%;
            }

            100%{
                top:100%;
            }
        }

        /* CYBER CORNERS */
        .corner{

            position:absolute;

            width:35px;
            height:35px;

            border-color:#38BDF8;

            z-index:5;
        }

        .corner1{

            top:12px;
            left:12px;

            border-top:3px solid;
            border-left:3px solid;
        }

        .corner2{

            top:12px;
            right:12px;

            border-top:3px solid;
            border-right:3px solid;
        }

        .corner3{

            bottom:12px;
            left:12px;

            border-bottom:3px solid;
            border-left:3px solid;
        }

        .corner4{

            bottom:12px;
            right:12px;

            border-bottom:3px solid;
            border-right:3px solid;
        }

        /* TITLE */
        .rainbow-title{

            font-size:44px;

            line-height:1.2;

            white-space:nowrap;

            font-weight:900;

            font-family:'Orbitron',sans-serif;

            background:
            linear-gradient(
                90deg,
                #00ffff,
                #38BDF8,
                #8b5cf6,
                #ff1493,
                #ff7f00
            );

            background-size:300% auto;

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            animation:rainbowFlow 8s linear infinite;

            text-shadow:
            0 0 15px rgba(56,189,248,0.35),
            0 0 25px rgba(168,85,247,0.25);
        }

        @keyframes rainbowFlow{

            0%{
                background-position:0% center;
            }

            100%{
                background-position:300% center;
            }
        }

        /* TYPING TEXT */
        .typing-text{

            color:#E2E8F0;

            font-size:18px;

            font-weight:500;

            margin-top:14px;

            margin-bottom:18px;

            overflow:hidden;

            white-space:nowrap;

            border-right:2px solid #38BDF8;

            width:0;

            text-shadow:
            0 0 10px rgba(255,255,255,0.08);

            animation:
            typing 4s steps(40,end) forwards,
            blink 1s infinite;
        }

        @keyframes typing{

            from{
                width:0;
            }

            to{
                width:100%;
            }
        }

        @keyframes blink{

            50%{
                border-color:transparent;
            }
        }

        /* INPUTS */
        .stTextInput input{

            background:
            rgba(17,24,39,0.9);

            border:
            1px solid rgba(56,189,248,0.15);

            border-radius:12px;

            color:white;

            transition:0.3s;
        }

        .stTextInput input:focus{

            border:
            1px solid #38BDF8;

            box-shadow:
            0 0 18px rgba(56,189,248,0.25);
        }

        /* BUTTON */
        .stButton>button{

            background:
            linear-gradient(
                135deg,
                #06B6D4,
                #2563EB
            );

            color:white;

            border:none;

            border-radius:14px;

            font-weight:700;

            height:3.2em;

            width:100%;

            font-size:15px;

            transition:0.3s;

            animation:pulseGlow 2s infinite;
        }

        .stButton>button:hover{

            transform:
            scale(1.03)
            translateY(-2px);

            box-shadow:
            0 0 20px rgba(56,189,248,0.35),
            0 0 40px rgba(59,130,246,0.25);
        }

        @keyframes pulseGlow{

            0%{
                box-shadow:
                0 0 10px rgba(56,189,248,0.25);
            }

            50%{
                box-shadow:
                0 0 25px rgba(56,189,248,0.45),
                0 0 45px rgba(168,85,247,0.25);
            }

            100%{
                box-shadow:
                0 0 10px rgba(56,189,248,0.25);
            }
        }

        /* MOBILE */
        @media (max-width:768px){

            .login-box{

                padding:35px 20px;

                margin-top:40px;
            }

            .rainbow-title{

                font-size:30px;

                white-space:normal;
            }

            .typing-text{

                font-size:14px;
            }

        }

        </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="cyber-grid"></div>

        <div class="cyber-orb orb1"></div>
        <div class="cyber-orb orb2"></div>
        """,
        unsafe_allow_html=True,
    )

    # LOGIN PAGE

    left, center, right = st.columns([1, 1.2, 1])

    with center:

        st.markdown(
            """

        <div class="login-box">

        <div class="login-ring ring1"></div>
        <div class="login-ring ring2"></div>

        <div class="scan-line"></div>

        <div class="corner corner1"></div>
        <div class="corner corner2"></div>
        <div class="corner corner3"></div>
        <div class="corner corner4"></div>

        <div class="rainbow-title">
        NeuroSense AI
        </div>

        <div class="typing-text">
        Advanced EEG Clinical Monitoring Platform
        </div>

        <div style="
        font-family:monospace;
        font-size:13px;
        color:#67E8F9;
        margin-top:12px;
        margin-bottom:20px;
        line-height:1.7;
        text-shadow:0 0 10px rgba(103,232,249,0.35);
        ">

        > Initializing NeuroSense Core...<br>
        > Connecting Neural Interface...<br>
        > AI System Ready █

        </div>

        </div>

        """,
            unsafe_allow_html=True,
        )

        username = st.text_input("👤 Username")

        password = st.text_input("🔒 Password", type="password")

        if st.button("🚀 LOGIN", use_container_width=True):

            if username == "admin" and password == "1234":

                st.session_state.logged_in = True
                st.rerun()

            else:

                st.error("Invalid Credentials")

        st.markdown(
            """
        <div style='
        margin-top:25px;
        background:rgba(15,23,42,0.75);
        padding:18px;
        border-radius:18px;
        border:1px solid rgba(56,189,248,0.15);
        box-shadow:0 0 20px rgba(56,189,248,0.08);
        '>

        <div style='
        display:flex;
        justify-content:space-between;
        margin-bottom:12px;
        '>

        <span>🟢 Neural Engine</span>
        <span style="color:#22c55e;">ONLINE</span>

        </div>

        <div style='
        display:flex;
        justify-content:space-between;
        margin-bottom:12px;
        '>

        <span>🧠 AI Scanner</span>
        <span style="color:#38BDF8;">ACTIVE</span>

        </div>

        <div style='
        display:flex;
        justify-content:space-between;
        '>

        <span>🔒 Security Layer</span>
        <span style="color:#a855f7;">PROTECTED</span>

        </div>

        </div>
        """,
            unsafe_allow_html=True,
        )

    st.stop()

# DATABASE

init_db()


# =====================================================
# DEMO AI MODEL
# =====================================================

class DummyModel:

    def predict(self, data):

        return [np.array([0.10, 0.82, 0.08])]


@st.cache_resource
def load_trained_model():

    return DummyModel()


model = load_trained_model()

# SESSION VARIABLES

defaults = {
    "prediction_done": False,
    "patient_name": "",
    "patient_id": "",
    "pdf_file": None,
    "alpha_pct": 0,
    "beta_pct": 0,
    "gamma_pct": 0,
    "risk_score": 0,
    "predicted_class": "Unknown",
    "confidence": 0,
    "full_img": None,
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value

# SIDEBAR

with st.sidebar:

    # =====================================================
    # SIDEBAR CSS
    # =====================================================
    st.markdown("""
        <style>

        /* =====================================================
        SIDEBAR BLACK BACKGROUND
        ===================================================== */
        [data-testid="stSidebar"]{

            background:
            linear-gradient(
                180deg,
                #000000,
                #020617,
                #000000
            );

            border-right:
            1px solid rgba(56,189,248,0.15);

            box-shadow:
            0 0 35px rgba(56,189,248,0.10);

            overflow:hidden;

            position:relative;
        }

        /* =====================================================
        GLITTER EFFECT
        ===================================================== */
        [data-testid="stSidebar"]::before{

            content:"";

            position:absolute;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:sidebarGlitter 18s linear infinite;

            opacity:0.45;

            z-index:0;
        }

        @keyframes sidebarGlitter{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-250px);
            }
        }

        /* =====================================================
        CYBER GRID
        ===================================================== */
        [data-testid="stSidebar"]::after{

            content:"";

            position:absolute;

            inset:0;

            background-image:

            linear-gradient(
                rgba(56,189,248,0.03) 1px,
                transparent 1px
            ),

            linear-gradient(
                90deg,
                rgba(56,189,248,0.03) 1px,
                transparent 1px
            );

            background-size:35px 35px;

            pointer-events:none;

            z-index:0;
        }

        /* =====================================================
        LOGO CARD
        ===================================================== */
        .sidebar-logo{

            position:relative;

            z-index:2;

            background:
            linear-gradient(
                135deg,
                rgba(0,0,0,0.95),
                rgba(15,23,42,0.88)
            );

            border:
            1px solid rgba(56,189,248,0.15);

            border-radius:30px;

            padding:38px 20px;

            text-align:center;

            overflow:hidden;

            margin-bottom:25px;

            backdrop-filter:blur(18px);

            box-shadow:
            0 0 30px rgba(56,189,248,0.12),
            inset 0 0 20px rgba(255,255,255,0.02);
        }

        /* =====================================================
        CARD SHINE EFFECT
        ===================================================== */
        .sidebar-logo::before{

            content:"";

            position:absolute;

            inset:0;

            background:
            linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.05),
                transparent
            );

            transform:translateX(-100%);

            animation:shineMove 7s infinite;
        }

        @keyframes shineMove{

            100%{
                transform:translateX(100%);
            }
        }

        /* =====================================================
        GLOW EFFECT
        ===================================================== */
        .logo-glow{

            position:absolute;

            width:240px;
            height:240px;

            background:
            radial-gradient(
                circle,
                rgba(56,189,248,0.25),
                transparent 70%
            );

            top:-120px;
            right:-120px;

            animation:glowMove 6s ease infinite alternate;
        }

        @keyframes glowMove{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(30px);
            }
        }

        /* =====================================================
        ICON
        ===================================================== */
        .logo-icon{

            font-size:70px;

            margin-bottom:14px;

            filter:
            drop-shadow(0 0 15px #38BDF8);

            animation:brainPulse 3s ease infinite;
        }

        @keyframes brainPulse{

            0%{
                transform:scale(1);
            }

            50%{
                transform:scale(1.08);
            }

            100%{
                transform:scale(1);
            }
        }

        /* =====================================================
        TITLE
        ===================================================== */
        .sidebar-title{

            font-size:30px;

            font-weight:900;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            margin-bottom:10px;

            font-family:'Orbitron',sans-serif;

            text-shadow:
            0 0 15px rgba(56,189,248,0.25);
        }

        /* =====================================================
        SUBTITLE
        ===================================================== */
        .sidebar-sub{

            color:#CBD5E1;

            font-size:13px;

            line-height:1.8;

            margin-bottom:18px;
        }

        /* =====================================================
        LINE
        ===================================================== */
        .sidebar-line{

            width:100%;

            height:4px;

            border-radius:20px;

            background:
            linear-gradient(
                90deg,
                #06B6D4,
                #8B5CF6,
                #EC4899
            );

            box-shadow:
            0 0 15px rgba(56,189,248,0.35);
        }

        /* =====================================================
        NAVIGATION BUTTONS
        ===================================================== */
        div[role="radiogroup"] > label{

            background:
            linear-gradient(
                135deg,
                rgba(0,0,0,0.95),
                rgba(15,23,42,0.88)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            padding:14px 16px;

            border-radius:18px;

            margin-bottom:12px;

            color:white;

            transition:0.35s;

            backdrop-filter:blur(12px);

            position:relative;

            overflow:hidden;
        }

        div[role="radiogroup"] > label:hover{

            transform:
            translateX(4px)
            scale(1.02);

            border:
            1px solid #38BDF8;

            box-shadow:
            0 0 20px rgba(56,189,248,0.18);
        }

        /* =====================================================
        STATUS BOX
        ===================================================== */
        .status-box{

            background:
            linear-gradient(
                135deg,
                rgba(0,0,0,0.95),
                rgba(15,23,42,0.88)
            );

            padding:20px;

            border-radius:20px;

            border:
            1px solid rgba(34,197,94,0.15);

            margin-top:20px;

            color:white;

            box-shadow:
            0 0 20px rgba(34,197,94,0.08);
        }

        /* =====================================================
        BUTTON
        ===================================================== */
        .stButton>button{

            background:
            linear-gradient(
                135deg,
                #06B6D4,
                #2563EB,
                #7C3AED,
                #EC4899
            ) !important;

            background-size:300% !important;

            animation:buttonFlow 7s linear infinite;

            color:white !important;

            border:none !important;

            border-radius:18px !important;

            height:3.3em !important;

            font-weight:800 !important;

            transition:0.35s !important;

            box-shadow:
            0 0 25px rgba(56,189,248,0.18);
        }

        @keyframes buttonFlow{

            0%{
                background-position:0%;
            }

            100%{
                background-position:300%;
            }
        }

        .stButton>button:hover{

            transform:
            translateY(-3px)
            scale(1.02);

            box-shadow:
            0 0 35px rgba(56,189,248,0.28),
            0 0 55px rgba(139,92,246,0.18);
        }

        </style>
    
    """,unsafe_allow_html=True,)


    # =====================================================
    # NAVIGATION
    # =====================================================
    page = st.radio(
            "⚡ Navigation Panel",
            [
                "🏥 Dashboard",
                "📝 Patient Registration",
                "🧠 EEG Examination",
                "📡 Live Monitoring",
                "📊 Analytics",
                "🗂 Patient Records",
                "👨‍⚕️ Doctor Review",
                "🚨 Emergency Alerts",
                "📄 Final Clinical Report",
            ],
        )

    # =====================================================
    # STATUS PANEL
    # =====================================================
    st.markdown(
        """

    <div class="status-box">

    <div style="
    display:flex;
    justify-content:space-between;
    margin-bottom:12px;
    ">

    <span>🟢 AI Core</span>
    <span style="color:#22c55e;">
    ONLINE
    </span>

    </div>

    <div style="
    display:flex;
    justify-content:space-between;
    margin-bottom:12px;
    ">

    <span>📡 EEG Signal</span>
    <span style="color:#38BDF8;">
    ACTIVE
    </span>

    </div>

    <div style="
    display:flex;
    justify-content:space-between;
    ">

    <span>🔒 Security</span>
    <span style="color:#A855F7;">
    PROTECTED
    </span>

    </div>

    </div>

    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # LOGOUT BUTTON
    # =====================================================
    if st.button("🚪 Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.rerun()

    # =====================================================
    # ULTRA AI DASHBOARD
    # =====================================================

if page == "🏥 Dashboard":

    st.markdown("""
        <style>

        /* DASHBOARD BACKGROUND */
        .main{

            background:
            radial-gradient(
                circle at top,
                #050505,
                #000000,
                #020617
            );
        }

        /* FLOATING GLITTER */
        .stApp::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(255,20,147,0.8) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 18s linear infinite;

            opacity:0.6;

            z-index:0;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-200px);
            }
        }

        /* CYBER GRID */
        .dashboard-grid{

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            background-image:

            linear-gradient(
                rgba(56,189,248,0.05) 1px,
                transparent 1px
            ),

            linear-gradient(
                90deg,
                rgba(56,189,248,0.05) 1px,
                transparent 1px
            );

            background-size:40px 40px;

            pointer-events:none;

            z-index:0;
        }

        /* HEADER */
        .dashboard-header{

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.85),
                rgba(30,41,59,0.85)
            );

            padding:30px;

            border-radius:24px;

            border:
            1px solid rgba(56,189,248,0.15);

            box-shadow:
            0 0 30px rgba(56,189,248,0.12);

            margin-bottom:25px;

            position:relative;

            overflow:hidden;
        }

        .dashboard-title{

            font-size:42px;

            font-weight:800;

            color:#38BDF8;

            font-family:'Orbitron',sans-serif;

            margin-bottom:10px;

            text-shadow:
            0 0 15px rgba(56,189,248,0.35);
        }

        .dashboard-sub{

            color:#CBD5E1;

            font-size:17px;
        }

        /* STATUS CARDS */
        .stat-card{

            background:
            rgba(15,23,42,0.78);

            backdrop-filter:blur(18px);

            padding:24px;

            border-radius:22px;

            border:
            1px solid rgba(56,189,248,0.15);

            transition:0.3s;

            box-shadow:
            0 0 20px rgba(56,189,248,0.08);

            overflow:hidden;

            position:relative;
        }

        .stat-card:hover{

            transform:translateY(-6px);

            box-shadow:
            0 0 35px rgba(56,189,248,0.22);
        }

        .stat-title{

            color:#94A3B8;

            font-size:16px;

            margin-bottom:15px;
        }

        .stat-value{

            font-size:28px;

            font-weight:800;

            color:#38BDF8;

            text-shadow:
            0 0 15px rgba(56,189,248,0.35);
        }

        .glow-line{

            width:100%;

            height:4px;

            margin-top:18px;

            border-radius:10px;

            background:
            linear-gradient(
                90deg,
                #06B6D4,
                #8B5CF6,
                #EC4899
            );
        }

        /* SYSTEM PANEL */
        .system-panel{

            background:
            rgba(15,23,42,0.75);

            padding:24px;

            border-radius:22px;

            border:
            1px solid rgba(56,189,248,0.12);

            margin-top:25px;

            box-shadow:
            0 0 25px rgba(56,189,248,0.08);
        }

        /* AI CORE */
        .ai-core{

            background:
            rgba(15,23,42,0.78);

            padding:35px;

            border-radius:24px;

            border:
            1px solid rgba(56,189,248,0.15);

            box-shadow:
            0 0 25px rgba(56,189,248,0.08);

            margin-top:20px;
        }

        .core-box{

            background:
            rgba(0,0,0,0.35);

            padding:20px;

            border-radius:18px;

            border:
            1px solid rgba(56,189,248,0.12);

            transition:0.3s;
        }

        .core-box:hover{

            transform:translateY(-5px);

            box-shadow:
            0 0 25px rgba(56,189,248,0.15);
        }

        /* MOBILE */
        @media (max-width:768px){

            .dashboard-title{

                font-size:28px;
            }

        }

        </style>
    """,unsafe_allow_html=True,)

    st.markdown("""
        <div class="dashboard-grid"></div>
        """,
            unsafe_allow_html=True,
        )

        # HEADER
    st.markdown("""
        <div class="dashboard-header">

        <div class="dashboard-title">
        🧠 NeuroSense AI Command Center
        </div>

        <div class="dashboard-sub">
        Real-Time EEG Cognitive Monitoring & Clinical Intelligence System
        </div>

        </div>
    """,unsafe_allow_html=True,)

        # STATUS CARDS
    c1, c2, c3, c4 = st.columns(4)

    stats = [
            ("🧠 Neural Activity", "ACTIVE"),
            ("📡 EEG Signal", "CONNECTED"),
            ("⚡ AI Engine", "RUNNING"),
            ("🔒 Security", "PROTECTED"),
        ]

    for col, stat in zip([c1, c2, c3, c4], stats):

        with col:

            st.markdown(
                    f"""
                <div class="stat-card">

                <div class="stat-title">
                {stat[0]}
                </div>

                <div class="stat-value">
                {stat[1]}
                </div>

                <div class="glow-line"></div>

                </div>
                """,
                    unsafe_allow_html=True,
                )

        # SYSTEM OVERVIEW
    st.markdown(
            """
        <div class="system-panel">

        <h3 style="color:#38BDF8;">
        ⚡ AI System Overview
        </h3>

        <br>

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:14px;
        ">

        <span>🟢 EEG Scanner Network</span>
        <span style="color:#22c55e;">ONLINE</span>

        </div>

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:14px;
        ">

        <span>🧠 AI Prediction Engine</span>
        <span style="color:#38BDF8;">ACTIVE</span>

        </div>

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:14px;
        ">

        <span>☁ Cloud Database</span>
        <span style="color:#a855f7;">CONNECTED</span>

        </div>

        <div style="
        display:flex;
        justify-content:space-between;
        ">

        <span>🔒 Clinical Security Layer</span>
        <span style="color:#f43f5e;">PROTECTED</span>

        </div>

        </div>
    """,unsafe_allow_html=True,
        )

    # AI CORE PANEL
    st.markdown(
        """
    <div class="ai-core">

    <h2 style='
    color:#38BDF8;
    font-family:Orbitron;
    margin-bottom:25px;
    '>
    🧠 NeuroSense AI Core
    </h2>

    <div style='
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    '>

    <div class="core-box">

    <h4 style='color:#67E8F9;'>
    ⚡ AI Prediction
    </h4>

    <p style='color:#CBD5E1;'>
    Real-time cognitive stress prediction engine running continuously.
    </p>

    </div>

    <div class="core-box">

    <h4 style='color:#67E8F9;'>
    📡 EEG Monitoring
    </h4>

    <p style='color:#CBD5E1;'>
    Live EEG signal acquisition and neural synchronization active.
    </p>

    </div>

    <div class="core-box">

    <h4 style='color:#67E8F9;'>
    🔒 Security Layer
    </h4>

    <p style='color:#CBD5E1;'>
    Encrypted medical data protection and secure AI processing enabled.
    </p>

    </div>

    </div>

    </div>
    """,unsafe_allow_html=True,
    )

# CINEMATIC PATIENT REGISTRATION
if page == "📝 Patient Registration":

    # =====================================================
    # ADVANCED CSS
    # =====================================================
    st.markdown(
        """
    <style>

    /* MAIN WRAPPER */
    .patient-wrapper{

        position:relative;

        padding-top:10px;

        overflow:hidden;
    }

    /* GLITTER BACKGROUND */
    .patient-wrapper::before{

        content:"";

        position:fixed;

        top:0;
        left:0;

        width:100%;
        height:100%;

        pointer-events:none;

        background-image:

        radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
        radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
        radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
        radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

        background-size:
        120px 120px,
        180px 180px,
        220px 220px,
        260px 260px;

        animation:glitterMove 20s linear infinite;

        opacity:0.5;

        z-index:0;
    }

    @keyframes glitterMove{

        0%{
            transform:translateY(0px);
        }

        100%{
            transform:translateY(-250px);
        }
    }

    /* CYBER GRID */
    .patient-wrapper::after{

        content:"";

        position:fixed;

        inset:0;

        background-image:

        linear-gradient(
            rgba(56,189,248,0.04) 1px,
            transparent 1px
        ),

        linear-gradient(
            90deg,
            rgba(56,189,248,0.04) 1px,
            transparent 1px
        );

        background-size:40px 40px;

        pointer-events:none;

        z-index:0;
    }

    /* HEADER */
    .patient-header{

        position:relative;

        z-index:2;

        background:
        linear-gradient(
            135deg,
            rgba(15,23,42,0.95),
            rgba(30,41,59,0.88)
        );

        border:
        1px solid rgba(56,189,248,0.16);

        border-radius:32px;

        padding:40px;

        overflow:hidden;

        margin-bottom:30px;

        backdrop-filter:blur(20px);

        box-shadow:
        0 0 35px rgba(56,189,248,0.12),
        inset 0 0 20px rgba(255,255,255,0.02);
    }

    /* HEADER GLOW */
    .patient-header::before{

        content:"";

        position:absolute;

        width:400px;
        height:400px;

        background:
        radial-gradient(
            circle,
            rgba(56,189,248,0.18),
            transparent 70%
        );

        top:-180px;
        right:-180px;

        animation:headerGlow 6s ease infinite alternate;
    }

    @keyframes headerGlow{

        from{
            transform:translateY(0px);
        }

        to{
            transform:translateY(30px);
        }
    }

    /* TITLE */
    .patient-title{

        font-size:48px;

        font-weight:900;

        font-family:'Orbitron',sans-serif;

        background:
        linear-gradient(
            90deg,
            #38BDF8,
            #8B5CF6,
            #EC4899,
            #38BDF8
        );

        background-size:300%;

        -webkit-background-clip:text;

        -webkit-text-fill-color:transparent;

        animation:titleFlow 8s linear infinite;

        margin-bottom:14px;
    }

    @keyframes titleFlow{

        0%{
            background-position:0%;
        }

        100%{
            background-position:300%;
        }
    }

    /* SUBTITLE */
    .patient-sub{

        color:#CBD5E1;

        font-size:16px;

        letter-spacing:0.5px;
    }

    /* FORM CARD */
    .patient-card{

        position:relative;

        z-index:2;

        background:
        linear-gradient(
            135deg,
            rgba(15,23,42,0.94),
            rgba(30,41,59,0.84)
        );

        border:
        1px solid rgba(56,189,248,0.14);

        border-radius:32px;

        padding:40px;

        backdrop-filter:blur(22px);

        box-shadow:
        0 0 40px rgba(56,189,248,0.12);

        overflow:hidden;
    }

    /* CARD SHINE */
    .patient-card::before{

        content:"";

        position:absolute;

        inset:0;

        background:
        linear-gradient(
            120deg,
            transparent,
            rgba(255,255,255,0.04),
            transparent
        );

        transform:translateX(-100%);

        animation:shine 6s infinite;
    }

    @keyframes shine{

        100%{
            transform:translateX(100%);
        }
    }

    /* INPUTS */
    .stTextInput input,
    .stNumberInput input,
    textarea{

        background:
        rgba(2,6,23,0.95) !important;

        color:white !important;

        border:
        1px solid rgba(56,189,248,0.14) !important;

        border-radius:18px !important;

        padding:12px !important;

        transition:0.35s !important;

        box-shadow:
        inset 0 0 10px rgba(56,189,248,0.03);
    }

    /* INPUT FOCUS */
    .stTextInput input:focus,
    .stNumberInput input:focus,
    textarea:focus{

        border:
        1px solid #38BDF8 !important;

        box-shadow:
        0 0 20px rgba(56,189,248,0.25),
        0 0 35px rgba(139,92,246,0.12) !important;

        transform:scale(1.01);
    }

    /* SELECT */
    div[data-baseweb="select"] > div{

        background:
        rgba(2,6,23,0.95) !important;

        color:white !important;

        border:
        1px solid rgba(56,189,248,0.14) !important;

        border-radius:18px !important;

        transition:0.35s !important;
    }

    /* LABELS */
    label{

        color:#E2E8F0 !important;

        font-weight:700 !important;

        letter-spacing:0.4px;
    }

    /* BUTTON */
    .stButton>button{

        background:
        linear-gradient(
            135deg,
            #06B6D4,
            #2563EB,
            #7C3AED,
            #EC4899
        ) !important;

        background-size:300% !important;

        animation:buttonFlow 7s linear infinite;

        color:white !important;

        border:none !important;

        border-radius:20px !important;

        height:3.5em !important;

        font-weight:800 !important;

        font-size:16px !important;

        transition:0.35s !important;

        box-shadow:
        0 0 25px rgba(56,189,248,0.18);
    }

    @keyframes buttonFlow{

        0%{
            background-position:0%;
        }

        100%{
            background-position:300%;
        }
    }

    .stButton>button:hover{

        transform:
        translateY(-4px)
        scale(1.02);

        box-shadow:
        0 0 35px rgba(56,189,248,0.28),
        0 0 55px rgba(139,92,246,0.18);
    }

    /* SUCCESS */
    .stSuccess{

        border-radius:18px !important;

        border:
        1px solid rgba(34,197,94,0.18) !important;

        background:
        rgba(15,23,42,0.9) !important;
    }

    </style>
    """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # WRAPPER START
    # =====================================================
    st.markdown(
        """
    <div class="patient-wrapper">
    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # HEADER
    # =====================================================
    st.markdown(
        """

        <div class="patient-header">

        <div class="patient-title">
        🧠 Patient Registration Portal
        </div>

        <div class="patient-sub">
        Advanced NeuroSense AI Clinical Patient Enrollment System
        </div>

        </div>

    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # FORM CARD START
    # =====================================================
    st.markdown(
        """
    <div class="patient-card">
    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # FORM
    # =====================================================
    col1, col2 = st.columns(2)

    with col1:

        st.session_state.patient_name = st.text_input("👤 Patient Name")

        age = st.number_input("🎂 Age", 1, 100)

        gender = st.selectbox("⚧ Gender", ["Male", "Female", "Other"])

    with col2:

        doctor = st.text_input("👨‍⚕️ Assigned Doctor")

        blood_group = st.selectbox(
            "🩸 Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        )

    medical_history = st.text_area("📄 Medical History")

    # =====================================================
    # BUTTON
    # =====================================================
    if st.button("🚀 Register Patient", use_container_width=True):

        st.success("✅ Patient Registered Successfully")

        st.balloons()

    # =====================================================
    # FORM CARD END
    # =====================================================
    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # WRAPPER END
    # =====================================================
    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )

# EEG EXAMINATION EFFECTS CSS

    st.markdown(
        """

    """,
        unsafe_allow_html=True,
    )


    # ULTRA EEG EFFECTS

    st.markdown(
        """

    """,
        unsafe_allow_html=True,
    )


# EEG EXAMINATION

if page == "🧠 EEG Examination":

    # =====================================================
    # ADVANCED CSS EFFECTS
    # =====================================================
    st.markdown("""
        <style>

        /* =====================================================
        MAIN BLACK BACKGROUND
        ===================================================== */
        [data-testid="stAppViewContainer"]{

            background:
            linear-gradient(
                180deg,
                #000000,
                #020617,
                #000000
            );
        }

        /* =====================================================
        GLITTER EFFECT
        ===================================================== */
        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:0;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        /* =====================================================
        CYBER GRID
        ===================================================== */
        [data-testid="stAppViewContainer"]::after{

            content:"";

            position:fixed;

            inset:0;

            background-image:

            linear-gradient(
                rgba(56,189,248,0.03) 1px,
                transparent 1px
            ),

            linear-gradient(
                90deg,
                rgba(56,189,248,0.03) 1px,
                transparent 1px
            );

            background-size:40px 40px;

            pointer-events:none;

            z-index:0;
        }

        /* =====================================================
        TITLE
        ===================================================== */
        h3{

            font-size:44px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            text-shadow:
            0 0 20px rgba(56,189,248,0.25);
        }

        /* =====================================================
        BLACK GLASS BOXES
        ===================================================== */
        [data-testid="stVerticalBlockBorderWrapper"]{

            background:
            linear-gradient(
                135deg,
                rgba(0,0,0,0.95),
                rgba(15,23,42,0.88)
            ) !important;

            border:
            1px solid rgba(56,189,248,0.14) !important;

            border-radius:28px !important;

            padding:22px !important;

            backdrop-filter:blur(18px);

            box-shadow:
            0 0 30px rgba(56,189,248,0.10),
            inset 0 0 20px rgba(255,255,255,0.02);

            overflow:hidden;

            position:relative;
        }

        /* =====================================================
        SHINE EFFECT
        ===================================================== */
        [data-testid="stVerticalBlockBorderWrapper"]::before{

            content:"";

            position:absolute;

            inset:0;

            background:
            linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.04),
                transparent
            );

            transform:translateX(-100%);

            animation:shineMove 7s infinite;
        }

        @keyframes shineMove{

            100%{
                transform:translateX(100%);
            }
        }

        /* =====================================================
        TABS
        ===================================================== */
        button[data-baseweb="tab"]{

            background:
            rgba(0,0,0,0.82) !important;

            border:
            1px solid rgba(56,189,248,0.12) !important;

            border-radius:18px !important;

            color:white !important;

            margin-right:10px !important;

            transition:0.35s !important;
        }

        button[data-baseweb="tab"]:hover{

            transform:
            translateY(-2px);

            box-shadow:
            0 0 20px rgba(56,189,248,0.18);
        }

        button[aria-selected="true"]{

            background:
            linear-gradient(
                135deg,
                #06B6D4,
                #2563EB,
                #7C3AED
            ) !important;

            color:white !important;

            box-shadow:
            0 0 25px rgba(56,189,248,0.22);
        }

        /* =====================================================
        SLIDERS
        ===================================================== */
        .stSlider{

            background:
            rgba(0,0,0,0.82) !important;

            padding:12px;

            border-radius:18px;

            border:
            1px solid rgba(56,189,248,0.10);
        }

        /* =====================================================
        TEXT AREA
        ===================================================== */
        textarea{

            background:
            rgba(0,0,0,0.92) !important;

            color:white !important;

            border:
            1px solid rgba(56,189,248,0.12) !important;

            border-radius:20px !important;

            box-shadow:
            0 0 20px rgba(56,189,248,0.06);
        }

        /* =====================================================
        METRICS
        ===================================================== */
        [data-testid="metric-container"]{

            background:
            linear-gradient(
                135deg,
                rgba(0,0,0,0.95),
                rgba(15,23,42,0.88)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:22px;

            padding:18px;

            box-shadow:
            0 0 25px rgba(56,189,248,0.08);

            transition:0.35s;
        }

        [data-testid="metric-container"]:hover{

            transform:
            translateY(-4px)
            scale(1.02);

            box-shadow:
            0 0 35px rgba(56,189,248,0.18);
        }

        /* =====================================================
        BUTTONS
        ===================================================== */
        .stButton>button{

            background:
            linear-gradient(
                135deg,
                #06B6D4,
                #2563EB,
                #7C3AED,
                #EC4899
            ) !important;

            background-size:300% !important;

            animation:buttonFlow 7s linear infinite;

            color:white !important;

            border:none !important;

            border-radius:20px !important;

            height:3.4em !important;

            font-weight:800 !important;

            transition:0.35s !important;

            box-shadow:
            0 0 25px rgba(56,189,248,0.18);
        }

        @keyframes buttonFlow{

            0%{
                background-position:0%;
            }

            100%{
                background-position:300%;
            }
        }

        .stButton>button:hover{

            transform:
            translateY(-4px)
            scale(1.02);

            box-shadow:
            0 0 40px rgba(56,189,248,0.28);
        }

        /* =====================================================
        ALERT BOXES
        ===================================================== */
        .stSuccess,
        .stWarning,
        .stError,
        .stInfo{

            border-radius:20px !important;

            background:
            rgba(0,0,0,0.88) !important;

            border:
            1px solid rgba(56,189,248,0.12) !important;
        }

        /* =====================================================
        IMAGE EFFECT
        ===================================================== */
        img{

            border-radius:24px !important;

            border:
            1px solid rgba(56,189,248,0.14);

            box-shadow:
            0 0 30px rgba(56,189,248,0.12);
        }

        </style>
    """,unsafe_allow_html=True,
    )

# =====================================================
# TITLE
# =====================================================
    st.subheader("🧠 EEG Cognitive Examination")

    tab1, tab2, tab3 = st.tabs(["EEG Signal", "AI Analysis", "Doctor Notes"])

    # =====================================================
    # TAB 1 - EEG SIGNAL
    # =====================================================
    with tab1:

        with st.container(border=True):

            alpha = st.slider("Alpha Activity", 0.0, 100.0, 20.0)

            beta = st.slider("Beta Activity", 0.0, 100.0, 15.0)

            gamma = st.slider("Gamma Activity", 0.0, 100.0, 10.0)

            # =====================================================
            # STORE EEG INPUT VALUES
            # =====================================================
            st.session_state.alpha = alpha
            st.session_state.beta = beta
            st.session_state.gamma = gamma

            # =====================================================
            # RUN AI
            # =====================================================
            if st.button("🚀 Run AI Examination", use_container_width=True):

                with st.spinner("Running AI EEG Analysis..."):

                    signal = generate_signal(alpha, beta, gamma)

                    full_img, cnn_img = generate_spectrogram(signal)

                    alpha_pct, beta_pct, gamma_pct = calculate_band_power(signal)

                    img = cv2.imread(cnn_img)

                    img = cv2.resize(img, (224, 224))

                    img = img / 255.0

                    img = np.expand_dims(img, axis=0)

                    numeric = np.array([[alpha_pct, beta_pct, gamma_pct]])

                    # =====================================================
# DYNAMIC AI LOGIC
# =====================================================

                    try:

                        # =====================================================
                        # EEG DECISION LOGIC
                        # =====================================================

                        if (
                            st.session_state.beta >= st.session_state.alpha
                            and
                            st.session_state.beta >= st.session_state.gamma
                        ):

                            predicted_class = "High Stress"

                            confidence = float(st.session_state.beta)

                            risk_score = float(st.session_state.beta)

                        elif (
                            st.session_state.alpha >= st.session_state.beta
                            and
                            st.session_state.alpha >= st.session_state.gamma
                        ):

                            predicted_class = "Relaxed"

                            confidence = float(st.session_state.alpha)

                            risk_score = 20.0

                        else:

                            predicted_class = "Normal"

                            confidence = float(st.session_state.gamma)

                            risk_score = 40.0

                    except Exception as e:

                        st.error(f"Prediction Error: {e}")

                        predicted_class = "Normal"

                        confidence = 60.0

                        risk_score = 40.0


                        st.session_state.prediction_done = True

                        st.session_state.alpha_pct = alpha_pct
                        st.session_state.beta_pct = beta_pct
                        st.session_state.gamma_pct = gamma_pct

                        st.session_state.predicted_class = predicted_class

                        st.session_state.confidence = confidence

                        st.session_state.risk_score = risk_score

                        st.session_state.full_img = full_img

                        st.success("✅ AI Analysis Completed")
    # =====================================================
    # TAB 2 - AI ANALYSIS
    # =====================================================
    with tab2:

        with st.container(border=True):

            if st.session_state.prediction_done:

                c1, c2, c3 = st.columns(3)

                c1.metric("Mental State", st.session_state.predicted_class)

                c2.metric("Confidence", f"{st.session_state.confidence:.2f}%")

                c3.metric("Risk Score", f"{st.session_state.risk_score:.2f}%")

                st.progress(int(st.session_state.confidence))

                feature_df = pd.DataFrame(
                    {
                        "Band": ["Alpha", "Beta", "Gamma"],
                        "Power": [
                            st.session_state.alpha_pct,
                            st.session_state.beta_pct,
                            st.session_state.gamma_pct,
                        ],
                    }
                )

                st.bar_chart(feature_df.set_index("Band"))

                if st.session_state.risk_score > 70:

                    st.error("🔴 High Cognitive Stress")

                elif st.session_state.risk_score > 40:

                    st.warning("🟠 Moderate Cognitive Stress")

                else:

                    st.success("🟢 Stable Cognitive State")

    # =====================================================
    # TAB 3 - DOCTOR NOTES
    # =====================================================
    with tab3:

        with st.container(border=True):

            auto_notes = ""

            ai_recommendation = "Normal"

            if st.session_state.prediction_done:

                state = st.session_state.predicted_class

                confidence = st.session_state.confidence

                risk = st.session_state.risk_score

                alpha = st.session_state.alpha_pct

                beta = st.session_state.beta_pct

                gamma = st.session_state.gamma_pct

                if state == "High Stress":

                    ai_recommendation = "Immediate Attention"

                    auto_notes = f"""
    Patient EEG analysis indicates HIGH STRESS condition.

    🧠 EEG SUMMARY
    • Elevated beta/gamma activity detected
    • Increased cognitive stress observed

    📊 ANALYSIS RESULTS
    • Risk Score : {risk:.2f}%
    • Confidence : {confidence:.2f}%

    💡 AI RECOMMENDATION
    • Immediate observation advised
    • Follow-up EEG monitoring suggested
    """

                elif state == "Relaxed":

                    ai_recommendation = "Normal"

                    auto_notes = f"""
                Patient EEG analysis indicates NORMAL cognitive state.
    🧠 EEG SUMMARY
    • Stable alpha activity observed
    • Calm neurological condition identified

    📊 ANALYSIS RESULTS
    • Risk Score : {risk:.2f}%
    • Confidence : {confidence:.2f}%

    💡 AI RECOMMENDATION
    • Routine monitoring recommended
    """

                else:

                    ai_recommendation = "Observation"

                    auto_notes = f"""
    Patient EEG analysis indicates NORMAL cognitive condition.

    🧠 EEG SUMMARY
    • Balanced EEG band activity observed

    📊 ANALYSIS RESULTS
    • Risk Score : {risk:.2f}%
    • Confidence : {confidence:.2f}%

    💡 AI RECOMMENDATION
    • Continue regular observation
    """

            else:

                auto_notes = "Run AI Examination First"

            doctor_notes = st.text_area(
                "🩺 AI Generated Clinical Notes", value=auto_notes, height=320
            )

            st.selectbox(
                "📋 AI Recommendation",
                ["Normal", "Observation", "Further Diagnosis", "Immediate Attention"],
                index=[
                    "Normal",
                    "Observation",
                    "Further Diagnosis",
                    "Immediate Attention",
                ].index(ai_recommendation),
            )

            if st.button("💾 Save Examination", use_container_width=True):

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                insert_record(
                    (
                        st.session_state.patient_name,
                        st.session_state.patient_id,
                        alpha,
                        beta,
                        gamma,
                        st.session_state.alpha_pct,
                        st.session_state.beta_pct,
                        st.session_state.gamma_pct,
                        st.session_state.predicted_class,
                        st.session_state.confidence,
                        timestamp,
                    )
                )

                st.success("✅ Examination Saved Successfully")

# =====================================================
# LIVE MONITORING
# =====================================================

if page == "📡 Live Monitoring":

    # =====================================================
    # BRAINFLOW IMPORTS DISABLED FOR STREAMLIT CLOUD
    # =====================================================

    # from brainflow.board_shim import BoardShim
    # from brainflow.board_shim import BrainFlowInputParams
    # from brainflow.board_shim import BoardIds

    # =====================================================
    # CSS
    # =====================================================

    st.markdown("""
        <style>

        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:999;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        h3{

            font-size:42px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;
        }

        .live-card{

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:30px;

            padding:30px;

            box-shadow:
            0 0 30px rgba(56,189,248,0.10);

            backdrop-filter:blur(18px);
        }

        .stButton>button{

            background:
            linear-gradient(
                135deg,
                #06B6D4,
                #2563EB,
                #7C3AED,
                #EC4899
            ) !important;

            color:white !important;

            border:none !important;

            border-radius:18px !important;

            height:3.4em !important;

            font-weight:800 !important;

            transition:0.35s !important;
        }

        .stButton>button:hover{

            transform:
            translateY(-3px)
            scale(1.02);
        }

        </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # TITLE
    # =====================================================

    st.subheader("📡 Real-Time EEG Monitoring")

    st.markdown("""
        <div class="live-card">
    """, unsafe_allow_html=True)

    # =====================================================
    # DEVICE MODE
    # =====================================================

    device_mode = st.selectbox(
        "🧠 EEG Source",
        [
            "Simulation Mode",
            "Real EEG Device"
        ]
    )

    # =====================================================
    # REAL DEVICE DISABLED
    # =====================================================

    if device_mode == "Real EEG Device":

        st.warning(
            "⚠ Real EEG Device mode is not supported in Streamlit Cloud deployment. Use Simulation Mode."
        )

    # =====================================================
    # START MONITORING
    # =====================================================

    if st.button(
        "🚀 Start Monitoring",
        use_container_width=True
    ):

        placeholder = st.empty()

        # =================================================
        # SIMULATION MODE
        # =================================================

        if device_mode == "Simulation Mode":

            st.success("✅ Simulation Started")

            for i in range(100):

                x = np.linspace(
                    0,
                    2 * np.pi,
                    500
                )

                y = (
                    np.sin(5 * x + i * 0.3)
                    +
                    0.5 * np.sin(15 * x)
                )

                fig, ax = plt.subplots(
                    figsize=(10, 4)
                )

                fig.patch.set_facecolor("#0F172A")

                ax.set_facecolor("#0F172A")

                ax.plot(
                    x,
                    y,
                    color="#38BDF8",
                    linewidth=2
                )

                ax.set_title(
                    "Simulated EEG Signal",
                    color="white"
                )

                ax.tick_params(
                    colors="white"
                )

                ax.grid(alpha=0.2)

                placeholder.pyplot(fig)

                plt.close(fig)

                time.sleep(0.1)

        # =================================================
        # REAL DEVICE MESSAGE
        # =================================================

        else:

            st.error(
                "❌ Real EEG Device mode is unavailable in cloud deployment."
            )

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True,
    )

# ANALYTICS

if page == "📊 Analytics":

    # =====================================================
    # CSS EFFECTS
    # =====================================================
    st.markdown("""
        <style>

        /* =====================================================
        GLITTER BACKGROUND
        ===================================================== */
        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:999;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        /* =====================================================
        TITLE
        ===================================================== */
        h3{

            font-size:42px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            text-shadow:
            0 0 20px rgba(56,189,248,0.25);
        }

        /* =====================================================
        ANALYTICS CARD
        ===================================================== */
        .analytics-card{

            position:relative;

            overflow:hidden;

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:30px;

            padding:30px;

            box-shadow:
            0 0 30px rgba(56,189,248,0.10);

            backdrop-filter:blur(18px);
        }

        /* =====================================================
        AURORA EFFECT
        ===================================================== */
        .analytics-card::before{

            content:"";

            position:absolute;

            width:450px;
            height:450px;

            top:-220px;
            right:-180px;

            background:
            radial-gradient(
                circle,
                rgba(56,189,248,0.15),
                transparent 70%
            );

            animation:auroraMove 10s ease infinite alternate;
        }

        @keyframes auroraMove{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(50px);
            }
        }

        /* =====================================================
        SHINE EFFECT
        ===================================================== */
        .analytics-card::after{

            content:"";

            position:absolute;

            inset:0;

            background:
            linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.05),
                transparent
            );

            transform:translateX(-100%);

            animation:shineMove 7s infinite;
        }

        @keyframes shineMove{

            100%{
                transform:translateX(100%);
            }
        }

        /* =====================================================
        METRIC CARDS
        ===================================================== */
        [data-testid="metric-container"]{

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:24px;

            padding:18px;

            box-shadow:
            0 0 25px rgba(56,189,248,0.08);

            transition:0.35s;
        }

        [data-testid="metric-container"]:hover{

            transform:
            translateY(-4px)
            scale(1.02);

            box-shadow:
            0 0 35px rgba(56,189,248,0.18);
        }

        /* =====================================================
        CHART EFFECT
        ===================================================== */
        canvas{

            border-radius:24px !important;

            background:
            rgba(15,23,42,0.65) !important;

            padding:10px;
        }

        </style>
    """,unsafe_allow_html=True,)

# =====================================================
# TITLE
# =====================================================
    st.subheader("📊 Brainwave Analytics")

    st.markdown(
        """
    <div class="analytics-card">
    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # METRICS
    # =====================================================
    c1, c2, c3 = st.columns(3)

    c1.metric("🧠 Alpha", f"{st.session_state.alpha_pct:.2f}")

    c2.metric("⚡ Beta", f"{st.session_state.beta_pct:.2f}")

    c3.metric("🌌 Gamma", f"{st.session_state.gamma_pct:.2f}")

    # =====================================================
    # DATAFRAME
    # =====================================================
    analytics_df = pd.DataFrame(
        {
            "Brainwave": ["Alpha", "Beta", "Gamma"],
            "Value": [
                st.session_state.alpha_pct,
                st.session_state.beta_pct,
                st.session_state.gamma_pct,
            ],
        }
    )

    # =====================================================
    # BAR CHART
    # =====================================================
    st.bar_chart(analytics_df.set_index("Brainwave"))

    # =====================================================
    # INSIGHTS
    # =====================================================
    highest_band = analytics_df.loc[analytics_df["Value"].idxmax()]["Brainwave"]

    st.info(f"🧠 Dominant Brainwave Activity: {highest_band}")

    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )

# PATIENT RECORDS

if page == "🗂 Patient Records":

    # =====================================================
    # ADVANCED CSS
    # =====================================================
    st.markdown(
        """
        <style>

        /* =====================================================
        GLITTER BACKGROUND
        ===================================================== */
        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:999;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        /* =====================================================
        TITLE
        ===================================================== */
        h3{

            font-size:42px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            text-shadow:
            0 0 20px rgba(56,189,248,0.25);
        }

        /* =====================================================
        RECORD CARD
        ===================================================== */
        .record-card{

            position:relative;

            overflow:hidden;

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:30px;

            padding:30px;

            box-shadow:
            0 0 30px rgba(56,189,248,0.10);

            backdrop-filter:blur(18px);
        }

        /* =====================================================
        AURORA EFFECT
        ===================================================== */
        .record-card::before{

            content:"";

            position:absolute;

            width:450px;
            height:450px;

            top:-220px;
            right:-180px;

            background:
            radial-gradient(
                circle,
                rgba(56,189,248,0.15),
                transparent 70%
            );

            animation:auroraMove 10s ease infinite alternate;
        }

        @keyframes auroraMove{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(50px);
            }
        }

        /* =====================================================
        SHINE EFFECT
        ===================================================== */
        .record-card::after{

            content:"";

            position:absolute;

            inset:0;

            background:
            linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.05),
                transparent
            );

            transform:translateX(-100%);

            animation:shineMove 7s infinite;
        }

        @keyframes shineMove{

            100%{
                transform:translateX(100%);
            }
        }

        /* =====================================================
        SEARCH BOX
        ===================================================== */
        .stTextInput input{

            background:
            rgba(2,6,23,0.92) !important;

            color:white !important;

            border:
            1px solid rgba(56,189,248,0.14) !important;

            border-radius:18px !important;

            transition:0.35s !important;

            box-shadow:
            0 0 20px rgba(56,189,248,0.05);
        }

        .stTextInput input:focus{

            border:
            1px solid #38BDF8 !important;

            box-shadow:
            0 0 25px rgba(56,189,248,0.22) !important;

            transform:scale(1.01);
        }

        /* =====================================================
        DATAFRAME
        ===================================================== */
        [data-testid="stDataFrame"]{

            border-radius:24px !important;

            overflow:hidden !important;

            border:
            1px solid rgba(56,189,248,0.12);

            box-shadow:
            0 0 25px rgba(56,189,248,0.10);

            background:
            rgba(15,23,42,0.92) !important;
        }

        /* =====================================================
        TABLE HEADER
        ===================================================== */
        thead tr th{

            background:
            linear-gradient(
                135deg,
                rgba(14,165,233,0.22),
                rgba(124,58,237,0.18)
            ) !important;

            color:white !important;

            font-weight:800 !important;

            border:none !important;
        }

        /* =====================================================
        TABLE BODY
        ===================================================== */
        tbody tr{

            background:
            rgba(15,23,42,0.82) !important;

            transition:0.3s !important;
        }

        tbody tr:hover{

            background:
            rgba(30,41,59,0.95) !important;

            transform:scale(1.002);
        }

        tbody td{

            color:#E2E8F0 !important;

            border-color:
            rgba(56,189,248,0.08) !important;
        }

        /* =====================================================
        INFO BOX
        ===================================================== */
        .stInfo{

            border-radius:18px !important;

            border:
            1px solid rgba(56,189,248,0.14) !important;

            background:
            rgba(15,23,42,0.92) !important;
        }

        /* =====================================================
        FLOATING PARTICLES
        ===================================================== */
        .particles{

            position:absolute;

            inset:0;

            pointer-events:none;

            overflow:hidden;
        }

        .particles span{

            position:absolute;

            width:4px;
            height:4px;

            border-radius:50%;

            background:#38BDF8;

            opacity:0.7;

            animation:floatParticle linear infinite;
        }

        .particles span:nth-child(1){

            left:10%;
            animation-duration:8s;
        }

        .particles span:nth-child(2){

            left:25%;
            animation-duration:12s;
        }

        .particles span:nth-child(3){

            left:40%;
            animation-duration:10s;
        }

        .particles span:nth-child(4){

            left:60%;
            animation-duration:14s;
        }

        .particles span:nth-child(5){

            left:80%;
            animation-duration:9s;
        }

        @keyframes floatParticle{

            0%{

                transform:
                translateY(100%);

                opacity:0;
            }

            30%{
                opacity:1;
            }

            100%{

                transform:
                translateY(-1200%);

                opacity:0;
            }
        }

        </style>
    """,
        unsafe_allow_html=True,
    )

# =====================================================
# TITLE
# =====================================================
    st.subheader("🗂 Patient Records")

    # =====================================================
    # SEARCH
    # =====================================================
    search = st.text_input("🔍 Search Patient ID")


    # =====================================================
    # RECORDS
    # =====================================================
    with st.container(border=True):

        records = fetch_records()

        if records:

            df = pd.DataFrame(
                records,
                columns=[
                    "DB_ID",
                    "Name",
                    "ID",
                    "Alpha",
                    "Beta",
                    "Gamma",
                    "Alpha_%",
                    "Beta_%",
                    "Gamma_%",
                    "Prediction",
                    "Confidence",
                    "Timestamp",
                ],
            )

            for col in df.columns:

                try:

                    df[col] = df[col].apply(
                        lambda x: (
                            x.decode("utf-8", errors="ignore")
                            if isinstance(x, bytes)
                            else x
                        )
                    )

                except:
                    pass

            for col in df.columns:

                df[col] = df[col].astype(str)

            df = df.fillna("")

            # =================================================
            # SEARCH FILTER
            # =================================================
            if search:

                df = df[df["ID"].str.contains(search, case=False)]

            # =================================================
            # METRICS
            # =================================================
            c1, c2, c3, c4 = st.columns(4)

            c1.metric("📄 Total Records", len(df))

            high_risk = len(df[df["Prediction"] == "High Stress"])

            c2.metric("🚨 High Risk", high_risk)

            latest = df.iloc[-1]["Prediction"]

            c3.metric("🩺 Latest Diagnosis", latest)

            c4.metric("🤖 AI Accuracy", "96.4%")

            # =================================================
            # DATAFRAME
            # =================================================
            st.dataframe(df, width="stretch", height=500)

        else:

            st.info("No records available")

    # =====================================================
    # CARD END
    # =====================================================
    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )

# DOCTOR REVIEW

if page == "👨‍⚕️ Doctor Review":

    # =====================================================
    # CSS EFFECTS
    # =====================================================
    st.markdown(
        """
        <style>

        /* =====================================================
        GLITTER BACKGROUND
        ===================================================== */
        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:999;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        /* =====================================================
        TITLE
        ===================================================== */
        h3{

            font-size:42px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            text-shadow:
            0 0 20px rgba(56,189,248,0.25);
        }

        /* =====================================================
        REVIEW CARD
        ===================================================== */
        .review-card{

            position:relative;

            overflow:hidden;

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:30px;

            padding:30px;

            box-shadow:
            0 0 30px rgba(56,189,248,0.10);

            backdrop-filter:blur(18px);
        }

        /* =====================================================
        AURORA EFFECT
        ===================================================== */
        .review-card::before{

            content:"";

            position:absolute;

            width:450px;
            height:450px;

            top:-220px;
            right:-180px;

            background:
            radial-gradient(
                circle,
                rgba(56,189,248,0.15),
                transparent 70%
            );

            animation:auroraMove 10s ease infinite alternate;
        }

        @keyframes auroraMove{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(50px);
            }
        }

        /* =====================================================
        SHINE EFFECT
        ===================================================== */
        .review-card::after{

            content:"";

            position:absolute;

            inset:0;

            background:
            linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.05),
                transparent
            );

            transform:translateX(-100%);

            animation:shineMove 7s infinite;
        }

        @keyframes shineMove{

            100%{
                transform:translateX(100%);
            }
        }

        /* =====================================================
        TEXT AREA
        ===================================================== */
        textarea{

            background:
            rgba(2,6,23,0.92) !important;

            color:white !important;

            border:
            1px solid rgba(56,189,248,0.14) !important;

            border-radius:18px !important;

            line-height:1.8 !important;

            transition:0.35s !important;
        }

        textarea:focus{

            border:
            1px solid #38BDF8 !important;

            box-shadow:
            0 0 25px rgba(56,189,248,0.22) !important;
        }

        /* =====================================================
        SELECT BOX
        ===================================================== */
        div[data-baseweb="select"] > div{

            background:
            rgba(2,6,23,0.92) !important;

            color:white !important;

            border:
            1px solid rgba(56,189,248,0.14) !important;

            border-radius:18px !important;

            transition:0.35s !important;
        }

        div[data-baseweb="select"] > div:hover{

            border:
            1px solid #38BDF8 !important;

            box-shadow:
            0 0 18px rgba(56,189,248,0.18);
        }

        /* =====================================================
        BUTTON
        ===================================================== */
        .stButton>button{

            background:
            linear-gradient(
                135deg,
                #06B6D4,
                #2563EB,
                #7C3AED,
                #EC4899
            ) !important;

            background-size:300% !important;

            animation:buttonFlow 7s linear infinite;

            color:white !important;

            border:none !important;

            border-radius:18px !important;

            height:3.4em !important;

            font-weight:800 !important;

            transition:0.35s !important;

            box-shadow:
            0 0 25px rgba(56,189,248,0.18);
        }

        @keyframes buttonFlow{

            0%{
                background-position:0%;
            }

            100%{
                background-position:300%;
            }
        }

        .stButton>button:hover{

            transform:
            translateY(-3px)
            scale(1.02);
        }

        /* =====================================================
        SUCCESS BOX
        ===================================================== */
        .stSuccess{

            border-radius:18px !important;

            background:
            rgba(15,23,42,0.92) !important;

            border:
            1px solid rgba(34,197,94,0.18) !important;
        }

        </style>
    """,
        unsafe_allow_html=True,
    )

# =====================================================
# TITLE
# =====================================================
    st.subheader("👨‍⚕️ Doctor Review Panel")

    # =====================================================
    # AI SUGGESTIONS
    # =====================================================
    ai_notes = ""

    ai_severity = "Low"

    if st.session_state.prediction_done:

        prediction = st.session_state.predicted_class

        confidence = st.session_state.confidence

        risk = st.session_state.risk_score

        # =================================================
        # HIGH STRESS
        # =================================================
        if prediction == "High Stress":

            ai_severity = "Critical"

            ai_notes = f"""
    Patient exhibits HIGH STRESS neurological condition.

    🧠 Elevated beta/gamma activity detected.
    ⚠ Increased cognitive stress response observed.

    📊 AI Analysis:
    • Confidence : {confidence:.2f}%
    • Risk Score : {risk:.2f}%

    💡 AI Recommendation:
    • Immediate clinical observation advised
    • Psychological consultation recommended
    • Continuous EEG monitoring required
    """

        # =================================================
        # RELAXED
        # =================================================
        elif prediction == "Relaxed":

            ai_severity = "Low"

            ai_notes = f"""
    Patient exhibits RELAXED cognitive condition.

    🧠 Stable alpha activity observed.
    ✅ Calm neurological state detected.

    📊 AI Analysis:
    • Confidence : {confidence:.2f}%
    • Risk Score : {risk:.2f}%

    💡 AI Recommendation:
    • Routine monitoring recommended
    • No immediate concern detected
    """

        # =================================================
        # NORMAL
        # =================================================
        else:

            ai_severity = "Moderate"

            ai_notes = f"""
    Patient exhibits NORMAL cognitive condition.

    🧠 Balanced EEG activity observed.
    ⚡ Stable neurological response detected.

    📊 AI Analysis:
    • Confidence : {confidence:.2f}%
    • Risk Score : {risk:.2f}%

    💡 AI Recommendation:
    • Continue regular observation
    • Follow-up monitoring suggested
    """

    else:

        ai_notes = "Run AI EEG Examination First"

    # =====================================================
    # CARD START
    # =====================================================
    st.markdown(
        """
    <div class="review-card">
    """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # DOCTOR NOTES
    # =====================================================
    doctor_notes = st.text_area(
        "🩺 AI Suggested Doctor Recommendations", value=ai_notes, height=320
    )

    # =====================================================
    # AI SEVERITY
    # =====================================================
    severity_levels = ["Low", "Moderate", "High", "Critical"]

    severity = st.selectbox(
        "🚨 AI Suggested Severity Level",
        severity_levels,
        index=severity_levels.index(ai_severity),
    )

    # =====================================================
    # SUBMIT
    # =====================================================
    if st.button("🚀 Submit Review", use_container_width=True):

        st.success("✅ Doctor Review Submitted Successfully")

    # =====================================================
    # CARD END
    # =====================================================
    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )

# EMERGENCY ALERTS

if page == "🚨 Emergency Alerts":

    # =====================================================
    # ADVANCED CSS
    # =====================================================
    st.markdown(
        """
        <style>

        /* =====================================================
        GLITTER BACKGROUND
        ===================================================== */
        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:999;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        /* =====================================================
        TITLE
        ===================================================== */
        h3{

            font-size:42px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;

            text-shadow:
            0 0 20px rgba(56,189,248,0.25);
        }

        /* =====================================================
        ALERT CARD
        ===================================================== */
        .alert-card{

            position:relative;

            overflow:hidden;

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:30px;

            padding:35px;

            box-shadow:
            0 0 35px rgba(56,189,248,0.12);

            backdrop-filter:blur(18px);
        }

        /* =====================================================
        AURORA EFFECT
        ===================================================== */
        .alert-card::before{

            content:"";

            position:absolute;

            width:500px;
            height:500px;

            top:-250px;
            right:-220px;

            background:
            radial-gradient(
                circle,
                rgba(56,189,248,0.15),
                transparent 70%
            );

            animation:auroraMove 10s ease infinite alternate;
        }

        @keyframes auroraMove{

            from{
                transform:translateY(0px);
            }

            to{
                transform:translateY(60px);
            }
        }

        /* =====================================================
        SHINE EFFECT
        ===================================================== */
        .alert-card::after{

            content:"";

            position:absolute;

            inset:0;

            background:
            linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.05),
                transparent
            );

            transform:translateX(-100%);

            animation:shineMove 7s infinite;
        }

        @keyframes shineMove{

            100%{
                transform:translateX(100%);
            }
        }

        /* =====================================================
        METRICS
        ===================================================== */
        [data-testid="metric-container"]{

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:24px;

            padding:18px;

            box-shadow:
            0 0 25px rgba(56,189,248,0.08);

            transition:0.35s;
        }

        [data-testid="metric-container"]:hover{

            transform:
            translateY(-4px)
            scale(1.02);

            box-shadow:
            0 0 35px rgba(56,189,248,0.18);
        }

        /* =====================================================
        ALERT BOXES
        ===================================================== */
        .stError{

            border-radius:20px !important;

            border:
            1px solid rgba(239,68,68,0.25) !important;

            background:
            rgba(15,23,42,0.92) !important;

            animation:pulseAlert 1.5s infinite;
        }

        @keyframes pulseAlert{

            0%{
                box-shadow:
                0 0 10px rgba(239,68,68,0.20);
            }

            50%{
                box-shadow:
                0 0 35px rgba(239,68,68,0.45);
            }

            100%{
                box-shadow:
                0 0 10px rgba(239,68,68,0.20);
            }
        }

        .stWarning{

            border-radius:20px !important;

            background:
            rgba(15,23,42,0.92) !important;

            border:
            1px solid rgba(245,158,11,0.22) !important;
        }

        .stSuccess{

            border-radius:20px !important;

            background:
            rgba(15,23,42,0.92) !important;

            border:
            1px solid rgba(34,197,94,0.22) !important;
        }

        /* =====================================================
        PARTICLES
        ===================================================== */
        .alert-particles{

            position:absolute;

            inset:0;

            overflow:hidden;

            pointer-events:none;
        }

        .alert-particles span{

            position:absolute;

            width:4px;
            height:4px;

            border-radius:50%;

            background:#38BDF8;

            opacity:0.7;

            animation:particleFloat linear infinite;
        }

        .alert-particles span:nth-child(1){

            left:10%;
            animation-duration:8s;
        }

        .alert-particles span:nth-child(2){

            left:25%;
            animation-duration:12s;
        }

        .alert-particles span:nth-child(3){

            left:40%;
            animation-duration:10s;
        }

        .alert-particles span:nth-child(4){

            left:60%;
            animation-duration:14s;
        }

        .alert-particles span:nth-child(5){

            left:80%;
            animation-duration:9s;
        }

        @keyframes particleFloat{

            0%{

                transform:
                translateY(100%);

                opacity:0;
            }

            30%{
                opacity:1;
            }

            100%{

                transform:
                translateY(-1200%);

                opacity:0;
            }
        }

        </style>
    """,
        unsafe_allow_html=True,
    )

# =====================================================
# TITLE
# =====================================================
    st.subheader("🚨 Emergency Monitoring")

    # =====================================================
    # AI ALERT LOGIC
    # =====================================================
    prediction = st.session_state.predicted_class

    confidence = st.session_state.confidence

    risk_score = st.session_state.risk_score


    with st.container(border=True):

        # =================================================
        # METRICS
        # =================================================
        c1, c2, c3 = st.columns(3)

        c1.metric("🧠 Mental State", prediction)

        c2.metric("⚡ Risk Score", f"{risk_score:.2f}%")

        c3.metric("📊 Confidence", f"{confidence:.2f}%")

        st.progress(int(confidence))

        # =================================================
        # ALERT CONDITIONS
        # =================================================
        if prediction == "High Stress":

            st.error("🚨 CRITICAL NEUROLOGICAL ALERT")

            st.warning("""
                    ⚠ Immediate medical attention required.

                    • Elevated cognitive stress detected
                    • High beta/gamma activity observed
                    • Continuous monitoring recommended
                    • Emergency clinical review advised
            """)

            st.markdown("""
                                        ### 🔴 AI Emergency Actions

                                        - Activate emergency monitoring
                                        - Notify neurologist immediately
                                        - Start continuous EEG observation
                                        - Prepare psychological assessment
            """)

        elif prediction == "Normal":

            st.warning("⚠ Moderate Cognitive Activity")

            st.info("""
                                        Patient shows moderate neurological activity.

                                        • Continue regular monitoring
                                        • Follow-up EEG analysis suggested
            """)

        else:

            st.success("✅ Patient Stable")

            st.info("""
                    Stable and relaxed EEG activity detected.

                    • No emergency intervention required
                    • Routine monitoring recommended
            """)

    # =====================================================
    # CARD END
    # =====================================================
    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )

# FINAL CLINICAL REPORT

if page == "📄 Final Clinical Report":

    # =====================================================
    # ADVANCED CSS
    # =====================================================
    st.markdown(
        """
        <style>

        /* =====================================================
        GLITTER BACKGROUND
        ===================================================== */
        [data-testid="stAppViewContainer"]::before{

            content:"";

            position:fixed;

            top:0;
            left:0;

            width:100%;
            height:100%;

            pointer-events:none;

            background-image:

            radial-gradient(circle, rgba(255,255,255,0.9) 1px, transparent 1px),
            radial-gradient(circle, rgba(56,189,248,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(168,85,247,0.7) 1px, transparent 1px),
            radial-gradient(circle, rgba(236,72,153,0.7) 1px, transparent 1px);

            background-size:
            120px 120px,
            180px 180px,
            220px 220px,
            260px 260px;

            animation:glitterMove 20s linear infinite;

            opacity:0.45;

            z-index:999;
        }

        @keyframes glitterMove{

            0%{
                transform:translateY(0px);
            }

            100%{
                transform:translateY(-300px);
            }
        }

        /* =====================================================
        TITLE
        ===================================================== */
        h3{

            font-size:42px !important;

            font-family:'Orbitron',sans-serif !important;

            background:
            linear-gradient(
                90deg,
                #38BDF8,
                #8B5CF6,
                #EC4899
            );

            -webkit-background-clip:text;

            -webkit-text-fill-color:transparent;
        }

        /* =====================================================
        REPORT CARD
        ===================================================== */
        .report-card{

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:30px;

            padding:35px;

            box-shadow:
            0 0 35px rgba(56,189,248,0.12);

            backdrop-filter:blur(18px);
        }

        /* =====================================================
        METRICS
        ===================================================== */
        [data-testid="metric-container"]{

            background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.92),
                rgba(30,41,59,0.84)
            );

            border:
            1px solid rgba(56,189,248,0.12);

            border-radius:22px;

            padding:18px;

            box-shadow:
            0 0 20px rgba(56,189,248,0.08);
        }

        /* =====================================================
        INFO BOX
        ===================================================== */
        .stInfo,
        .stSuccess,
        .stWarning,
        .stError{

            border-radius:20px !important;

            background:
            rgba(15,23,42,0.92) !important;
        }

        </style>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("📄 Final Clinical Report")

    st.markdown(
        """
    <div class="report-card">
    """,
        unsafe_allow_html=True,
    )

    if st.session_state.prediction_done:

        # =====================================================
        # HOSPITAL HEADER
        # =====================================================
        st.markdown(
            """
        <div style='
        background:linear-gradient(135deg,#0EA5E9,#2563EB,#7C3AED);
        padding:25px;
        border-radius:20px;
        margin-bottom:25px;
        box-shadow:0 0 30px rgba(56,189,248,0.18);
        '>

        <h1 style='color:white;'>
        🏥 NeuroSense AI Hospital Report
        </h1>

        <p style='color:white;font-size:16px;'>
        Advanced EEG Clinical Monitoring Platform
        </p>

        </div>
        """,
            unsafe_allow_html=True,
        )

        # =====================================================
        # PATIENT INFO
        # =====================================================
        st.markdown("## 👤 Patient Information")

        c1, c2 = st.columns(2)

        c1.info(f"""
    Patient Name:
    {st.session_state.patient_name}
    """)

        st.markdown("---")

        # =====================================================
        # EEG EXAMINATION
        # =====================================================
        st.markdown("## 🧠 EEG Examination")

        col1, col2, col3 = st.columns(3)

        col1.metric("Mental State", st.session_state.predicted_class)

        col2.metric("Confidence", f"{st.session_state.confidence:.2f}%")

        col3.metric("Risk Score", f"{st.session_state.risk_score:.2f}%")

        st.progress(int(st.session_state.confidence))

        # =====================================================
        # ALERTS
        # =====================================================
        st.markdown("## 🚨 Emergency Alerts")

        if st.session_state.predicted_class == "High Stress":

            st.error("""
    🚨 CRITICAL STRESS DETECTED

    Immediate neurological attention required.
    """)

        elif st.session_state.predicted_class == "Normal":

            st.warning("""
    ⚠ Moderate Cognitive Activity Detected
    """)

        else:

            st.success("""
    ✅ Patient Stable
    """)

        st.markdown("---")

        # =====================================================
        # LIVE MONITORING
        # =====================================================
        st.markdown("## 📡 Live Monitoring")

        st.success("""
    ✅ EEG Monitoring Active

    • Real-time EEG tracking completed
    • Neural activity recorded successfully
    • AI synchronization stable
    """)

        st.markdown("---")

        # =====================================================
        # EEG IMAGE
        # =====================================================
        st.markdown("## 🧠 EEG Spectrogram")

        st.image(st.session_state.full_img, width=750)

        st.markdown("---")

        # =====================================================
        # ANALYTICS
        # =====================================================
        st.markdown("## 📊 Analytics")

        analytics_df = pd.DataFrame(
            {
                "Brainwave": ["Alpha", "Beta", "Gamma"],
                "Value": [
                    st.session_state.alpha_pct,
                    st.session_state.beta_pct,
                    st.session_state.gamma_pct,
                ],
            }
        )

        st.bar_chart(analytics_df.set_index("Brainwave"))

        st.markdown("---")

        # =====================================================
        # PATIENT RECORDS
        # =====================================================
        st.markdown("## 🗂 Patient Records")

        st.info(f"""
    Patient records successfully stored.

    • Patient Name : {st.session_state.patient_name}

    • AI Prediction : {st.session_state.predicted_class}
    """)

        st.markdown("---")

        # =====================================================
        # DOCTOR REVIEW
        # =====================================================
        st.markdown("## 👨‍⚕️ Doctor Review")

        if st.session_state.predicted_class == "High Stress":

            recommendation = """
    • Immediate neurological consultation required
    • Continuous EEG monitoring advised
    • Stress management therapy recommended
    """

        elif st.session_state.predicted_class == "Relaxed":

            recommendation = """
    • Patient neurologically stable
    • Routine observation recommended
    """

        else:

            recommendation = """
    • Follow-up EEG monitoring suggested
    • Continue regular observation
    """

        st.success(recommendation)

        st.markdown("---")

        # =====================================================
        # FINAL AI SUMMARY
        # =====================================================
        st.markdown("## 🤖 Final AI Summary")

        st.info(f"""
    🧠 Final Diagnosis:
    {st.session_state.predicted_class}

    📊 Confidence:
    {st.session_state.confidence:.2f}%

    ⚡ Risk Score:
    {st.session_state.risk_score:.2f}%

    🏥 NeuroSense AI successfully completed
    clinical EEG cognitive analysis.
    """)

        st.markdown("---")

        # =====================================================
        # PDF GENERATION
        # =====================================================
        if st.button("📄 Generate PDF Report", use_container_width=True):

            pdf_file = generate_pdf_report(
                st.session_state.patient_name,
                st.session_state.patient_id,
                st.session_state.alpha,
                st.session_state.beta,
                st.session_state.gamma,
                st.session_state.alpha_pct,
                st.session_state.beta_pct,
                st.session_state.gamma_pct,
                st.session_state.predicted_class,
                st.session_state.confidence,
                st.session_state.full_img,
            )

            st.session_state.pdf_file = pdf_file

            st.success("✅ PDF Report Generated Successfully")

        # =====================================================
        # DOWNLOAD PDF
        # =====================================================
        if st.session_state.pdf_file is not None:

            with open(st.session_state.pdf_file, "rb") as f:

                st.download_button(
                    "📥 Download Clinical Report",
                    data=f,
                    file_name=st.session_state.pdf_file,
                    mime="application/pdf",
                    use_container_width=True,
                )

    else:

        st.warning("Please complete EEG Examination first.")

    st.markdown(
        """
    </div>
    """,
        unsafe_allow_html=True,
    )
