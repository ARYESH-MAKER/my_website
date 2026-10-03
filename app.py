import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CLARIX - Gaming Hub",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "selected_game" not in st.session_state:
    st.session_state.selected_game = None

if "dashboard_navigation" not in st.session_state:
    st.session_state.dashboard_navigation = None


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@400;500;600;700&display=swap'
);


/* ============================================================
   GLOBAL
   ============================================================ */

html, body, [class*="css"] {
    font-family: "Rajdhani", sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(0, 85, 170, 0.16),
            transparent 35%
        ),
        linear-gradient(
            180deg,
            #020711 0%,
            #040a14 45%,
            #02050b 100%
        );

    color: white;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   STREAMLIT HEADER
   ============================================================ */

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    visibility: hidden !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #030914 0%,
            #050b17 55%,
            #02060d 100%
        ) !important;

    border-right: 1px solid rgba(0, 140, 255, 0.35);
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
}

.sidebar-logo {
    font-family: "Orbitron", sans-serif;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 5px;
    color: white;
    text-align: center;

    text-shadow:
        0 0 5px #ffffff,
        0 0 12px #008cff,
        0 0 25px #006eff,
        0 0 45px rgba(0, 110, 255, 0.8);

    margin-top: 10px;
    margin-bottom: 2px;
}

.sidebar-subtitle {
    font-family: "Orbitron", sans-serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #55c7ff;
    text-align: center;

    text-shadow:
        0 0 8px rgba(0, 150, 255, 0.65);

    margin-bottom: 20px;
}

[data-testid="stSidebar"] label {
    font-family: "Orbitron", sans-serif !important;
    color: white !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    font-family: "Rajdhani", sans-serif !important;
    color: #dcecff !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    color: #55c7ff !important;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(0, 140, 255, 0.25) !important;
}


/* ============================================================
   SIDEBAR COLLAPSE BUTTON
   ============================================================ */

[data-testid="stSidebarCollapseButton"] {
    z-index: 9999 !important;
}

[data-testid="stSidebarCollapseButton"] button {
    color: #ffffff !important;
    background-color: #075fc7 !important;
    border: 2px solid #55c7ff !important;
    border-radius: 8px !important;

    width: 36px !important;
    height: 36px !important;

    box-shadow:
        0 0 8px rgba(0, 140, 255, 0.7),
        0 0 18px rgba(0, 140, 255, 0.35) !important;
}

[data-testid="stSidebarCollapseButton"] button svg {
    color: #ffffff !important;
    fill: #ffffff !important;
    stroke: #ffffff !important;

    width: 20px !important;
    height: 20px !important;
}

[data-testid="stSidebarCollapseButton"] button:hover {
    color: #ffffff !important;
    background-color: #0877e8 !important;
    border-color: #ffffff !important;

    box-shadow:
        0 0 10px rgba(85, 199, 255, 0.9),
        0 0 24px rgba(0, 140, 255, 0.6) !important;
}

[data-testid="stSidebarCollapseButton"] button:hover svg {
    color: #ffffff !important;
    fill: #ffffff !important;
    stroke: #ffffff !important;
}


/* ============================================================
   SIDEBAR CATEGORY SELECTBOX
   ============================================================ */

[data-testid="stSidebar"] [data-testid="stSelectbox"] label {
    color: white !important;
    font-family: "Orbitron", sans-serif !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #08101f !important;
    border: 1px solid #008cff !important;
    border-radius: 8px !important;
    min-height: 42px !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] [role="button"] {
    background-color: #08101f !important;
    color: #55c7ff !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] [role="button"] span {
    color: #55c7ff !important;
    -webkit-text-fill-color: #55c7ff !important;
    font-family: "Rajdhani", sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] svg {
    fill: #55c7ff !important;
    color: #55c7ff !important;
}

[data-baseweb="popover"] {
    background-color: #080f1d !important;
    border: 1px solid #008cff !important;
}

[data-baseweb="popover"] [role="option"] {
    background-color: #080f1d !important;
    color: #dcecff !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 16px !important;
}

[data-baseweb="popover"] [role="option"]:hover {
    background-color: #073b6d !important;
    color: #55c7ff !important;
}

