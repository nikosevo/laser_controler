import streamlit as st

st.set_page_config(page_title="Laser Controller", page_icon="🔴", layout="centered")

st.title("🔴 Laser Controller")

# --- Initialize session state for lasers ---
if 'lasers' not in st.session_state:
    st.session_state.lasers = [
        {
            "id": 1,
            "name": "Laser 1",
            "wavelength": "532",
            "power": "10",
            "pulse_rate": "50",
            "duration": "5",
            "beam_diameter": "2.5",
            "target_distance": "1.0",
            "laser_on": False,
            "custom_widgets": []
        }
    ]

# --- Button to add a new laser ---
if st.button("Add New Laser"):
    new_laser_id = len(st.session_state.lasers) + 1
    st.session_state.lasers.append(
        {
            "id": new_laser_id,
            "name": f"Laser {new_laser_id}",
            "wavelength": "532",
            "power": "10",
            "pulse_rate": "50",
            "duration": "5",
            "beam_diameter": "2.5",
            "target_distance": "1.0",
            "laser_on": False,
            "custom_widgets": []
        }
    )

st.divider()

# --- Display each laser ---
for laser in st.session_state.lasers:
    st.subheader(laser["name"])
    col1, col2, col3 = st.columns([1, 2, 2])
    with col1:
        laser["laser_on"] = st.toggle("ON/OFF", value=laser["laser_on"], key=f"on_off_{laser['id']}")
    with col2:
        laser["wavelength"] = st.text_input("Wavelength (nm)", value=laser["wavelength"], key=f"wavelength_{laser['id']}")
    with col3:
        if st.button("🔍 Start Scan", key=f"scan_{laser['id']}"):
            if not laser["laser_on"]:
                st.error(f"{laser['name']} must be ON before scanning!")
            else:
                st.info(f"Scanning with {laser['name']}...")
                st.success(f"Scan with {laser['name']} completed successfully ✅")

    with st.expander("Detailed Configuration"):
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            laser["power"] = st.text_input("Power (mW)", value=laser["power"], key=f"power_{laser['id']}")
            laser["pulse_rate"] = st.text_input("Pulse Rate (Hz)", value=laser["pulse_rate"], key=f"pulse_rate_{laser['id']}")
        with d_col2:
            laser["duration"] = st.text_input("Duration (s)", value=laser["duration"], key=f"duration_{laser['id']}")
            laser["beam_diameter"] = st.text_input("Beam Diameter (mm)", value=laser["beam_diameter"], key=f"beam_diameter_{laser['id']}")
            laser["target_distance"] = st.text_input("Target Distance (m)", value=laser["target_distance"], key=f"target_distance_{laser['id']}")

        st.subheader("Add Custom Widgets")
        widget_type = st.selectbox("Widget Type", ["Text Input", "Number Input", "Button"], key=f"widget_type_{laser['id']}")
        widget_label = st.text_input("Widget Label", key=f"widget_label_{laser['id']}")

        if st.button("Add Widget", key=f"add_widget_{laser['id']}"):
            laser["custom_widgets"].append({"type": widget_type, "label": widget_label})

        for widget in laser["custom_widgets"]:
            if widget["type"] == "Text Input":
                st.text_input(widget["label"], key=f"custom_{laser['id']}_{widget['label']}")
            elif widget["type"] == "Number Input":
                st.number_input(widget["label"], key=f"custom_{laser['id']}_{widget['label']}")
            elif widget["type"] == "Button":
                st.button(widget["label"], key=f"custom_{laser['id']}_{widget['label']}")

    st.divider()

st.caption("Developed by OpenAI ChatGPT")
