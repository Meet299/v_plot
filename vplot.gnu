
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
