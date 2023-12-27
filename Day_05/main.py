from dataclasses import dataclass
from tqdm import tqdm


def read_input():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


@dataclass
class objeto:
    seed: int = 0
    soil: int = 0
    fertilizer: int = 0
    water: int = 0
    light: int = 0
    temperature: int = 0
    humidity: int = 0
    location: int = 0


@dataclass
class objeto2:
    start: int = 0
    range: int = 0
    destination: int = 0


def parte_uno(lines):
    seeds = []
    stage = 0
    cambio_fase = False
    for line in lines:
        # line starts with "seeds"
        if line.startswith("seeds:"):
            for seed_num in line.split(":")[1].split(" "):
                if seed_num.isdigit():
                    seeds.append(objeto(int(seed_num), 0, 0, 0, 0, 0, 0, 0))
        elif line == "":
            continue
        elif line == "seed-to-soil map:":
            stage = 1
            cambio_fase = True
        elif line == "soil-to-fertilizer map:":
            stage = 2
            cambio_fase = True
        elif line == "fertilizer-to-water map:":
            stage = 3
            cambio_fase = True
        elif line == "water-to-light map:":
            stage = 4
            cambio_fase = True
        elif line == "light-to-temperature map:":
            stage = 5
            cambio_fase = True
        elif line == "temperature-to-humidity map:":
            stage = 6
            cambio_fase = True
        elif line == "humidity-to-location map:":
            stage = 7
            cambio_fase = True
        if cambio_fase:
            cambio_fase = False
            continue
        if stage == 1:
            soil_num = int(line.split(" ")[0])
            seed_num_start = int(line.split(" ")[1])
            seed_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if seed_num_start <= seed.seed < seed_num_start + seed_num_range:
                    seed.soil = soil_num + seed.seed - seed_num_start
                elif seed.soil == 0:
                    seed.soil = seed.seed
        elif stage == 2:
            fertilizer_num = int(line.split(" ")[0])
            soil_num_start = int(line.split(" ")[1])
            soil_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if soil_num_start <= seed.soil < soil_num_start + soil_num_range:
                    seed.fertilizer = fertilizer_num + seed.soil - soil_num_start
                elif seed.fertilizer == 0:
                    seed.fertilizer = seed.soil
        elif stage == 3:
            water_num = int(line.split(" ")[0])
            fertilizer_num_start = int(line.split(" ")[1])
            fertilizer_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if fertilizer_num_start <= seed.fertilizer < fertilizer_num_start + fertilizer_num_range:
                    seed.water = water_num + seed.fertilizer - fertilizer_num_start
                elif seed.water == 0:
                    seed.water = seed.fertilizer
        elif stage == 4:
            light_num = int(line.split(" ")[0])
            water_num_start = int(line.split(" ")[1])
            water_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if water_num_start <= seed.water < water_num_start + water_num_range:
                    seed.light = light_num + seed.water - water_num_start
                elif seed.light == 0:
                    seed.light = seed.water
        elif stage == 5:
            temperature_num = int(line.split(" ")[0])
            light_num_start = int(line.split(" ")[1])
            light_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if light_num_start <= seed.light < light_num_start + light_num_range:
                    seed.temperature = temperature_num + seed.light - light_num_start
                elif seed.temperature == 0:
                    seed.temperature = seed.light
        elif stage == 6:
            humidity_num = int(line.split(" ")[0])
            temperature_num_start = int(line.split(" ")[1])
            temperature_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if temperature_num_start <= seed.temperature < temperature_num_start + temperature_num_range:
                    seed.humidity = humidity_num + seed.temperature - temperature_num_start
                elif seed.humidity == 0:
                    seed.humidity = seed.temperature
        elif stage == 7:
            location_num = int(line.split(" ")[0])
            humidity_num_start = int(line.split(" ")[1])
            humidity_num_range = int(line.split(" ")[2])
            for seed in seeds:
                if humidity_num_start <= seed.humidity < humidity_num_start + humidity_num_range:
                    seed.location = location_num + seed.humidity - humidity_num_start
                elif seed.location == 0:
                    seed.location = seed.humidity
    return seeds


