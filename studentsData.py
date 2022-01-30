import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
data=df["math score"].to_list()

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)

print("Mean, Median and Mode of data is {}, {} and {} respectively".format(mean,median,mode))

std_deviation=statistics.stdev(data)

fig=ff.create_distplot([data],["math score"], show_hist=False)
fig.show()

first_stdev_start,first_stdev_end=mean-std_deviation,mean+std_deviation
list_of_data_within_one_stdev=[result for result in data if result>first_stdev_start and result<first_stdev_end]
print("{}% of data lies within one standard deviation".format(len(list_of_data_within_one_stdev)*100.0/len(data)))

second_stdev_start,second_stdev_end=mean-(2*std_deviation),mean+(2*std_deviation)
list_of_data_within_two_stddev=[result for result in data if result>second_stdev_start and result<second_stdev_end]
print("{}% of data lies within two standard deviation".format(len(list_of_data_within_two_stddev)*100.0/len(data)))

third_stdev_start,third_stdev_end=mean-(3*std_deviation),mean+(3*std_deviation)
list_of_data_within_three_stddev=[result for result in data if result>third_stdev_start and result<third_stdev_end]
print("{}% of data lies within three standard deviation".format(len(list_of_data_within_three_stddev)*100.0/len(data)))


