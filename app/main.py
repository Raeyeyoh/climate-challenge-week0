import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title(" Climate Analysis Dashboard (2015–2026)")

df = load_data()

st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

years = st.sidebar.slider(
    "Select Year Range",
    int(df["DATE"].dt.year.min()),
    int(df["DATE"].dt.year.max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

df_filtered = df[
    (df["Country"].isin(countries)) &
    (df["DATE"].dt.year.between(years[0], years[1]))
]


st.subheader("Temperature Trend")

temp = df_filtered.groupby(["DATE", "Country"])["T2M"].mean().reset_index()

fig, ax = plt.subplots()
for country in countries:
    data = temp[temp["Country"] == country]
    ax.plot(data["DATE"], data["T2M"], label=country)

ax.legend()
ax.set_title("Temperature Over Time")
st.pyplot(fig)


st.subheader("Precipitation Distribution")

fig2, ax2 = plt.subplots()
sns.boxplot(data=df_filtered, x="Country", y="PRECTOTCORR", ax=ax2)
ax2.set_title("Rainfall Distribution by Country")

st.pyplot(fig2)
