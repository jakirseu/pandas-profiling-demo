import pandas as pd
import pandas_profiling

# load data
train_data = pd.read_csv("data/train.csv")

profile = train_data.profile_report(title='Pandas Profiling Report')
profile.to_file(output_file="output.html")



