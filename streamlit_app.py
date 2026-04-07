import streamlit as st

st.set_page_config(
    page_title="IRONMAN view",
#    page_icon="Logo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def inject_custom_css():
    st.markdown("""
        <style>
        /* Hide the default Streamlit sidebar and header */
        [data-testid="collapsedControl"] { display: none; }
        section[data-testid="stSidebar"] { display: none; }
        header {visibility: hidden;}
        
        /* Reduce top/bottom padding of main content */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
        }
        
        /* Color accent bar at the top of the page */
        .disk-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 10px;
            background: linear-gradient(
                90deg,
                #d32f2f 0%,
                #d32f2f 25%,
                #1976d2 30%,
                #1976d2 55%,
                #d4af37 60%,
                #d4af37 80%,
                #e0e0e0 85%,
                #e0e0e0 100%
            );
        }
                
        /* Mobile Responsiveness Overrides */
        @media (max-width: 640px) {
            .hero-title {
                font-size: 4rem !important;
                line-height: 1.2 !important;
                width: 100% !important;
            }
            .block-container {
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
                max-width: 100% !important;
            }
        }

        /* --- Header Nav Link Colors --- */
        div[data-testid="stColumn"] a[data-testid="stPageLink-NavLink"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }

        </style>
        
        <div class="disk-bar"></div>
        <div class="disk-bar2"></div>

    """, unsafe_allow_html=True)

inject_custom_css()

pages = {
    "Race compare": st.Page("pages/race_comp.py", title="Home", icon="🏠"),
    "Athlete compare": st.Page("pages/athlete_comp.py", title="Athletes", icon="🏋️"),
    "Records": st.Page("pages/records.py", title="Records", icon="🏆"),
    "Info": st.Page("pages/info.py", title="Info", icon="ℹ️")
}

# Render top navigation using native columns
with st.container():
    # Col 0 is the Logo, the rest are nav links
    headerNavLinks = st.columns([5, 1, 1, 1, 1, 1])
    
    with headerNavLinks[0]: 
        st.markdown('<div class="nav-logo">PL<span>view</span></div>', unsafe_allow_html=True)
    with headerNavLinks[1]: st.page_link(pages["Race compare"], label="Home", icon="🏠", use_container_width=True)
    with headerNavLinks[2]: st.page_link(pages["Athlete compare"], label="Athletes", icon="🏋️", use_container_width=True)
    with headerNavLinks[3]: st.page_link(pages["Records"], label="Records", icon="🏆", use_container_width=True)
    with headerNavLinks[4]: st.page_link(pages["Info"], label="Info", icon="ℹ️", use_container_width=True)

st.markdown("---")
