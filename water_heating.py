def convert_volume(volume):
    right_volume = volume / 1000
    return right_volume


materials = ['Алюминий', 'Сталь', 'Чугун', 'Титан']

boilers_conductivity = {
                        'Алюминий': 920,
                        'Сталь': 500,
                        'Чугун': 540,
                        'Титан': 530
                        }


def main(boiler_index, boiler_mass, start_temp, burner_power, water_volume):

    boiler_conductivity = boilers_conductivity[boiler_index]

    boiler_heat = boiler_conductivity * boiler_mass * (100-start_temp)

    water_heat = 4200 * water_volume * (100-start_temp)

    heat = boiler_heat + water_heat

    useful_heat = heat * 2.2

    time = (useful_heat / (burner_power*1000)) / 60

    return time
