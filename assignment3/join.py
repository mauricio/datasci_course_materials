import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  order_id = record[1]
  mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
  order = None
  items = []
  for record in list_of_values:
    if record[0] == "order":
      order = record
    else:
      items.append(record)
  for item in items:
    mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
