import argparse
parser = argparse.ArgumentParser(prog='MyPyTalks',description='',epilog='Command Line Args')
parser.add_argument('-e', '--env')
parser.add_argument('-m', '--mode')
args, unknown = parser.parse_known_args()
import os
os.environ["ENV"] = args.env
print("Using environment file-->" + args.env)
from dotenv import load_dotenv
import os
load_dotenv(os.environ["ENV"])


def Main():
    if args.mode == "console":
        from MyPyTalks.PyTalk import Main as CMain
        CMain()
    else:
        from MyPyTalks.UiChat import Main as UMain
        UMain()


if __name__ == "__main__":
    Main()