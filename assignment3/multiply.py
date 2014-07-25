import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
# [matrix, i, j, value]

columns = range(0,5)

def mapper(record):
  matrix, i, j, value = record
  if matrix == "a":
    mr.emit_intermediate(i, record)
  else:
    for row in columns:
      mr.emit_intermediate(row, record)

def reducer(key, list_of_values):
  rows = []
  cols = {}
  for col in columns:
    cols[col] = []

  for row in list_of_values:
    if row[0] == "a":
      rows.append(row)
    else:
      cols[row[2]].append(row)

  for col_key, column_rows in cols.iteritems():
    sum = 0
    for col_value in column_rows:
      for row_value in rows:
        if row_value[2] == col_value[1]:
          sum += row_value[3] * col_value[3]
    mr.emit((key, col_key, sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
