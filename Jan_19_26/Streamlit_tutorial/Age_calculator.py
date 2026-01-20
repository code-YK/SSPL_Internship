import streamlit as st
from datetime import date

# Streamlit App : Age Calculator

st.title("Age Calculator App")
st.subheader("Calculate your age in years, months, days")

today = date.today()
st.write(f"Today's date: {today}")

dob = st.date_input("Enter your date of birth",min_value=date(1900,1,1), max_value=today, format="DD/MM/YYYY")

if dob:
    st.write(f"Your date of birth: {dob}")

if dob < today:
    age_days = (today - dob).days
    
    # Calculate years
    age_years = today.year - dob.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age_years -= 1
    
    # Calculate months
    age_months = today.month - dob.month
    if today.day < dob.day:
        age_months -= 1
    if age_months < 0:
        age_months += 12
    
    # Calculate remaining days
    if today.day >= dob.day:
        age_remaining_days = today.day - dob.day
    else:
        # Get days in previous month
        if today.month == 1:
            prev_month_days = 31
        else:
            from calendar import monthrange
            prev_month_days = monthrange(today.year, today.month - 1)[1]
        age_remaining_days = prev_month_days - dob.day + today.day

    st.write(f"You are {age_years} years, {age_months} months, and {age_remaining_days} days old.")