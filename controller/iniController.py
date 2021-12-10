from pathlib import Path

from controller import argsController, loggerController
from model import iniModel

path_config = iniModel.ini("./data/images", "./data/output")
args = argsController.get_args()


def inizialize():
    if '-i' in args or '--input' in args:
        if '-i' in args:
            path = args.index('-i') + 1
        elif '--input' in args:
            path = args.index('--input') + 1

        if not Path(args[path]).is_dir():
            loggerController.add_log(f"[Error] An error occurred while running the ini controller.")
            loggerController.add_log(f"[Error] The path {args[path]} is not valid.")
            loggerController.add_log(f"[Error] The program will be closed.")
            loggerController.exit_application();

        path_config.set_input_path(args[path])

    if '-o' in args or '--output' in args:
        if '-o' in args:
            path = args.index('-o') + 1
        elif '--output' in args:
            path = args.index('--output') + 1

        print(args[path])

        Path(args[path]).mkdir(parents=True, exist_ok=True)

        path_config.set_output_path(args[path])


def get_input_path():
    return path_config.get_input_path()


def get_output_path():
    return path_config.get_output_path()


inizialize()
