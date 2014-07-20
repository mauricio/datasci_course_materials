# CREATE TABLE Frequency (
# docid VARCHAR(255),
# term VARCHAR(255),
# count int,
# PRIMARY KEY(docid, term));

select f1.term, f1.count, f2.count from Frequency f1, Frequency f2 where f1.docid = "10080_txt_crude" AND f2.docid = "17035_txt_earn" AND f1.term = f2.term;

select a.row_num, b.col_num, sum(a.value * b.value) from a, b where (a.col_num = b.row_num) group by a.row_num, b.col_num;

select a.docid, b.docid, sum(a.count * b.count) from keyword_search a, keyword_search b where (a.term = b.term) and  a.docid != b.docid and b.docid = 'q' group by a.docid order by sum(a.count * b.count);

select a.docid, b.docid, sum(a.count * b.count) from Frequency a, Frequency b where (a.term = b.term) and  a.docid = "10080_txt_crude" AND b.docid = "17035_txt_earn" group by a.docid, b.docid;

     | april | ended | inc | mln | net | profit | reuter | six |
doc1 | 1     | 1     | 1   | 2   | 1   | 1      | 1      | 1   |
doc2 | 2     | 1     | 1   | 3   | 3   | 4      | 4      | 1   |

        | doc1 | doc2 |
 april  | 1    | 2    |
 ended  | 1    | 1    |
 inc    | 1    | 1    |
 mln    | 2    | 3    |
 net    | 1    | 3    |
 profit | 1    | 4    |
 reuter | 1    | 1    |
 six    | 1    | 1    |

1|1|5
1|2|3
1|3|3
1|4|8
1|5|7
1|6|9
1|7|3
1|8|3
2|1|3
2|2|2
2|3|2
2|4|5
2|5|4
2|6|5
2|7|2
2|8|2
3|1|3
3|2|2
3|3|2
3|4|5
3|5|4
3|6|5
3|7|2
3|8|2
4|1|8
4|2|5
4|3|5
4|4|13
4|5|11
4|6|14
4|7|5
4|8|5
5|1|7
5|2|4
5|3|4
5|4|11
5|5|10
5|6|13
5|7|4
5|8|4
6|1|9
6|2|5
6|3|5
6|4|14
6|5|13
6|6|17
6|7|5
6|8|5
7|1|3
7|2|2
7|3|2
7|4|5
7|5|4
7|6|5
7|7|2
7|8|2
8|1|3
8|2|2
8|3|2
8|4|5
8|5|4
8|6|5
8|7|2
8|8|2

create view keyword_search as SELECT * FROM frequency UNION SELECT 'q' as docid, 'washington' as term, 1 as count  UNION SELECT 'q' as docid, 'taxes' as term, 1 as count UNION SELECT 'q' as docid, 'treasury' as term, 1 as count;
