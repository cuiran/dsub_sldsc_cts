#!/bin/bash

dsub \
    --provider google-v2 \
    --project encode-uk-biobank \
    --zones "us-east1-b" \
    --logging gs://ran/log/ldcts/ \
    --disk-size 100 \
    --machine-type n1-standard-4 \
    --image "gcr.io/ldscore-data/ldscore" \
    --script "run_ldcts.py" \
    --tasks "submit_list.tsv"
