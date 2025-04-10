student_dict = {
    "names" : ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie'],
    "scores" : [70, 65, 80, 89, 90, 95]
}

#normal for loop through the dict
for (key, val) in student_dict.items():
    print(key)
    print(val)
    """for i in val:
        print(i)"""

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame by iterrows() method
for (index, rows) in student_data_frame.iterrows():
    #print(rows)
    #print(rows.names)
    if rows.names == 'Alex':
        print(f"{rows.names} got the mark {rows.scores}")
