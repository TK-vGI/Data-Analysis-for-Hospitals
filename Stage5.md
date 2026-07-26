# Stage 5/5: Visualize it!
## Description
Are you ready to catch sight of your data?

Graphics are arguably the most accessible way to represent the data and its structure. Sometimes, it can help to find  
the main data patterns and deviations. We will use data visualization methods to conclude our dataset.

In the last stage, you need to create data visualization to answer the following questions:
1. What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following  
   age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
2. What is the most common diagnosis among patients in all hospitals? Create a pie chart.
3. Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the  
   gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is  
   required to answer this question.

**Tip**: To answer the last question think about specializations of the hospitals in the dataset and the unit of measurement
of height.

Please note that the answers are independent of each other.

At this stage, use `pandas` visualization tools, `seaborn` or `matplotlib`.  
For second plot use `pandas` or `matplotlib`, this is necessary for the tests to run correctly.

## Objectives
Use the DataFrame from the previous stage. The fifth stage requires completing one step:

Answer questions 1-3. Output the answers in the specified format. The answers to the first two questions should be  
formatted as in the examples. No special form is required to answer the third question

If you have corrupted CSV files, please [download them](files.zip) and unzip in your working directory.

## Example
The input is 3 CSV files, `test/general.csv`, `test/prenatal.csv`, and `test/sports.csv`.

The output:
(The following answers are given for reference only, the actual answers might be different)

```
The answer to the 1st question: 0-15
The answer to the 2nd question: flu
The answer to the 3rd question: It's because...
```