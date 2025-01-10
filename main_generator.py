import argparse
from datagenerator.generator import generate_data

parser = argparse.ArgumentParser(
    prog='File Data Generator',
    description='Generate daily Data')


parser.add_argument('-dd', '--desired_dir')
parser.add_argument('-n', '--number_of_id', default=1000)
parser.add_argument('-d', '--day')

args = parser.parse_args()


generate_data(desired_dir=args.desired_dir, day=args.day,
              number_of_id=int(args.number_of_id))
