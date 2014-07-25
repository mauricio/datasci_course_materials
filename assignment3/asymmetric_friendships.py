import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  mr.emit_intermediate("-".join(sorted(record)), record)

def reducer(key, list_of_values):
  if len(list_of_values) == 1:
    record = list_of_values[0]
    mr.emit((record[1], record[0]))
    mr.emit((record[0], record[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