[data-baseweb="popover"] [role="option"][aria-selected="true"] {
    background-color: #064c9b !important;
    color: white !important;
}


/* ============================================================
   MAIN CLARIX LOGO
   ============================================================ */

.clarix-logo {
    font-family: "Orbitron", sans-serif;
    font-size: 72px;
    font-weight: 900;
    letter-spacing: 9px;
    color: white;

    text-shadow:
        0 0 4px #ffffff,
        0 0 10px #008cff,
        0 0 20px #008cff,
        0 0 40px #006eff,
        0 0 75px rgba(0, 110, 255, 0.85);

    margin-bottom: 0;
    line-height: 1.1;
    text-align: center;
}

.clarix-tagline {
    text-align: center;
    color: #8fa9c4;

    font-family: "Rajdhani", sans-serif;
    font-size: 19px;
    font-weight: 600;
    letter-spacing: 4px;

    margin-top: 8px;
}

.gaming-247 {
    text-align: center;
    color: #55c7ff;

    font-family: "Orbitron", sans-serif;
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 5px;

    margin-top: 15px;

    text-shadow:
        0 0 7px #008cff,
        0 0 18px rgba(0, 140, 255, 0.6);
}


/* ============================================================
   STATS
   ============================================================ */

.stat-box {
    background:
        linear-gradient(
            145deg,
            rgba(8, 22, 42, 0.95),
            rgba(3, 9, 18, 0.95)
        );

    border: 1px solid rgba(0, 140, 255, 0.35);
    border-radius: 10px;

    padding: 18px 10px;
    text-align: center;

    box-shadow:
        inset 0 0 20px rgba(0, 100, 255, 0.04),
        0 0 12px rgba(0, 80, 180, 0.10);
}

.stat-number {
    color: #55c7ff;

    font-family: "Orbitron", sans-serif;
    font-size: 22px;
    font-weight: 900;

    text-shadow:
        0 0 8px #008cff;
}

.stat-label {
    color: #91a9c4;

    font-family: "Rajdhani", sans-serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;

    margin-top: 5px;
}


/* ============================================================
   DASHBOARD
   ============================================================ */

.home-dashboard-title {
    color: #c77dff !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 32px !important;
    font-weight: 900 !important;
    letter-spacing: 4px;

    text-shadow:
        0 0 8px rgba(199, 125, 255, 0.9),
        0 0 20px rgba(140, 70, 255, 0.55);

    margin-top: 35px;
    margin-bottom: 8px;
}

.home-dashboard-intro {
    color: #91a9c4 !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 17px !important;
    letter-spacing: 1px;

    margin-bottom: 25px;
}

.home-section-title {
    font-family: "Orbitron", sans-serif !important;
    font-size: 23px !important;
    font-weight: 900 !important;
    letter-spacing: 2px !important;

    margin-top: 8px;
    margin-bottom: 8px;
}

.section-yellow {
    color: #ffcc66 !important;

    text-shadow:
        0 0 7px #ffcc66,
        0 0 18px rgba(255, 180, 50, 0.65) !important;
}

.section-pink {
    color: #ff4fd8 !important;

    text-shadow:
        0 0 7px #ff4fd8,
        0 0 18px rgba(255, 0, 180, 0.65) !important;
}

.section-orange {
    color: #ff9d42 !important;

    text-shadow:
        0 0 7px #ff9d42,
        0 0 18px rgba(255, 100, 20, 0.65) !important;
}

.section-green {
    color: #66ffcc !important;

    text-shadow:
        0 0 7px #66ffcc,
        0 0 18px rgba(0, 255, 180, 0.65) !important;
}


/* ============================================================
   COMMAND CENTER
   ============================================================ */

.clarix-command-center {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;

    color: #c77dff !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 22px !important;
    font-weight: 800 !important;
    letter-spacing: 2px !important;

    text-shadow:
        0 0 7px #c77dff,
        0 0 18px rgba(199, 125, 255, 0.75) !important;

    margin-top: 30px !important;
    margin-bottom: 14px !important;
}

.home-command-text {
    color: #55c7ff !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 2px;

    text-shadow:
        0 0 7px rgba(0, 150, 255, 0.55);
}


