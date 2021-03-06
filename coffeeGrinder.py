import streamlit as st
import math
# 1 cup equals .75 tablepoons

st.markdown("<h1 style='text-align: center; '>Coffee Magic</h1>", unsafe_allow_html=True)
st.write("Welcome to the coffee selector.")
coffeeInput = st.text_input("How do you like your coffee: Strong or Weak? ")
#coffeeInput = input("Select Coffee Strength: Strong or Weak? ")
coffeeVolume = st.number_input("Water filled to which line? ")
#coffeeVolume = input("Water filled to what line on the coffee Pot? ")
grind = 1.2381

coffeePOTTOTAL = 4
watercup = coffeeVolume / 2
tbSpoon = (2 * watercup)

tbSpoon = tbSpoon / grind

def strength():
    if coffeeInput.lower() == "strong":
        return math.ceil(tbSpoon)
    elif coffeeInput.lower() == 'weak':
        return math.floor(tbSpoon)
    else:
        return "incorrect" 

st.write("Set the Grinder to %s" % strength())
