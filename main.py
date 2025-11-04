import streamlit as st

st.set_page_config(page_title="Laser Controller", page_icon="🔴", layout="centered")

st.title("🔴 Laser Controller")

# --- Laser configuration inputs ---
st.subheader("Laser Configuration")
col1, col2 = st.columns(2)
with col1:
    wavelength = st.text_input("Wavelength (nm)", "532")
    power = st.text_input("Power (mW)", "10")
    pulse_rate = st.text_input("Pulse Rate (Hz)", "50")
with col2:
    duration = st.text_input("Duration (s)", "5")
    beam_diameter = st.text_input("Beam Diameter (mm)", "2.5")
    target_distance = st.text_input("Target Distance (m)", "1.0")

# --- Laser control toggle ---
st.subheader("Laser Control")

laser_on = st.toggle("Laser ON/OFF", value=False)

if laser_on:
    st.success("✅ Laser is ACTIVE")
else:
    st.warning("⚠️ Laser is OFF")

# --- Scan button ---
if st.button("🔍 Start Scan"):
    if not laser_on:
        st.error("Laser must be ON before scanning!")
    else:
        st.info("Scanning in progress...")
        # Simulated scanning action
        st.success("Scan completed successfully ✅")

# --- Status section ---
st.divider()
st.caption("Status log and info:")
st.write({
    "Laser On": laser_on,
    "Wavelength": wavelength,
    "Power": power,
    "Pulse Rate": pulse_rate,
    "Duration": duration,
    "Beam Diameter": beam_diameter,
    "Target Distance": target_distance
})
st.caption("Developed by OpenAI ChatGPT")