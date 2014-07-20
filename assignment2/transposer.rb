require 'sequel'

DB = Sequel.sqlite("simple-matrix.db")

[:a, :b].each do |table|
  DB.create_table! table do
    Fixnum :row_num
    Fixnum :col_num
    Fixnum :value
    primary_key([:row_num, :col_num])
  end
end

b = [
  [1, 2],
  [1,1],
  [1,1],
  [2,3],
  [1,3],
  [1,4],
  [1,1],
  [1,1],
]

a = [
  [1,1,1,2,1,1,1,1],
  [2,1,1,3,3,4,1,1]
]

def insert_matrix(table, items)
  items.each_with_index do |row, row_num|
    row.each_with_index do |item, column|
      table.insert( row_num: row_num + 1, col_num: column + 1, value: item )
    end
  end
end

insert_matrix(DB[:a], a)
insert_matrix(DB[:b], b)

#  select a.row_num, b.col_num, sum(a.value * b.value) from a, b where ((a.row_num = b.col_num OR a.row_num != b.col_num) AND a.col_num = b.row_num) group by a.row_num, b.col_num;
