import streamlit as st
import math

print("Welcome to the coffee selector.")
coffeeInput = st.text_input("label goes here ")
#coffeeInput = input("Select Coffee Strength: Strong or Weak? ")
coffeeVolume = st.text_input("Water filled to which line? ")
#coffeeVolume = input("Water filled to what line on the coffee Pot? ")
grind = 1.2381

coffeePOTTOTAL = 4
watercup = int(coffeeVolume) / 2
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
