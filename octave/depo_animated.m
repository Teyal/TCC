function rho = depolarization_animated(rho, p, interv = .001, steps = 0.1)
  base_matrices
  
  rho_original = rho;
  for j = [0 : steps : p]
    rho = rho_original;
    e0 = sqrt(1- 3*j/4) * Id;
    e1 = sqrt(j/4)      * X;
    e2 = sqrt(j/4)      * Y;
    e3 = sqrt(j/4)      * Z;
    
    
    for i = 1 : length(rho)
      rho{i} = e0*rho{i}*e0' + e1*rho{i}*e1' + e2*rho{i}*e2' + e3*rho{i}*e3';
    endfor
    plot_bloch(rho);
    pause (interv);
  endfor
  
endfunction