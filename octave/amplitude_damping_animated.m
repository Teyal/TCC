function rho = amplitude_damping_animated(rho, gamma, interv = 0.01, steps = 0.1)
  
  rho_original = rho;
  for j = [0 : steps : gamma]
    rho = rho_original;
    
    e0 = [1             0;
          0 sqrt(1-j)];
    e1 = [0   sqrt(j);
          0             0];
    
    for i = 1 : length(rho)
      rho{i} = e0*rho{i}*e0' + e1*rho{i}*e1';
    endfor
    plot_bloch(rho);
    pause (interv);
  endfor
endfunction