/* ============================================================
   DASHBOARD CARDS
   ============================================================ */

.dashboard-card {
    background:
        linear-gradient(
            145deg,
            rgba(7, 17, 31, 0.98),
            rgba(3, 8, 16, 0.98)
        );

    border: 1px solid rgba(0, 130, 255, 0.28);
    border-radius: 10px;

    padding: 17px;
    margin-bottom: 18px;

    box-shadow:
        inset 0 0 25px rgba(0, 80, 180, 0.03),
        0 0 15px rgba(0, 60, 150, 0.08);
}

.dashboard-card p {
    color: #9aadc2 !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 16px !important;
}


/* ============================================================
   BLUE BUTTONS
   ============================================================ */

.stButton > button {
    width: 100%;

    background:
        linear-gradient(
            90deg,
            #064c9b,
            #075fc7
        ) !important;

    color: white !important;

    border: 1px solid #008cff !important;
    border-radius: 8px !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
}

.stButton > button:hover {
    background:
        linear-gradient(
            90deg,
            #0877e8,
            #006eff
        ) !important;

    color: white !important;
    border-color: #55c7ff !important;

    box-shadow:
        0 0 16px rgba(0, 140, 255, 0.40) !important;
}

.stButton > button:focus,
.stButton > button:active {
    color: white !important;

    background:
        linear-gradient(
            90deg,
            #075fc7,
            #064c9b
        ) !important;

    border-color: #55c7ff !important;
}


/* ============================================================
   LINK BUTTONS
   ============================================================ */

[data-testid="stLinkButton"] a {
    width: 100%;

    background:
        linear-gradient(
            90deg,
            #064c9b,
            #075fc7
        ) !important;

    color: white !important;

    border: 1px solid #008cff !important;
    border-radius: 8px !important;

    font-family: "Orbitron", sans-serif !important;
    font-weight: 700 !important;

    text-decoration: none !important;
}

[data-testid="stLinkButton"] a:hover {
    background:
        linear-gradient(
            90deg,
            #0877e8,
            #006eff
        ) !important;

    color: white !important;
    border-color: #55c7ff !important;

    box-shadow:
        0 0 18px rgba(0, 140, 255, 0.40) !important;
}

[data-testid="stLinkButton"] a:visited {
    color: white !important;
}


/* ============================================================
   QUICK ACCESS GAME NAMES
   ============================================================ */

.quick-game-name {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 18px !important;
    font-weight: 900 !important;
    letter-spacing: 1px !important;

    margin-bottom: 6px !important;
}

.quick-minecraft {
    color: #66ffcc !important;

    text-shadow:
        0 0 7px #66ffcc,
        0 0 15px rgba(102, 255, 204, 0.65) !important;
}

.quick-fortnite {
    color: #ff4fd8 !important;

    text-shadow:
        0 0 7px #ff4fd8,
        0 0 15px rgba(255, 79, 216, 0.65) !important;
}

.quick-gta {
    color: #ff9d42 !important;

    text-shadow:
        0 0 7px #ff9d42,
        0 0 15px rgba(255, 157, 66, 0.65) !important;
}


/* ============================================================
   SEARCH BAR
   ============================================================ */

.stTextInput input {
    background-color: #080e1d !important;
    color: white !important;

    border: 1px solid #075fc7 !important;
    border-radius: 8px !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 17px !important;

    caret-color: #55c7ff !important;
}

.stTextInput input::placeholder {
    color: #9da9b8 !important;
    opacity: 1 !important;
}

.stTextInput input:focus {
    border-color: #00aaff !important;

    box-shadow:
        0 0 0 1px #00aaff !important;
}

.stTextInput label {
    color: white !important;

    font-family: "Orbitron", sans-serif !important;
    font-weight: 600 !important;
}


/* ============================================================
   GAME GENRE
   ============================================================ */

.game-genre {
    display: inline-block !important;

    color: #55c7ff !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;

    background: rgba(0, 130, 255, 0.10) !important;

    border: 1px solid rgba(0, 150, 255, 0.45) !important;
    border-radius: 5px !important;

    padding: 4px 11px !important;
    margin-bottom: 13px !important;
}


/* ============================================================
   PAGE TITLES
   ============================================================ */

