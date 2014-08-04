-- raw = LOAD 'cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD 'btc-2010-chunk-000' USING TextLoader as (line:chararray);

tuples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

A = FILTER tuples BY subject matches
-- '.*business.*';
'.*rdfabout\\.com.*';

B = foreach A generate subject as subject2, predicate as predicate2, object as object2;

C = JOIN A
--  BY subject, B BY subject2;
BY object, B BY subject2;

D = distinct C parallel 50;

D_GROUP = GROUP D ALL;
D_COUNT = FOREACH D_GROUP GENERATE COUNT(D);

store D_COUNT into 'full-total-counts' using PigStorage();
