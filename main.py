import streamlit as st

def calculate_power(voltage, current, resistance, conductance, energy, time, power_factor):
    power = None
    
    if voltage and current:
        power = voltage * current

    elif current and resistance:
        power = (current ** 2) * resistance

    elif voltage and resistance:
        power = (voltage ** 2) / resistance

    elif current and conductance:
        power = (current ** 2) / conductance

    elif energy and time:
        power = energy / time

    elif voltage and current and power_factor:
        power = voltage * current * power_factor

    return power


def main():
    st.title('Power Calculator')

    voltage = st.number_input('Enter voltage:')
    current = st.number_input('Enter current:')
    resistance = st.number_input('Enter resistance:')
    conductance = st.number_input('Enter conductance:')
    energy = st.number_input('Enter energy:')
    time = st.number_input('Enter time:')
    power_factor = st.number_input('Enter power factor:')

    if st.button('Calculate Power'):
        result = calculate_power(voltage, current, resistance, conductance, energy, time, power_factor)
        if result is not None:
            st.write(f"Calculated Power: {result} watts")
        else:
            st.write("Insufficient input to calculate power.")


if __name__ == "__main__":
    main()
