"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800) and (neutrons_emitted > 500) and ((temperature * neutrons_emitted) < 500000):
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    # porcentaje = ((voltage* current)/theoretical_max_power)*100
    # if porcentaje >= 80:
    #     return 'green'
    # elif porcentaje < 80 or porcentaje >= 60:
    #     return 'orange'
    # elif porcentaje < 50 or porcentaje >= 30:
    #     return 'red'
    # elif porcentaje < 30:
    #     return 'black'

    efficiency = ((voltage * current) / theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # prod = temperature * neutrons_produced_per_second
    # if (prod/threshold) < 0.4:
    #     return "LOW"
    # elif threshold * 0.9 <= prod <= threshold * 1.1:
    #     return "NORMAL"
    # return "DANGER"
    prod = temperature * neutrons_produced_per_second
    if prod < (threshold*0.9):
        return "LOW"
    elif threshold * 0.9 <= prod <= threshold * 1.1:
        return "NORMAL"
    return "DANGER"

