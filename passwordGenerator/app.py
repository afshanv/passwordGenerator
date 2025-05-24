import re
import streamlit as st
import random
import string

# --- Password Strength Checker ---
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*).")

    return score, feedback

# --- Password Generator ---
def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(all_chars) for _ in range(length))

# --- Streamlit App ---
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.markdown("---")
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Can be improved.")
        for f in feedback:
            st.info(f)
    else:
        st.error("❌ Weak Password - Please improve:")
        for f in feedback:
            st.info(f)

    st.markdown("---")
    if st.button("💡 Suggest Strong Password"):
        st.code(generate_strong_password(), language="text")
