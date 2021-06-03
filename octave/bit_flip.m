function rho = bit_flip (rho, p)
  base_matrices
  e0 = sqrt(p)   * Id;
  e1 = sqrt(1-p) * X;
  
  for i = 1 : length(rho)
    rho{i} = e0*rho{i}*e0' + e1*rho{i}*e1';
  end
endfunction