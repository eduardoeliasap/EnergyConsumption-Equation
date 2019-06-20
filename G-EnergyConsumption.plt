reset
set terminal postscript eps enhanced color solid linewidth 3.8 font 'Helvetica, 15'
set grid
set xlabel "hop (s)"  
set ylabel "averege power consumption in joule"
set yrange[0:0.020]
set pointsize 1.5
set key right box opaque
set output 'EquationConsumption.eps'
plot "resultsNS.txt" using 1:2 t"Simulation results" with linespoints lc 8, "resultsEquation.txt" using 1:2 t"Equation results" with linespoints lc 7
unset output;
