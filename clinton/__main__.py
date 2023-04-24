import argparse
import os
import shutil

from clinton.process import process_file


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_files", nargs="+", help="Input files")
    ap.add_argument("-d", "--out-dir")
    ap.add_argument("-p", "--print-text", action="store_true", help="Print text")
    args = ap.parse_args()
    out_dir = args.out_dir
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    for filename in args.input_files:
        res = process_file(filename, print_text=args.print_text)
        if out_dir:
            new_filename = os.path.join(out_dir, res.get_new_filename())
            shutil.copyfile(filename, new_filename)
            print(f"Copied {filename} to {new_filename}")
        else:
            print(res.to_dict())


if __name__ == "__main__":
    main()