def parse_parte_dos(lines):
    seeds = []
    soils = []
    fertilizers = []
    waters = []
    lights = []
    temperatures = []
    humidities = []
    locations = []
    stage = 0
    cambio_fase = False
    for line in lines:
        # line starts with "seeds"
        if line.startswith("seeds:"):
            for idx, seed_num in enumerate(line.split(": ")[1].split(" ")):
                if seed_num.isdigit() and idx % 2 == 0:
                    seeds.append(objeto2())
                    seeds[-1].start = int(seed_num)
                elif seed_num.isdigit() and idx % 2 == 1:
                    seeds[-1].range = int(seed_num)
        elif line == "":
            continue
        elif line == "seed-to-soil map:":
            stage = 1
            cambio_fase = True
        elif line == "soil-to-fertilizer map:":
            stage = 2
            cambio_fase = True
        elif line == "fertilizer-to-water map:":
            stage = 3
            cambio_fase = True
        elif line == "water-to-light map:":
            stage = 4
            cambio_fase = True
        elif line == "light-to-temperature map:":
            stage = 5
            cambio_fase = True
        elif line == "temperature-to-humidity map:":
            stage = 6
            cambio_fase = True
        elif line == "humidity-to-location map:":
            stage = 7
            cambio_fase = True
        if cambio_fase:
            cambio_fase = False
            continue
        if stage == 1:
            soils.append(objeto2())
            soils[-1].destination = int(line.split(" ")[0])
            soils[-1].start = int(line.split(" ")[1])
            soils[-1].range = int(line.split(" ")[2])
        elif stage == 2:
            fertilizers.append(objeto2())
            fertilizers[-1].destination = int(line.split(" ")[0])
            fertilizers[-1].start = int(line.split(" ")[1])
            fertilizers[-1].range = int(line.split(" ")[2])
        elif stage == 3:
            waters.append(objeto2())
            waters[-1].destination = int(line.split(" ")[0])
            waters[-1].start = int(line.split(" ")[1])
            waters[-1].range = int(line.split(" ")[2])
        elif stage == 4:
            lights.append(objeto2())
            lights[-1].destination = int(line.split(" ")[0])
            lights[-1].start = int(line.split(" ")[1])
            lights[-1].range = int(line.split(" ")[2])
        elif stage == 5:
            temperatures.append(objeto2())
            temperatures[-1].destination = int(line.split(" ")[0])
            temperatures[-1].start = int(line.split(" ")[1])
            temperatures[-1].range = int(line.split(" ")[2])
        elif stage == 6:
            humidities.append(objeto2())
            humidities[-1].destination = int(line.split(" ")[0])
            humidities[-1].start = int(line.split(" ")[1])
            humidities[-1].range = int(line.split(" ")[2])
        elif stage == 7:
            locations.append(objeto2())
            locations[-1].destination = int(line.split(" ")[0])
            locations[-1].start = int(line.split(" ")[1])
            locations[-1].range = int(line.split(" ")[2])
    return seeds, soils, fertilizers, waters, lights, temperatures, humidities, locations


def search_min_loc_parte2(parse_parte_dos):
    seeds, soils, fertilizers, waters, lights, temperatures, humidities, locations = parse_parte_dos
    seed_min = objeto(location=10e10)
    for seed in seeds:
        for i in tqdm(range(seed.start, seed.start + seed.range)):
            soil = 0
            fertilizer = 0
            water = 0
            light = 0
            temperature = 0
            humidity = 0
            location = 0
            for soil_obj in soils:
                if soil_obj.start <= i < soil_obj.start + soil_obj.range:
                    soil = soil_obj.destination + i - soil_obj.start
                    break
                elif soil == 0:
                    soil = i
            for fertilizer_obj in fertilizers:
                if fertilizer_obj.start <= soil < fertilizer_obj.start + fertilizer_obj.range:
                    fertilizer = fertilizer_obj.destination + soil - fertilizer_obj.start
                    break
                elif fertilizer == 0:
                    fertilizer = soil
            for water_obj in waters:
                if water_obj.start <= fertilizer < water_obj.start + water_obj.range:
                    water = water_obj.destination + fertilizer - water_obj.start
                    break
                elif water == 0:
                    water = fertilizer
            for light_obj in lights:
                if light_obj.start <= water < light_obj.start + light_obj.range:
                    light = light_obj.destination + water - light_obj.start
                    break
                elif light == 0:
                    light = water
            for temperature_obj in temperatures:
                if temperature_obj.start <= light < temperature_obj.start + temperature_obj.range:
                    temperature = temperature_obj.destination + light - temperature_obj.start
                    break
                elif temperature == 0:
                    temperature = light
            for humidity_obj in humidities:
                if humidity_obj.start <= temperature < humidity_obj.start + humidity_obj.range:
                    humidity = humidity_obj.destination + temperature - humidity_obj.start
                    break
                elif humidity == 0:
                    humidity = temperature
            for location_obj in locations:
                if location_obj.start <= humidity < location_obj.start + location_obj.range:
                    location = location_obj.destination + humidity - location_obj.start
                    break
                elif location == 0:
                    location = humidity
            if location < seed_min.location:
                seed_min = objeto(i, soil, fertilizer, water, light, temperature, humidity, location)
    return seed_min


if __name__ == '__main__':
    input = read_input()
    seeds = parte_uno(input)
    print(0)
    min_seed = seeds[0]
    for seed in seeds:
        if seed.location < min_seed.location:
            min_seed = seed
    print(min_seed.location)

    parte_2_parsed = parse_parte_dos(input)
    seed_min_parte2 = search_min_loc_parte2(parte_2_parsed)
    print(seed_min_parte2)
