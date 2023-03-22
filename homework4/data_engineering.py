
from util import load_data_from_s3, write_data_to_s3


def clean_data(input):
    # TODO takes a string as input, removes any trailing whitespace from each line of the string,
    #  and replaces any occurrences of the word "page" (in various capitalization and spacing forms)
    #  followed by a number with a single space character.
    output_cleaned = ""
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