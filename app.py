import streamlit as st
from chempy import balance_stoichiometry

st.set_page_config(page_title="Balanceador de Ecuaciones Químicas", page_icon="⚗️")

st.title("⚗️ Calculadora de Balanceo Químico")
st.write("Ingresa una ecuación química no balanceada (por ejemplo: `H2 + O2 -> H2O`)")

# Input del usuario
input_eq = st.text_input("Ecuación no balanceada", "H2 + O2 -> H2O")

def balance_equation(equation):
    try:
        reactants_str, products_str = equation.split("->")
        reactants = set(s.strip() for s in reactants_str.split("+"))
        products = set(s.strip() for s in products_str.split("+"))

        reac, prod = balance_stoichiometry(reactants, products)
        balanced_eq = " + ".join(f"{reac[k]} {k}" for k in reac) + " -> " + " + ".join(f"{prod[k]} {k}" for k in prod)
        return balanced_eq
    except Exception as e:
        return f"❌ Error: {str(e)}"

if input_eq:
    result = balance_equation(input_eq)
    st.markdown(f"### ✅ Ecuación balanceada:")
    st.latex(result.replace(" ", "\\,"))