.page-title-games {
    color: #ffcc66 !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 32px !important;
    font-weight: 900 !important;
    letter-spacing: 3px;

    text-shadow:
        0 0 8px rgba(255, 204, 102, 0.8),
        0 0 20px rgba(255, 160, 50, 0.45);
}

.page-title-leaderboard {
    color: #ff4fd8 !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 32px !important;
    font-weight: 900 !important;
    letter-spacing: 3px;

    text-shadow:
        0 0 8px rgba(255, 79, 216, 0.85),
        0 0 22px rgba(255, 0, 180, 0.45);
}

.page-title-news {
    color: #ff9d42 !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 32px !important;
    font-weight: 900 !important;
    letter-spacing: 3px;

    text-shadow:
        0 0 8px rgba(255, 157, 66, 0.85),
        0 0 22px rgba(255, 100, 20, 0.45);
}

.page-title-profiles {
    color: #b86cff !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 32px !important;
    font-weight: 900 !important;
    letter-spacing: 3px;

    text-shadow:
        0 0 8px rgba(184, 108, 255, 0.85),
        0 0 22px rgba(130, 50, 255, 0.45);
}


/* ============================================================
   GAME CARDS
   ============================================================ */

.game-card {
    background:
        linear-gradient(
            145deg,
            rgba(7, 18, 33, 0.98),
            rgba(3, 8, 16, 0.98)
        );

    border: 1px solid rgba(0, 140, 255, 0.35);
    border-radius: 10px;

    padding: 20px;
    margin-bottom: 18px;

    box-shadow:
        0 0 16px rgba(0, 90, 180, 0.08);
}

.game-card-title {
    color: white !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 24px !important;
    font-weight: 900 !important;
    letter-spacing: 1px !important;

    margin-bottom: 5px;
}

.game-card-description {
    color: #9aadc2 !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 16px !important;
    line-height: 1.5;
}

.detail-label {
    color: #55c7ff !important;

    font-family: "Orbitron", sans-serif !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
}

.detail-value {
    color: white !important;

    font-family: "Rajdhani", sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}


/* ============================================================
   LEADERBOARD
   ============================================================ */

.leader-row {
    background:
        linear-gradient(
            90deg,
            rgba(10, 19, 35, 0.95),
            rgba(4, 10, 19, 0.95)
        );

    border: 1px solid rgba(255, 79, 216, 0.20);
    border-radius: 8px;

    padding: 13px 18px;
    margin-bottom: 8px;
}

.leader-rank {
    color: #ff4fd8;

    font-family: "Orbitron", sans-serif;
    font-size: 18px;
    font-weight: 900;
}

.leader-name {
    color: white;

    font-family: "Rajdhani", sans-serif;
    font-size: 18px;
    font-weight: 700;
}


/* ============================================================
   NEWS
   ============================================================ */

.news-card {
    background:
        linear-gradient(
            145deg,
            rgba(20, 15, 8, 0.98),
            rgba(8, 8, 7, 0.98)
        );

    border: 1px solid rgba(255, 157, 66, 0.35);
    border-radius: 10px;

    padding: 20px;
    margin-bottom: 18px;
}

.news-game {
    color: #ff9d42;

    font-family: "Orbitron", sans-serif;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
}

.news-title {
    color: white;

    font-family: "Orbitron", sans-serif;
    font-size: 20px;
    font-weight: 800;

    margin-top: 7px;
}

.news-date {
    color: #9da9b8;

    font-family: "Rajdhani", sans-serif;
    font-size: 14px;

    margin-top: 5px;
}

.news-description {
    color: #b4bfcc;

    font-family: "Rajdhani", sans-serif;
    font-size: 16px;
    line-height: 1.5;

    margin-top: 10px;
}


/* ============================================================
   PROFILE
   ============================================================ */

.profile-card {
    background:
        linear-gradient(
            145deg,
            rgba(14, 8, 25, 0.98),
            rgba(5, 6, 13, 0.98)
        );

    border: 1px solid rgba(184, 108, 255, 0.30);
    border-radius: 10px;

    padding: 22px;
    margin-bottom: 18px;
}

