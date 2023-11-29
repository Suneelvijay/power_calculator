import streamlit as st

def calculate_power(voltage, current, resistance, conductance, energy, time):
    power = None

    if voltage and current:
        power = voltage * current

    elif voltage and resistance:
        power = (voltage ** 2) / resistance

    elif current and resistance:
        power = (current ** 2) * resistance

    elif current and conductance:
        power = (current ** 2) / conductance

    elif energy and time:
        power = energy / time

    return power


def main():
    st.title('Power Calculator')

    selected_param_1 = st.selectbox('Select first parameter', ('V', 'I', 'R', 'G', 'E'))
    selected_param_2 = st.selectbox('Select second parameter', ('I', 'R', 'V', 'G', 't'))

    input_values = {
        'V': None,
        'I': None,
        'R': None,
        'G': None,
        'E': None,
        't': None
    }

    if selected_param_1 in input_values:
        input_values[selected_param_1] = st.number_input('Enter value for ' + selected_param_1 + ':')

    if selected_param_2 in input_values:
        input_values[selected_param_2] = st.number_input('Enter value for ' + selected_param_2 + ':')

    if st.button('Calculate Power'):
        result = calculate_power(input_values.get('V'),
                                 input_values.get('I'),
                                 input_values.get('R'),
                                 input_values.get('G'),
                                 input_values.get('E'),
                                 input_values.get('t'))
        if result is not None:
            st.write(f"Calculated Power: {result} watts")
        else:
            st.write("Insufficient input to calculate power.")


if __name__ == "__main__":
    main()
