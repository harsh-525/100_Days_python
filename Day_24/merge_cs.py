import os
import pandas as pd
import glob

path = '/Users/harshbharath/Documents/Python/sample_csv/sales_csv'

os.chdir(path)
extension = "csv"

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

