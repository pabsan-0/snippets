import argparse

parser = argparse.ArgumentParser(description="Hello")

parser.add_argument("--poses", type=str, help="poses file for the valid split")
parser.add_argument("--rest", type=float, default=0, help="extra wait in between airsim API calls")
parser.add_argument("--random-z", action="store_true", help="whether to override poses with random z")

args = parser.parse_args()
