#!/usr/bin/env python

import subprocess
import os

SUMSTAT = os.environ['SUMSTAT']
BASELINE = os.environ['BASELINE']
OUT = os.environ['OUT']
LDCTS = os.environ['LDCTS']
WEIGHTS = os.environ['WEIGHTS']
DATASET = os.environ['DATASET']


subprocess.call(['mkdir','/mnt/data/results/'])
subprocess.call(['mkdir','/mnt/data/ss/'])
subprocess.call(['mkdir','/mnt/data/baselineLD/'])
subprocess.call(['mkdir','/mnt/data/'+DATASET+'/'])
subprocess.call(['mkdir','/mnt/data/weights/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/data/sumstats_formatted/UKB_460K.disease_T2D.sumstats','/mnt/data/ss/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/data/annots_1000G_EUR/baselineLD_v2.2/baselineLD.*','/mnt/data/baselineLD/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/data/annots_1000G_EUR/'+DATASET+'/*','/mnt/data/'+DATASET+'/'])
subprocess.call(['gsutil','-m','cp','gs://ran/functionally_informed_fm/data/annots_1000G_EUR/weights_noMHC/weights.hm3_noMHC.*','/mnt/data/weights/'])


subprocess.call(['/home/ldscore/ldsc-kt_exclude_files/ldsc.py',
    '--h2-cts',SUMSTAT,
    '--ref-ld-chr',BASELINE,
    '--out',OUT,
    '--ref-ld-chr-cts',LDCTS,
    '--w-ld-chr',WEIGHTS])

subprocess.call(['gsutil','-m','cp',OUT+'*','gs://ran/functionally_informed_fm/results/UKBB_T2D_ldcts/'])
