register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' USING TextLoader as (line:chararray);

-- raw = LOAD 'cse344-test-file' USING TextLoader as (line:chararray);
-- raw = LOAD 'btc-2010-chunk-000' USING TextLoader as (line:chararray);

tuples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

subjects = group tuples by (subject) PARALLEL 50;

count_by_subjects = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

subjects_by_count = group count_by_subjects by (count) PARALLEL 50;

histogram = foreach subjects_by_count generate flatten($0), COUNT($1) as histogram_count PARALLEL 50;

D_GROUP = GROUP histogram ALL;
D_COUNT = FOREACH D_GROUP GENERATE COUNT(histogram);

store D_COUNT into 'counted-histogram' using PigStorage();
