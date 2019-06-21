# This script converts the directory names in ldcts files to the relevant directory names in the instance.

import pandas as pd
import argparse

def convert(args):
    dataset = args.dataset
    df = pd.read_csv(dataset+'.ldcts',delim_whitespace=True,header=None)
    if ',' in df.iloc[0,1]:
        dirs = [s.split(',')[0] for s in df[1].tolist()]
        fnames = [s.split('/')[-1] for s in dirs]
        controls = [s.split(',')[1] for s in df[1].tolist()]
        cnames = [s.split('/')[-1] for s in controls]
        newdirs = ['/mnt/data/'+dataset+'/'+s for s in fnames]
        newcontrols = ['/mnt/data/'+dataset+'/'+s for s in cnames]
        df[1] = [','.join(x) for x in zip(newdirs,newcontrols)]
    else:
        dirs = df[1].tolist()
        fnames = [s.split('/')[-1] for s in dirs]
        newdirs = ['/mnt/data/'+dataset+'/'+s for s in fnames]
        df[1] = newdirs
    df.to_csv(dataset+'_dsub.ldcts',sep='\t',header=False,index=False)
    return

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset')
    args = parser.parse_args()

    convert(args)
