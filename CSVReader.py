import csv


class CSVReader:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:  # each row is (value [delim] value [delim] etc...)
                row["platforms"] = row["platforms"].split(';')
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')  # formatted string literal
                    line_count += 1
                else:
                    print(f'{row["name"]}')
                    line_count += 1


reader = CSVReader("steam.csv")
reader.read_file()
