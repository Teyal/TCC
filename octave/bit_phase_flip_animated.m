function rho = bit_phase_flip (rho, p, interv = .001, steps = 0.1)
  base_matrices
  
  rho_original = rho;
  for j = [0 : steps : p]
    rho = rho_original;
    e0 = sqrt(j)   * Id;
    e1 = sqrt(1-j) *  Y;
    
    for i = 1 : length(rho)
      rho{i} = e0*rho{i}*e0' + e1*rho{i}*e1';
    endfor
    plot_bloch(rho);
    pause (interv);
  endfor
endfunction