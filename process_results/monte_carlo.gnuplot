plot  "monte_carlo.dat" using 1:2 title 'Monte-Carlo' with linespoints, \
      "monte_carlo.dat" using 1:3 title 'Monte-Carlo-Threaded' with linespoints
set yrange [0:2650]
set xrange [10:42]
set xlabel "Number of nodes"
set ylabel "Time (seconds)"
set term png
set output "monte_carlo_runtime.png"
set size 1.0, 0.8
replot