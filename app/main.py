import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(page_title="Solar Comparison Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    sierra = pd.read_csv("data/sierra-leone_clean.csv")

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"

    return pd.concat([benin, togo, sierra], ignore_index=True)

df = load_data()

# --- Sidebar ---
st.sidebar.title("🌍 Filter Options")
selected_country = st.sidebar.multiselect("Select countries", df["Country"].unique(), default=df["Country"].unique())

filtered_df = df[df["Country"].isin(selected_country)]

# --- Title ---
st.title("☀️ Solar Radiation Dashboard")
st.markdown("Analyze and compare GHI, DNI, and DHI across Benin, Togo, and Sierra Leone.")

# --- Summary Stats ---
st.subheader("📊 Summary Statistics")
st.dataframe(filtered_df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2))

# --- Visualizations ---
st.subheader("📈 Distribution of Irradiance")
cols = st.columns(3)

for i, col in enumerate(["GHI", "DNI", "DHI"]):
    with cols[i]:
        st.write(f"### {col}")
        fig, ax = plt.subplots()
        sns.boxplot(data=filtered_df, x="Country", y=col, ax=ax)
        st.pyplot(fig)
