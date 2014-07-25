import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  #[document_id, text]
  document_id = record[0]
  words = set(record[1].split(" "))
  for w in words:
    mr.emit_intermediate(w, document_id)

def reducer(key, list_of_values):
  mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
