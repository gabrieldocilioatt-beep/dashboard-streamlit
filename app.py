import streamlit as st
import pandas as pd

st.title("FROTA DE VEÍCULOS")

st.write("""Atlântico""")

df = pd.read_csv(
    "_tmp_csv_tmpwgC6Of.csv",
    sep=";",
    encoding="latin1",
    skiprows=4,
    on_bad_lines="skip"
)

st.dataframe(df, use_container_width=True)

