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

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GOOGLE FONTS
       ======================================================== */

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@400;500;600;700&display=swap');


    /* ========================================================
       MAIN BACKGROUND
       ======================================================== */

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
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       GENERAL TEXT
       ======================================================== */

    p,
    li {
        font-family: "Rajdhani", sans-serif !important;
        color: #c9d7e8;
    }

    .stMarkdown {
        font-family: "Rajdhani", sans-serif;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

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


    /* ========================================================
       SIDEBAR COLLAPSE BUTTON
       ======================================================== */

    [data-testid="stSidebarCollapseButton"] {
        z-index: 9999 !important;
    }

    [data-testid="stSidebarCollapseButton"] button {
        color: #ffffff !important;
        background-color: #000000 !important;
        border: 2px solid #075fc7 !important;
        border-radius: 8px !important;
        width: 36px !important;
        height: 36px !important;

        box-shadow:
            0 0 8px rgba(0, 100, 255, 0.45) !important;

        transition: all 0.2s ease-in-out !important;
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
        background-color: #000000 !important;
        border-color: #55c7ff !important;

        box-shadow:
            0 0 8px rgba(85, 199, 255, 0.9),
            0 0 20px rgba(0, 140, 255, 0.7) !important;
    }

    [data-testid="stSidebarCollapseButton"] button:hover svg {
        color: #ffffff !important;
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }


    /* ========================================================
       SIDEBAR GAME CATEGORY
       ======================================================== */

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

    [data-testid="stSidebar"] [data-baseweb="select"]
    [role="button"] span {
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


    /* ========================================================
       CLARIX MAIN LOGO
       ======================================================== */

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
        color: #91a9c4 !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 19px !important;
        letter-spacing: 3px;
        margin-top: 8px;
    }

    .gaming-247 {
        text-align: center;
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        letter-spacing: 4px;
        text-shadow:
            0 0 8px rgba(0, 150, 255, 0.7),
            0 0 18px rgba(0, 100, 255, 0.4);
        margin-top: 5px;
    }


    /* ========================================================
       SEARCH BAR
       ======================================================== */

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
        box-shadow: 0 0 0 1px #00aaff !important;
    }

    .stTextInput label {
        color: white !important;
        font-family: "Orbitron", sans-serif !important;
        font-weight: 600 !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        width: 100%;
        background: linear-gradient(
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

        transition: all 0.2s ease-in-out !important;
    }

    .stButton > button:hover {
        background: linear-gradient(
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
        background: linear-gradient(
            90deg,
            #075fc7,
            #064c9b
        ) !important;

        border-color: #55c7ff !important;
    }


    /* ========================================================
       LINK BUTTONS
       ======================================================== */

    [data-testid="stLinkButton"] a {
        background: linear-gradient(
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

        transition: all 0.2s ease-in-out !important;
    }

    [data-testid="stLinkButton"] a:hover {
        background: linear-gradient(
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


    /* ========================================================
       HOME STATS
       ======================================================== */

    .stat-title {
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 13px !important;
        font-weight: 800 !important;
        letter-spacing: 2px;
    }

    .stat-value {
        color: white !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 19px !important;
        font-weight: 700 !important;
    }


    /* ========================================================
       HOME DASHBOARD
       ======================================================== */

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
        color: #55c7ff !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 17px !important;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }

    .home-section-tag {
        color: #91a9c4 !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 13px !important;
        font-weight: 800 !important;
        letter-spacing: 3px;
        margin-bottom: 8px;
    }

    .home-section-title {
        font-family: "Orbitron", sans-serif !important;
        font-size: 23px !important;
        font-weight: 900 !important;
        letter-spacing: 2px;
        margin-top: 8px;
        margin-bottom: 8px;
    }

    .library-title {
        color: #ffcc66 !important;
        text-shadow:
            0 0 8px rgba(255, 190, 80, 0.55);
    }

    .competitive-title {
        color: #ff4fd8 !important;
        text-shadow:
            0 0 8px rgba(255, 79, 216, 0.55);
    }

    .news-section-title {
        color: #ff9d42 !important;
        text-shadow:
            0 0 8px rgba(255, 157, 66, 0.55);
    }

    .profiles-section-title {
        color: #55e69b !important;
        text-shadow:
            0 0 8px rgba(85, 230, 155, 0.55);
    }

    .home-feature-text {
        color: #b9cbe0 !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 17px !important;
        line-height: 1.5;
    }

    .home-divider {
        height: 1px;
        background: linear-gradient(
            90deg,
            transparent,
            #075fc7,
            #55c7ff,
            #075fc7,
            transparent
        );
        margin: 25px 0;
    }

    .command-center-title {
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 25px !important;
        font-weight: 900 !important;
        letter-spacing: 3px;

        text-shadow:
            0 0 8px rgba(0, 150, 255, 0.7);
    }

    .quick-access-title {
        color: #55e69b !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 25px !important;
        font-weight: 900 !important;
        letter-spacing: 3px;

        text-shadow:
            0 0 8px rgba(85, 230, 155, 0.55);
    }

    .home-command-text {
        color: #c77dff !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        letter-spacing: 2px;

        text-shadow:
            0 0 7px rgba(199, 125, 255, 0.55);
    }


    /* ========================================================
       PAGE HEADINGS
       ======================================================== */

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
        color: #55e69b !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 32px !important;
        font-weight: 900 !important;
        letter-spacing: 3px;

        text-shadow:
            0 0 8px rgba(85, 230, 155, 0.75),
            0 0 22px rgba(0, 200, 120, 0.35);
    }


    /* ========================================================
       GAME GENRE
       ======================================================== */

    .game-genre {
        display: inline-block;

        font-family: "Rajdhani", sans-serif;
        font-size: 17px;
        font-weight: 700;
        letter-spacing: 2px;

        color: #55c7ff !important;

        background: rgba(0, 130, 255, 0.10);
        border: 1px solid rgba(0, 150, 255, 0.45);
        border-radius: 5px;

        padding: 4px 11px;
        margin-bottom: 13px;

        text-shadow:
            0 0 8px rgba(0, 150, 255, 0.55);
    }


    /* ========================================================
       GAME DETAILS
       ======================================================== */

    .game-detail-title {
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 25px !important;
        font-weight: 900 !important;
        letter-spacing: 2px;

        text-shadow:
            0 0 8px rgba(0, 150, 255, 0.65);
    }

    .game-detail-label {
        color: #ffcc66 !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
    }

    .game-detail-value {
        color: #c9d7e8 !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 17px !important;
        font-weight: 600 !important;
    }


    /* ========================================================
       LEADERBOARD
       ======================================================== */

    .leaderboard-name {
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        letter-spacing: 1px;

        text-shadow:
            0 0 6px rgba(0, 150, 255, 0.6);
    }

    .leaderboard-rank {
        color: #ffcc66 !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 25px !important;
        font-weight: 900 !important;

        text-shadow:
            0 0 8px rgba(255, 190, 80, 0.5);
    }

    .leaderboard-row {
        padding: 8px 0;
    }


    /* ========================================================
       NEWS
       ======================================================== */

    .news-game {
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        letter-spacing: 2px;
    }

    .news-title {
        color: #ff9d42 !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        letter-spacing: 1px;
    }

    .news-date {
        color: #c77dff !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
    }

    .news-description {
        color: #b9cbe0 !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 17px !important;
        line-height: 1.5;
    }


    /* ========================================================
       PLAYER PROFILES
       ======================================================== */

    .profile-name {
        color: #55e69b !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 23px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;

        text-shadow:
            0 0 8px rgba(85, 230, 155, 0.65);
    }

    .profile-rank {
        color: #ff4fd8 !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 17px !important;
        font-weight: 700 !important;
    }


    /* ========================================================
       QUICK ACCESS
       ======================================================== */

    .quick-title {
        color: #55c7ff !important;
        font-family: "Orbitron", sans-serif !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
    }

    .quick-genre {
        color: #c77dff !important;
        font-family: "Rajdhani", sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA
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
# PAGE NAVIGATION HELPER
# ============================================================

def go_to_page(page):
    st.session_state.page = page
    st.session_state.selected_game = None


# ============================================================
# GAME DETAILS
# ============================================================

def display_game_details(game):

    st.markdown(
        f'<div class="game-detail-title">{game["name"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="game-genre">{game["genre"]}</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="game-detail-label">DEVELOPER</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-detail-value">'
            f'{game["developer"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<br><div class="game-detail-label">RELEASE</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-detail-value">'
            f'{game["release"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<br><div class="game-detail-label">PLAYERS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-detail-value">'
            f'{game["players"]}'
            f'</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="game-detail-label">PLATFORMS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="game-detail-value">'
            f'{game["platforms"]}'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="game-detail-label">ABOUT THE GAME</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="game-detail-value">'
        f'{game["description"]}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="game-detail-label">GAMEPLAY FEATURES</div>',
        unsafe_allow_html=True
    )

    for feature in game["features"]:

        st.markdown(
            f'<div class="game-detail-value">'
            f'• {feature}'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "OFFICIAL WEBSITE",
        game["official"],
        use_container_width=True
    )


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

    page_options = [
        "🏠 Home",
        "🎮 Games",
        "🏆 Leaderboard",
        "📰 Gaming News",
        "👤 Player Profiles"
    ]

    current_index = page_options.index(st.session_state.page)

    page_name = st.radio(
        "NAVIGATION",
        page_options,
        index=current_index,
        label_visibility="collapsed"
    )

    if page_name != st.session_state.page:
        st.session_state.page = page_name
        st.session_state.selected_game = None
        st.rerun()

    st.markdown("---")

    st.markdown("### GAME CATEGORY")

    genre_filter = st.selectbox(
        "Select Genre",
        [
            "All",
            "Sandbox / Adventure",
            "Battle Royale / Action",
            "Action / Open World"
        ],
        label_visibility="collapsed"
    )


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "🏠 Home":

    st.markdown(
        '<div class="clarix-logo">CLARIX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="clarix-tagline">'
        'YOUR COMMAND CENTER FOR THE GAMING WORLD'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="gaming-247">GAMING 24 / 7</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # --------------------------------------------------------
    # STATS
    # --------------------------------------------------------

    stat1, stat2, stat3, stat4 = st.columns(4)

    with stat1:

        st.markdown(
            '<div class="stat-title">FEATURED GAMES</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="stat-value">3</div>',
            unsafe_allow_html=True
        )

    with stat2:

        st.markdown(
            '<div class="stat-title">GAME DATA</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="stat-value">REAL</div>',
            unsafe_allow_html=True
        )

    with stat3:

        st.markdown(
            '<div class="stat-title">GAMING NEWS</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="stat-value">LIVE</div>',
            unsafe_allow_html=True
        )

    with stat4:

        st.markdown(
            '<div class="stat-title">GAMING HUB</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="stat-value">24 / 7</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # GAMING DASHBOARD
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-dashboard-title">'
        'GAMING DASHBOARD'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-dashboard-intro">'
        'YOUR COMMAND CENTER FOR THE GAMING WORLD'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # GAME LIBRARY
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-tag">01 / EXPLORE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-section-title library-title">'
        'GAME LIBRARY'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-feature-text">'
        'Discover detailed information about Minecraft, Fortnite '
        'and Grand Theft Auto V. Explore genres, developers, '
        'platforms, gameplay and features.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "EXPLORE GAMES",
        key="home_explore_games",
        use_container_width=True
    ):
        go_to_page("🎮 Games")
        st.rerun()

    st.markdown(
        '<div class="home-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # COMPETITIVE GAMING
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-tag">02 / COMPETE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-section-title competitive-title">'
        'COMPETITIVE GAMING'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-feature-text">'
        'Track competitive players, explore leaderboard positions '
        'and keep an eye on the competitive gaming scene.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "VIEW LEADERBOARD",
        key="home_view_leaderboard",
        use_container_width=True
    ):
        go_to_page("🏆 Leaderboard")
        st.rerun()

    st.markdown(
        '<div class="home-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # GAMING NEWS
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-tag">03 / DISCOVER</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-section-title news-section-title">'
        'GAMING NEWS'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-feature-text">'
        'Stay connected with announcements, seasonal events, '
        'updates and important developments from your favorite games.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "OPEN GAMING NEWS",
        key="home_news_button",
        use_container_width=True
    ):
        go_to_page("📰 Gaming News")
        st.rerun()

    st.markdown(
        '<div class="home-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # PLAYER PROFILES
    # --------------------------------------------------------

    st.markdown(
        '<div class="home-section-tag">04 / CONNECT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-section-title profiles-section-title">'
        'PLAYER PROFILES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-feature-text">'
        'Explore competitive player names and leaderboard positions '
        'displayed through the CLARIX gaming hub.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "VIEW PLAYER PROFILES",
        key="home_profiles_button",
        use_container_width=True
    ):
        go_to_page("👤 Player Profiles")
        st.rerun()

    st.markdown(
        '<div class="home-divider"></div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # COMMAND CENTER
    # --------------------------------------------------------

    st.markdown(
        '<div class="command-center-title">'
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

    st.write(
        "Everything you need to explore the gaming world, "
        "all in one place."
    )


    # --------------------------------------------------------
    # QUICK ACCESS
    # --------------------------------------------------------

    st.markdown(
        '<div class="quick-access-title">'
        'QUICK ACCESS'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    quick1, quick2, quick3 = st.columns(3)

    with quick1:

        st.markdown(
            '<div class="quick-title">MINECRAFT</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="quick-genre">'
            'SANDBOX / ADVENTURE'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "OFFICIAL WEBSITE",
            "https://www.minecraft.net/",
            use_container_width=True
        )

    with quick2:

        st.markdown(
            '<div class="quick-title">FORTNITE</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="quick-genre">'
            'BATTLE ROYALE / ACTION'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "OFFICIAL WEBSITE",
            "https://www.fortnite.com/",
            use_container_width=True
        )

    with quick3:

        st.markdown(
            '<div class="quick-title">'
            'GRAND THEFT AUTO V'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="quick-genre">'
            'ACTION / OPEN WORLD'
            '</div>',
            unsafe_allow_html=True
        )

        st.link_button(
            "OFFICIAL WEBSITE",
            "https://www.rockstargames.com/gta-v",
            use_container_width=True
        )


# ============================================================
# GAMES
# ============================================================

elif st.session_state.page == "🎮 Games":

    st.markdown(
        '<div class="page-title-games">'
        'GAME LIBRARY'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#55c7ff; '
        'font-family:Rajdhani; '
        'font-size:17px; '
        'margin-top:5px;">'
        'EXPLORE YOUR FAVORITE GAMES'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    search_query = st.text_input(
        "SEARCH GAMES",
        placeholder="Search for a game...",
        key="game_search"
    )

    filtered_games = []

    for game in games:

        if search_query.strip():

            matches_search = (
                search_query.strip().lower()
                in game["name"].lower()
            )

        else:

            matches_search = True

        matches_genre = (
            genre_filter == "All"
            or genre_filter == game["genre"]
        )

        if matches_search and matches_genre:
            filtered_games.append(game)


    if not filtered_games:

        st.warning(
            "No games found matching your search."
        )

    else:

        for game in filtered_games:

            st.markdown(
                f'<div class="game-detail-title">'
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

            if st.button(
                "VIEW DETAILS"
                if st.session_state.selected_game != game["name"]
                else "HIDE DETAILS",
                key=f"game_details_{game['name']}",
                use_container_width=True
            ):

                if (
                    st.session_state.selected_game
                    == game["name"]
                ):
                    st.session_state.selected_game = None
                else:
                    st.session_state.selected_game = game["name"]

                st.rerun()


            if (
                st.session_state.selected_game
                == game["name"]
            ):

                display_game_details(game)


            st.markdown(
                '<div class="home-divider"></div>',
                unsafe_allow_html=True
            )


# ============================================================
# LEADERBOARD
# ============================================================

elif st.session_state.page == "🏆 Leaderboard":

    st.markdown(
        '<div class="page-title-leaderboard">'
        'FORTNITE RANKED LEADERBOARD'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#8ed8ff; '
        'font-family:Rajdhani; '
        'font-size:17px; '
        'margin-top:5px;">'
        'TOP COMPETITIVE PLAYERS'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    for rank, player in leaderboard:

        st.markdown(
            '<div class="leaderboard-row">',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([1, 7])

        with col1:

            st.markdown(
                f'<div class="leaderboard-rank">'
                f'#{rank}'
                f'</div>',
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f'<div class="leaderboard-name">'
                f'{player}'
                f'</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")


# ============================================================
# GAMING NEWS
# ============================================================

elif st.session_state.page == "📰 Gaming News":

    st.markdown(
        '<div class="page-title-news">'
        'GAMING NEWS'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#c77dff; '
        'font-family:Rajdhani; '
        'font-size:17px; '
        'margin-top:5px;">'
        'ANNOUNCEMENTS • EVENTS • UPDATES'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    for item in news:

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

        st.write("")

        st.link_button(
            "READ MORE",
            item["url"],
            use_container_width=True
        )

        st.markdown(
            '<div class="home-divider"></div>',
            unsafe_allow_html=True
        )


# ============================================================
# PLAYER PROFILES
# ============================================================

elif st.session_state.page == "👤 Player Profiles":

    st.markdown(
        '<div class="page-title-profiles">'
        'PLAYER PROFILES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#ff4fd8; '
        'font-family:Rajdhani; '
        'font-size:17px; '
        'margin-top:5px;">'
        'COMPETITIVE GAMING COMMUNITY'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    for rank, player in leaderboard:

        st.markdown(
            f'<div class="profile-name">'
            f'{player}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="profile-rank">'
            f'FORTNITE RANKED POSITION: #{rank}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="home-divider"></div>',
            unsafe_allow_html=True
        )