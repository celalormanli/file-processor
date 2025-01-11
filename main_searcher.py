import argparse
from datasearcher.searcher import search_data


def create_s_data(args_data):
    s_data = {
        "ids": args_data.ids,
        "attributes": {}
    }
    if args_data.attributes:
        for data in args_data.attributes:
            datas = data.split("=")
            s_data["attributes"][datas[0]] = datas[1]
    return s_data


parser = argparse.ArgumentParser(
    prog="File Data Searcher",
    description="Search Data from last 10 days")

parser.add_argument("-i", "--ids", nargs="+",
                    help="add values ​​separated by spaces. Example: -i 111 wqwq 3232", default=[])
parser.add_argument("-a", "--attributes", nargs="+",
                    help="add keys and values ​​separated by spaces like key=value. Example: -i key1=value1 key2=value1 key3=value1")
parser.add_argument("-p", "--processes", default=1, type=int)
parser.add_argument("-dd", "--desired_dir")

args = parser.parse_args()
s_data = create_s_data(args)

search_data(s_data=s_data, processes=args.processes,
            desired_dir=args.desired_dir)
