def maxima_contaminacio(filename):
    fitxer = open(filename, "r")
    fitxer_lines = fitxer.readlines()
    max_value = -1

    for lines in fitxer_lines:
        current_lines = lines.split(";")
        if max_value < int(current_lines[2]):
            max_value = int(current_lines[2])
            max_value_time = current_lines[1]

    print(f"tiempo: {max_value_time}, el volumen maximo es {max_value}")
    fitxer.close()


def max_noise_threshold(filename):
    fitxer = open(filename, "r")
    fitxer_lines = fitxer.readlines()
    limit_level_morning = 700
    limit_level_night = 600

    for lines in fitxer_lines:
        current_lines = lines.split(";")
        time = current_lines[1].split(":")
        if 7 < int(time[0]) < 23:
            if int(current_lines[2]) > limit_level_morning:
                print(current_lines[1], current_lines[2])
        else:
            if int(current_lines[2]) > limit_level_night:
                print(current_lines[1], current_lines[2])


maxima_contaminacio("9808dies1a3.csv")
max_noise_threshold("9808dies1a3reduit.csv")
