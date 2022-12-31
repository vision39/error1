def convert_units(value, from_unit, to_unit):
    # Convert the value to meters
    if from_unit == 'km':
        value = int(value) * 1000
    elif from_unit == 'cm':
        value = int(value) / 100
    elif from_unit == 'ft':
        value = int(value) * 0.3048
    elif from_unit == 'in':
        value = int(value) * 0.0254
    else:
        return 'Invalid unit'
    
    # Convert the value from meters to the desired unit
    if to_unit == 'km':
        value = int(value) / 1000
    elif to_unit == 'cm':
        value = int(value) * 100
    elif to_unit == 'ft':
        value = int(value) / 0.3048
    elif to_unit == 'in':
        value = int(value) / 0.0254
    else:
        return 'Invalid unit'
    
    return value