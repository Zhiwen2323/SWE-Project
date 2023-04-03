
import re
from util import load_data_from_s3, write_data_to_s3


def clean_data(input):
    # Remove trailing whitespace from each line
    output_cleaned = "\n".join([line.rstrip() for line in input.split("\n")])

    # Replace occurrences of "page" followed by a number with a single space character
    output_cleaned = re.sub(r"(?i)page\s+\d+", " ", output_cleaned)

    return output_cleaned


def main():
    # load raw data from s3 at s3://zhiwenswe/Harry_Potter/
    raw_data = load_data_from_s3()

    # clean the data
    cleaned_data = clean_data(raw_data)

    # write cleaned data to s3
    write_data_to_s3(cleaned_data)


if __name__ == '__main__':
    main()