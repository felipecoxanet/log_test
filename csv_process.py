import csv


def gera_csv(row, header, file_name):
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(header)
        for data in row:
            writer.writerow(data)