.profile-name {
    color: #b86cff;

    font-family: "Orbitron", sans-serif;
    font-size: 22px;
    font-weight: 900;

    text-shadow:
        0 0 10px rgba(184, 108, 255, 0.65);
}

.profile-info {
    color: #aab8c8;

    font-family: "Rajdhani", sans-serif;
    font-size: 16px;

    margin-top: 8px;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border-color: rgba(0, 140, 255, 0.20) !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# GAME DATA
# ============================================================

games = [
    {
        "name": "Minecraft",
        "genre": "Sandbox / Adventure",
        "developer": "Mojang Studios",
        "release": "2011",
        "players": "Single-player & Multiplayer",
        "platforms": "PC / Xbox / PlayStation / Switch / Mobile",
        "description": (
            "Minecraft is a sandbox game focused on exploration, "
            "building, crafting and survival in procedurally generated worlds."
        ),
        "features": [
            "Creative Mode",
            "Survival Mode",
            "Multiplayer",
            "Building & Crafting",
            "Procedurally Generated Worlds"
        ],
        "official": "https://www.minecraft.net/"
    },
    {
        "name": "Fortnite",
        "genre": "Battle Royale / Action",
        "developer": "Epic Games",
        "release": "2017",
        "players": "Online Multiplayer",
        "platforms": "PC / PlayStation / Xbox / Switch / Supported Mobile",
        "description": (
            "Fortnite is an online gaming platform featuring "
            "Battle Royale and a wide range of creator experiences."
        ),
        "features": [
            "Battle Royale",
            "Ranked Play",
            "Creative Experiences",
            "Cross-platform Multiplayer",
            "Live Events"
        ],
        "official": "https://www.fortnite.com/"
    },
    {
        "name": "Grand Theft Auto V",
        "genre": "Action / Open World",
        "developer": "Rockstar Games",
        "release": "2013",
        "players": "Single-player & GTA Online",
        "platforms": "PC / PlayStation / Xbox",
        "description": (
            "Grand Theft Auto V takes place across Los Santos and "
            "Blaine County, following three protagonists alongside GTA Online."
        ),
        "features": [
            "Large Open World",
            "Story Mode",
            "Three Playable Protagonists",
            "GTA Online",
            "Vehicles & Activities"
        ],
        "official": "https://www.rockstargames.com/gta-v"
    }
]


# ============================================================
# LEADERBOARD DATA
# ============================================================

leaderboard = [
    ("1", "FadingLyfe"),
    ("2", "ᴮᴼᴳPookie Poke"),
    ("3", "道化師 PiELo あすらん"),
    ("4", "Crackedv2x ttv"),
    ("5", "まつくんYouTubeいろっぴー"),
    ("6", "Panda_19cm_"),
    ("7", "buttermilk143"),
    ("8", "KiLLeR_VaLDee"),
    ("9", "ITALYANОS"),
    ("10", "iJerra.TV")
]


# ============================================================
# NEWS DATA
# ============================================================

news = [
    {
        "game": "Minecraft",
        "title": "Minecraft Live September 2026",
        "date": "September 2026",
        "description": (
            "News and announcements covering upcoming Minecraft "
            "projects and new content."
        ),
        "url": "https://www.minecraft.net/en-us/"
    },
    {
        "game": "Fortnite",
        "title": "Fortnitemares 2026",
        "date": "October 2026",
        "description": (
            "Seasonal Halloween content and activities arriving in Fortnite."
        ),
        "url": (
            "https://www.fortnite.com/news/"
            "the-corruption-spreads-in-fortnitemares-2026"
        )
    },
    {
        "game": "GTA Online",
        "title": "Halloween Activities in GTA Online",
        "date": "October 2026",
        "description": (
            "Halloween activities and seasonal updates for GTA Online."
        ),
        "url": "https://www.rockstargames.com/newswire"
    }
]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">CLARIX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">GAMING HUB</div>',
        unsafe_allow_html=True
    )

    page_name = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "🎮 Games",
            "🏆 Leaderboard",
            "📰 Gaming News",
            "👤 Player Profiles"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    genre_filter = st.selectbox(
        "GAME CATEGORY",
        [
            "All",
            "Sandbox / Adventure",
            "Battle Royale / Action",
            "Action / Open World"
        ]
    )


