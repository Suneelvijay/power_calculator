import streamlit as st
import math

class UnitConverter:
    def __init__(self):
        pass

    def calculate_pre_unit(self, actual, base):
        return actual / base if base != 0 else "Base value cannot be zero"

    def calculate_actual_from_pre_unit(self, pre_unit, base):
        return pre_unit * base

    def calculate_base_from_pre_unit(self, pre_unit, actual):
        return actual / pre_unit if pre_unit != 0 else "Pre-unit value cannot be zero"
        
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


def calculate_rp(voltage, current, power_factor):
    if voltage and current and power_factor:
        power = voltage * current * power_factor
        return power
    else:
        return None
        
def calculate_Rp(voltage, current, power_factor):
    if voltage and current and power_factor:
        power = voltage * current * sqrt(1 - power_factor**2)
        return power
    else:
        return None
        
def calculate_ap(voltage, current, power_factor):
    if voltage and current and power_factor:
        power = voltage * current
        return power
    else:
        return None

def power_calculator():
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


def per_unit_calculator():
    st.title('Per-unit Calculator')
    # Add functionality for per-unit calculator
    converter = UnitConverter()

    conversion_type = st.selectbox('Select Conversion Type', ('Actual/Base to Pre-unit', 'Pre-unit to Actual', 'Pre-unit to Base'))

    if conversion_type == 'Actual/Base to Pre-unit':
        actual = st.number_input('Enter Actual Quantity:', value=1)
        base = st.number_input('Enter Base Quantity:', value=1)
        pre_unit_result = converter.calculate_pre_unit(actual, base)
        st.write(f'Pre-unit value is: {pre_unit_result}')

    elif conversion_type == 'Pre-unit to Actual':
        pre_unit = st.number_input('Enter Pre-unit Quantity:')
        base = st.number_input('Enter Base Quantity:', value=1)
        actual_result = converter.calculate_actual_from_pre_unit(pre_unit, base)
        st.write(f'Actual value is: {actual_result:.2f}')

    elif conversion_type == 'Pre-unit to Base':
        pre_unit = st.number_input('Enter Pre-unit Quantity:')
        actual = st.number_input('Enter Actual Quantity:', value=1)
        base_result = converter.calculate_base_from_pre_unit(pre_unit, actual)
        st.write(f'Base value is: {base_result:.2f}')


def three_phase_power_calculator():
    st.title('Three-Phase Power Calculator')
    
    voltage = st.number_input('Enter line voltage (V):')
    current = st.number_input('Enter line current (I):')
    power_factor = st.number_input('Enter power factor:')
    type = st.selectbox('Select Power Type', ('Real Power', 'Reactive Power', 'Apparent Power'))
    if type == 'Real Power':
        result = calculate_rp(voltage, current, power_factor)
        if result is not None:
            st.write(f"Calculated Three-Phase Power: {result} watts")
        else:
            st.write("Insufficient input to calculate three-phase power.")
    elif type == 'Reactive Power':
        result = calculate_Rp(voltage, current, power_factor)
        if result is not None:
            st.write(f"Calculated Three-Phase Power: {result} watts")
        else:
            st.write("Insufficient input to calculate three-phase power.")
    elif type == 'Apparent Power':
        result = calculate_ap(voltage, current, power_factor)
        if result is not None:
            st.write(f"Calculated Three-Phase Power: {result} watts")
        else:
            st.write("Insufficient input to calculate three-phase power.")
    

def main():
    st.sidebar.title('Calculator Options')
    calculator_option = st.sidebar.selectbox('Select Calculator', ('Power Calculator', 'Per-unit Calculator', 'Three-Phase Power Calculator'))

    if calculator_option == 'Power Calculator':
        power_calculator()
    elif calculator_option == 'Per-unit Calculator':
        per_unit_calculator()
    elif calculator_option == 'Three-Phase Power Calculator':
        three_phase_power_calculator()


if __name__ == "__main__":
    main()
    
st.markdown(
        '<div style="text-align:center; margin-top: 42px">'
        '<a href = "https://github.com/Suneelvijay/" style = "text-decoration: none;" ><p style="font-size: 10px;">Suneelvijay Projects © 2023 .</a></p>'
        '<p style="font-size: 10px;">Open Source rights reserved.</p>'
        '</div>',
        unsafe_allow_html=True
    )
