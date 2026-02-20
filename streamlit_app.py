import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go

# Set up the web page layout
st.set_page_config(page_title="Bangladesh Capital Market", layout="wide")

# Sidebar for Presentation Navigation
st.sidebar.title("Navigation")
slide = st.sidebar.radio("Go to Slide:", (
    "1. Title Page",
    "2. What is Capital Market?",
    "3. BSEC & Ecosystem",
    "4. Regional Market Preview",
    "5. DSEX Movement & Turnover",
    "6. Policy Implications",
    "7. Q & A"
))

# -------------------------------------------------------------------
# Slide 1: Title Slide
# -------------------------------------------------------------------
if slide == "1. Title Page":
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>Fostering Trust, Fueling Growth</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>An Overview Of Bangladesh Capital Market</h3>", unsafe_allow_html=True)
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Presented By:")
        st.write("**Team M.S.T.**")
    with col2:
        st.subheader("Presented To:")
        st.write("**Nazrul Islam**")
        st.write("Assistant Professor, Department Of Economics")
        st.write("Rabindra University, Bangladesh")

# -------------------------------------------------------------------
# Slide 2: What is Capital Market?
# -------------------------------------------------------------------
elif slide == "2. What is Capital Market?":
    st.title("What is a Capital Market?")
    
    st.markdown("""
    A capital market is a financial market where **companies, governments, and institutions** raise long-term funds (usually for more than 1 year) and where investors invest money to earn returns.
    
    #### Core Balance:
    * 🟢 **Protect:** Safeguarding investor interests.
    * 🔴 **Develop:** Fueling economic and industrial growth.
    """)
    
    st.info(" *“Capital market around the world is the provider of long-term finance to the industries and infrastructure development.”* — Message from the Chairman")

# -------------------------------------------------------------------
# Slide 3: Ecosystem & Regulation
# -------------------------------------------------------------------
elif slide == "3. BSEC & Ecosystem":
    st.title("Founded to Regulate and Develop")
    st.subheader("Bangladesh Securities and Exchange Commission (BSEC)")
    
    st.write("Established under the Bangladesh Securities and Exchange Commission Act, 1993. It is a statutory body attached to the Ministry of Finance.")
    
    st.markdown("""
    ### The Capital Market Ecosystem:
    * **Regulator:** BSEC (IOSCO Category 'A' Member)
    * **Stock Exchanges:** DSE (Dhaka) & CSE (Chittagong)
    * **Central & Clearing:** CDBL, CCBL
    * **Market Intermediates:** Brokers, Dealers, Merchant Bankers, Asset Managers
    * **Instruments:** Equity (IPO, RPO, Rights), Debt (Bonds), Funds (Mutual, ETF)
    * **Investors:** Retail, Institutional, Foreign
    """)

# -------------------------------------------------------------------
# Slide 4: Regional Market Preview (Dynamic Chart)
# -------------------------------------------------------------------
elif slide == "4. Regional Market Preview":
    st.title("Last Year Preview OF Capital Market")
    st.write("Return in % (Dec 31, 2024 to Dec 15, 2025)")
    
    # Dynamic Data
    data = {
        "Country": ["India", "Pakistan", "Sri Lanka", "Bangladesh"],
        "Return (%)": [12.5, 8.3, 5.2, 18.7]
    }
    df = pd.DataFrame(data)
    
    # Interactive Plotly Chart
    fig = px.bar(df, x="Country", y="Return (%)", color="Return (%)", 
                 color_continuous_scale=px.colors.diverging.RdYlGn,
                 text="Return (%)", title="Regional Market Returns")
    fig.update_traces(textposition='outside', textfont_size=14)
    fig.update_layout(yaxis_title="Return (%)", xaxis_title="Country")
    
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------------
# Slide 5: DSEX Movement & Turnover (Dynamic Charts)
# -------------------------------------------------------------------
elif slide == "5. DSEX Movement & Turnover":
    st.title("Market Performance: DSEX & Turnover")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Movement of DSEX Since Jan 2024")
        dsex_data = pd.DataFrame({
            "Date": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01"],
            "Points": [6500, 6650, 6800, 7100]
        })
        fig1 = px.line(dsex_data, x="Date", y="Points", markers=True, title="DSEX Points Over Time")
        fig1.update_traces(line_color='mediumvioletred', line_width=4, marker_size=12)
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        st.subheader("Turnover So Far This Month (Feb '26)")
        turnover_data = pd.DataFrame({
            "Date": ["Feb 1", "Feb 2", "Feb 3", "Feb 4"],
            "Crore Taka": [250, 320, 275, 410]
        })
        fig2 = px.bar(turnover_data, x="Date", y="Crore Taka", text="Crore Taka", title="Daily Turnover (in Crore Taka)")
        fig2.update_traces(marker_color='#3498db', textposition='outside')
        st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------------------------
# Slide 6: Policy Implications
# -------------------------------------------------------------------
elif slide == "6. Policy Implications":
    st.title("Policy Implications")
    st.write("To drive future growth and trust in the market, the following actions are crucial:")
    
    st.markdown("""
    * 🚫 **Curb corruption & extortion**
    * 📈 **Boost investment & employment**
    * 📉 **Low down lending rate & remove bureaucratic hurdles**
    * 🚪 **The pathway for new IPOs made easier to enter**
    """)
    
    st.success("Dedicated Policy and Implementation Programs: Ongoing Investor’s Education Program and Training.")

# -------------------------------------------------------------------
# Slide 7: Q&A
# -------------------------------------------------------------------
elif slide == "7. Q & A":
    st.markdown("<h1 style='text-align: center; margin-top: 100px;'>Thank You For Your Attention!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: gray;'>Any Questions?</h2>", unsafe_allow_html=True)
    st.balloons() # Adds a fun dynamic animation on the final slide