# ============================================================
# CURRENT PAGE
# ============================================================

page = page_name


# ============================================================
# GAME DETAIL FUNCTION
# ============================================================

def display_game_details(game):

    st.markdown(
        f'<div class="game-card-title">{game["name"].upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="game-genre">{game["genre"]}</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div>
                <div class="detail-label">DEVELOPER</div>
                <div class="detail-value">{game["developer"]}</div>
            </div>

            <br>

            <div>
                <div class="detail-label">RELEASE</div>
                <div class="detail-value">{game["release"]}</div>
            </div>

            <br>

            <div>
                <div class="detail-label">PLAYERS</div>
                <div class="detail-value">{game["players"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div>
                <div class="detail-label">PLATFORMS</div>
                <div class="detail-value">{game["platforms"]}</div>
            </div>

            <br>

            <div>
                <div class="detail-label">FEATURES</div>
                <div class="detail-value">
                    {" • ".join(game["features"])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "VISIT OFFICIAL WEBSITE",
        game["official"],
        use_container_width=True
    )


# ============================================================
# HOME PAGE
# ============================================================

def show_home():

    st.markdown(
        '<div class="clarix-logo">CLARIX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="clarix-tagline">'
        'THE ULTIMATE GAMING HUB'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="gaming-247">GAMING 24 / 7</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # STATS
    # --------------------------------------------------------

    stat1, stat2, stat3, stat4 = st.columns(4)

    with stat1:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-number">3</div>
                <div class="stat-label">FEATURED GAMES</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with stat2:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-number">REAL</div>
                <div class="stat-label">GAME DATA</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with stat3:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-number">LIVE</div>
                <div class="stat-label">GAMING NEWS</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with stat4:
        st.markdown(
            """
            <div class="stat-box">
                <div class="stat-number">24 / 7</div>
                <div class="stat-label">GAMING HUB</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-dashboard-title">'
        'GAMING DASHBOARD'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-dashboard-intro">'
        'Your central command center for gaming, competition, '
        'news and player discovery.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # GAME LIBRARY
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-title section-yellow">'
        'GAME LIBRARY'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="dashboard-card">
            <p>
                Explore featured games, discover their details,
                platforms, genres and gameplay features.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "EXPLORE GAMES",
        key="dashboard_games",
        use_container_width=True
    ):
        st.session_state.dashboard_navigation = "🎮 Games"
        st.rerun()

    # --------------------------------------------------------
    # COMPETITIVE GAMING
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-title section-pink">'
        'COMPETITIVE GAMING'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="dashboard-card">
            <p>
                Check the CLARIX leaderboard and discover
                competitive players from the gaming community.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "VIEW LEADERBOARD",
        key="dashboard_leaderboard",
        use_container_width=True
    ):
        st.session_state.dashboard_navigation = "🏆 Leaderboard"
        st.rerun()

    # --------------------------------------------------------
    # GAMING NEWS
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-title section-orange">'
        'GAMING NEWS'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="dashboard-card">
            <p>
                Stay updated with gaming announcements,
                seasonal content and important updates.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "READ GAMING NEWS",
        key="dashboard_news",
        use_container_width=True
    ):
        st.session_state.dashboard_navigation = "📰 Gaming News"
        st.rerun()

    # --------------------------------------------------------
    # PLAYER PROFILES
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-title section-green">'
        'PLAYER PROFILES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="dashboard-card">
            <p>
                Explore the player community and discover
                gaming identities across CLARIX.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "EXPLORE PROFILES",
        key="dashboard_profiles",
        use_container_width=True
    ):
        st.session_state.dashboard_navigation = "👤 Player Profiles"
        st.rerun()

    # --------------------------------------------------------
    # COMMAND CENTER
    # --------------------------------------------------------

    st.markdown(
        '<div class="clarix-command-center">'
        'CLARIX COMMAND CENTER'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-command-text">'
        'EXPLORE  •  COMPETE  •  DISCOVER  •  CONNECT'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # QUICK ACCESS
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-title section-green">'
        'QUICK ACCESS'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            '<div class="dashboard-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="quick-game-name quick-minecraft">'
            'MINECRAFT'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="game-card-description">'
            'Sandbox / Adventure'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown(
            '<div class="dashboard-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="quick-game-name quick-fortnite">'
            'FORTNITE'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="game-card-description">'
            'Battle Royale / Action'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col3:

        st.markdown(
            '<div class="dashboard-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="quick-game-name quick-gta">'
            'GRAND THEFT AUTO V'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="game-card-description">'
            'Action / Open World'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# GAMES PAGE
# ============================================================

def show_games():

    st.markdown(
        '<div class="page-title-games">'
        'GAME LIBRARY'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="game-card-description">'
        'Explore the featured games available on CLARIX.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    search = st.text_input(
        "SEARCH GAMES",
        placeholder="Search for a game..."
    )

    filtered_games = games.copy()

    if genre_filter != "All":

        filtered_games = [
            game
            for game in filtered_games
            if game["genre"] == genre_filter
        ]

    if search:

        search_text = search.lower()

        filtered_games = [
            game
            for game in filtered_games
            if (
                search_text in game["name"].lower()
                or search_text in game["genre"].lower()
            )
        ]

    if not filtered_games:

        st.markdown(
            """
            <div class="dashboard-card">
                <div class="game-card-description">
                    No games found.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        return

    for game in filtered_games:

        st.markdown(
            '<div class="game-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-card-title">'
            f'{game["name"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-genre">'
            f'{game["genre"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-card-description">'
            f'{game["description"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if st.button(
            "VIEW DETAILS",
            key=f"details_{game['name']}",
            use_container_width=True
        ):

            if st.session_state.selected_game == game["name"]:

                st.session_state.selected_game = None

            else:

                st.session_state.selected_game = game["name"]

            st.rerun()

        if st.session_state.selected_game == game["name"]:

            st.markdown(
                '<div class="dashboard-card">',
                unsafe_allow_html=True
            )

            display_game_details(game)

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


# ============================================================
# LEADERBOARD PAGE
# ============================================================

def show_leaderboard():

    st.markdown(
        '<div class="page-title-leaderboard">'
        'LEADERBOARD'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="game-card-description">'
        'Top players in the CLARIX competitive gaming community.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    for rank, name in leaderboard:

        st.markdown(
            f"""
            <div class="leader-row">
                <span class="leader-rank">#{rank}</span>
                &nbsp;&nbsp;&nbsp;
                <span class="leader-name">{name}</span>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# GAMING NEWS PAGE
# ============================================================

def show_news():

    st.markdown(
        '<div class="page-title-news">'
        'GAMING NEWS'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="game-card-description">'
        'Latest gaming announcements and updates.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    for item in news:

        st.markdown(
            '<div class="news-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="news-game">'
            f'{item["game"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="news-title">'
            f'{item["title"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="news-date">'
            f'{item["date"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="news-description">'
            f'{item["description"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.link_button(
            "READ MORE",
            item["url"],
            use_container_width=True
        )

        st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# PLAYER PROFILES PAGE
# ============================================================

def show_profiles():

    st.markdown(
        '<div class="page-title-profiles">'
        'PLAYER PROFILES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="game-card-description">'
        'Gaming community profiles on CLARIX.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    profiles = [
        ("FadingLyfe", "Competitive Gamer"),
        ("ᴮᴼᴳPookie Poke", "Gaming Community"),
        ("Crackedv2x ttv", "Competitive Gamer"),
        ("KiLLeR_VaLDee", "Multiplayer Gamer")
    ]

    for name, role in profiles:

        st.markdown(
            f"""
            <div class="profile-card">
                <div class="profile-name">{name}</div>
                <div class="profile-info">
                    {role}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DASHBOARD NAVIGATION
# ============================================================

if st.session_state.dashboard_navigation:

    page = st.session_state.dashboard_navigation

    st.session_state.dashboard_navigation = None


# ============================================================
# PAGE ROUTING
# ============================================================

if page == "🏠 Home":

    show_home()

elif page == "🎮 Games":

    show_games()

elif page == "🏆 Leaderboard":

    show_leaderboard()

elif page == "📰 Gaming News":

    show_news()

elif page == "👤 Player Profiles":

    show_profiles()