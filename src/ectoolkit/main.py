import os.path as path

class Record:
    def __init__(self) -> None:
        pass


def parse_csv_probe_output(filename: str) -> list[Record]:
    pass

def main():
    # Read input file name
    input_file = "../local.data/local.input"

    if not path.isfile(input_file):
        print("Provided input file path: {} does not point to a valid file", input_file)
        return 1
    
    # Read output directory
    output_dir = "../local.data"

    if not path.isdir(output_dir):
        print("Provided output directory path: {} does not point to a valid directory", output_dir)
        return 1

    

    # Read & parse input file

    # Pass records to visualizer

    # Run visualizer 

    # (Optional) Print some summary 

    pass


if __name__ == "__main__":
    main()
