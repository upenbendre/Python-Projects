# setting a current working  directory

getwd()

# setwd(C:/Documents and Settings/Data) 
# command to specify a working directory

# Read a CSV file

sample_csv <- read.csv("HR.csv")


# Find the attributes of the dataset

attributes (sample_csv)

# Mentioning the presence of Headers in the dataset

sample_csv <- read.csv("HR.csv", header = F)

print (sample_csv)

sample_csv <- read.csv ("HR.csv", header = T)

print (sample_csv)

# Missing Data Values

sample_table <- read.table("sample.txt", header = T)




