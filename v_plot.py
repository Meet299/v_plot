import sys
from collections import defaultdict
import gzip

f_length=[]
matrix=[]
matrix_count=defaultdict(lambda:defaultdict(int))

file='mapped.bed.gz' 
output_file='v_plot_data.tsv'

file_data=[]
with gzip.open(file,'rt') as read_file:
    for line in read_file:
        columns=line.strip().split("\t")

        gene_start = int(columns[2])
        gene_end = int(columns[3])
        #gene_length = gene_end - gene_start
        gene_avg=(gene_end+gene_start)/2
       # r_gene_avg= round(gene_avg)

        fragment_start= int(columns[8])
        fragment_end= int(columns[9])
        fragment_avg = (fragment_end + fragment_start)/2
       # r_fragment_avg = round(fragment_avg)

        offset = fragment_avg - gene_avg
        r_offset=round(offset)
        fragment_length=fragment_end - fragment_start 

        if -500 <= offset <= 500:
            matrix_count[fragment_length][offset] += 1
            if fragment_length not in f_length:
                f_length.append(fragment_length)

for length in f_length:
    for offset in range(-500,500):
        count = matrix_count[length][offset]    
        if count > 0:
            matrix.append((offset,length,count))


with open(output_file, 'w') as output_f:
    for values in matrix:
        output_f.write(f"{values[0]}\t{values[1]}\t{values[2]}\n")  # Write in TSV format

# Gnuplot commands as a string
gnuplot_script = """
set terminal pngcairo enhanced font "Arial,14" size 2000,1800
set output 'vplot.png'
set title "V Plot - Gene Fragments" font "Arial,18"
set xlabel 'Offset(bp)' font "Arial,16"
set ylabel 'Gene Fragment Length (bp)' font "Arial,16"
set xrange [-500:500]
set yrange [0:*]
set grid lw 0.5 lc rgb "gray"
set border lw 1.5

set palette defined (0 "white", 1 "blue", 2 "black", 3 "yellow",4 "red")
set cblabel "Frequency" font "Arial,14"
set cbrange[0:200]
set cbtics font "Arial,12"

set xtics font "Arial,14"
set ytics font "Arial,14"

set pointsize 2

plot 'v_plot_data.tsv' using 1:2:3 with points pointtype 7 pointsize 1.5 palette title 'Gene Fragments'
"""

with open('vplot.gnu', 'w') as gnuplot_file:
    gnuplot_file.write(gnuplot_script)

print("Run the following command in your terminal to generate the plot:")
print(" gnuplot vplot.gnu")
