# -*- coding: utf-8 -*-
"""
Editted by Zongrui Dai
Email:dzr17723980497@gmail.com
The statistic of NGG,NGN target
"""


%cd D:/test
from Bio import SeqIO
import numpy as np
import pandas as pd

##基因组NGG的统计数据
input_file = open('GCF_000002775.4_Pop_tri_v3_genomic.fna','r')

AGG=[]
CGG=[]
GGG=[]
TGG=[]
Sum=[]
ID=[]
L=[]
from Bio import SeqIO
for seq in SeqIO.parse(input_file,"fasta"):
    name = seq.description
    A = seq.seq.count('AGG')
    C = seq.seq.count('CGG')
    G = seq.seq.count('GGG')
    T = seq.seq.count('TGG')
    l = len(seq.seq)
    AGG.append(A);
    CGG.append(C);
    GGG.append(G);
    TGG.append(T);
    Sum.append(np.sum([A,C,G,T]))
    L.append(l)
    ID.append(name)

d = np.array([ID,L,AGG,CGG,GGG,TGG,Sum])
d = pd.DataFrame(d)
d.to_csv('NGG.csv')



##基因组NGN的统计数据
input_file = open('GCF_000002775.4_Pop_tri_v3_genomic.fna','r')
Sum=[]
L=[]
ID=[]
from Bio import SeqIO
for seq in SeqIO.parse(input_file,"fasta"):
    name = seq.description
    A = seq.seq.count('AGG')
    C = seq.seq.count('CGG')
    G = seq.seq.count('GGG')
    T = seq.seq.count('TGG')
    A1 = seq.seq.count('AGA')
    C1 = seq.seq.count('CGA')
    G1 = seq.seq.count('GGA')
    T1 = seq.seq.count('TGA')
    A2 = seq.seq.count('AGC')
    C2 = seq.seq.count('CGC')
    G2 = seq.seq.count('GGC')
    T2 = seq.seq.count('TGC')
    A3 = seq.seq.count('AGT')
    C3 = seq.seq.count('CGT')
    G3 = seq.seq.count('GGT')
    T3 = seq.seq.count('TGT')
    l = len(seq.seq)
    Sum.append(np.sum([A,C,G,T,A1,C1,G1,T1,A2,C2,G2,T2,A3,C3,G3,T3]))
    L.append(l)
    ID.append(name)
d1 = np.array([ID,L,Sum])
d1 = pd.DataFrame(d1)
d1.to_csv('NGN.csv')










