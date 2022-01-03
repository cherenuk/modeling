# boiler_index = int(input(material_text))
    # boiler_mass = int(input(mass_text))
    #
    # start_temp = int(input(temp_text))
    #
    # burner_power = int(input(burner_text))
    #
    # water_volume = int(input(volume_text))


def convert_volume(volume):
    right_volume = volume / 1000
    return right_volume


# [920, 500, 540, 530]


boilers_conductivity = {
                        'Алюминий': 920,
                        'Сталь': 500,
                        'Чугун': 540,
                        'Титан': 530
                        }

title = '---- Кипение воды на газовой горелке ----'
material_text = '''
Из какого материала сделан котелок/чайник:
1)Алюминий
2)Сталь
3)Чугун
4)Титан
'''
materials = ['Алюминий', 'Сталь', 'Чугун', 'Титан']

mass_text = 'Масса котелка/чайника(кг): '

temp_text = 'Начальная температура воды или котла/чайника(C°): '

burner_text = 'Мощность горелки(кВт): '

volume_text = 'Объем воды(л): '


def main(boiler_index, boiler_mass, start_temp, burner_power, water_volume):
    print(title)

    boiler_conductivity = boilers_conductivity[boiler_index]

    boiler_heat = boiler_conductivity * boiler_mass * (100-start_temp)

    water_heat = 4200 * water_volume * (100-start_temp)

    heat = boiler_heat + water_heat

    useful_heat = heat * 2.2

    time = (useful_heat / (burner_power*1000)) / 60

    return time


if __name__ == '__main__':
    main(1, 1, 1, 1, 1)






