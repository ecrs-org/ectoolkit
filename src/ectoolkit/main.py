import os
import os.path as path
import csv
import json

import numpy as np
import matplotlib.pyplot as plt

from records import *
from individual import Individual

EVENT_TYPE_NEW_GEN = 'new_gen'
EVENT_TYPE_INIT_GEN = 'init_gen'
EVENT_TYPE_NEW_BEST = 'new_best'
EVENT_TYPE_END = 'end'

def average_fitness_in_pop(population: list[Individual]) -> float:
    return np.average(list(map(lambda idv: idv.fitness, population)))

def plot_avg_fitness_in_pop(generation_records: list[tuple[int, int, list[Individual]]], axes: plt.Axes):
    first_gen = generation_records[0][1]
    last_gen = generation_records[-1][1]

    x_data = np.arange(first_gen, last_gen + 1, 1)
    y_data = [average_fitness_in_pop(record[2]) for record in generation_records]

    axes.plot(x_data, y_data)


def dispatch_record(record: list[str],
                    new_gen_list: list,
                    init_gen_list: list,
                    new_best_list: list,
                    end_list: list):
    # print(record)
    match record:
        case ['new_gen', dur, gen, *population]:
            print(EVENT_TYPE_NEW_GEN)
            print(type(population), len(population), type(population[0]))
            # raise ValueError
            population = json.loads(population[0])
            individuals = [Individual.from_json(idv_json) for idv_json in population]
            new_gen_list.append((int(dur), int(gen), individuals))
            raise ValueError

        case ['new_best', dur, gen, indiv]:
            print(EVENT_TYPE_NEW_BEST)

        case ['init_gen', *population]:
            print(EVENT_TYPE_INIT_GEN)

        case ['end', dur, gen, best, *population]:
            print(EVENT_TYPE_END)
            
        case _:
            raise ValueError(f"Unhandled record type: {record[0]}")



def parse_csv_probe_output(filename: str) -> list:
    new_gen_list = [ ]
    with open(filename, 'r') as input_file:
        reader = csv.reader(input_file, delimiter='|')

        # I assume here there are no headers
        for line in reader:
            dispatch_record(line, new_gen_list, None, None, None)
    
    return new_gen_list
            

def main():
    # Read input file name
    input_file = "local.data/local.input"

    if not path.isfile(input_file):
        print(f"Provided input file path: {input_file} does not point to a valid file")
        print(f"cwd: {os.getcwd()}")
        return 1
    
    # Read output directory
    output_dir = "local.data"

    if not path.isdir(output_dir):
        print(f"Provided output directory path: {output_dir} does not point to a valid directory")
        print(f"cwd: {os.getcwd()}")
        return 1

    individual = Individual([0, 0, 0], 42)

    print(json.dumps({
        "chromosome": [0.0, 1.0, 2.0],
        "fitness": 42
    })) 
    return

    # Read & parse input file
    new_gen_list = parse_csv_probe_output(input_file)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 7))

    plot_avg_fitness_in_pop(new_gen_list, axes)

    fig.show()

    # Pass records to visualizer

    # Run visualizer 

    # (Optional) Print some summary 

    pass


if __name__ == "__main__":
    main()
