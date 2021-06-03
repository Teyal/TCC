function rho = depolarization(rho, p)
  base_matrices
  e0 = sqrt(1- 3*p/4) * Id;
  e1 = sqrt(p/4)      * X;
  e2 = sqrt(p/4)      * Y;
  e3 = sqrt(p/4)      * Z;

  for i = 1 : length(rho)
    rho{i} = e0*rho{i}*e0' + e1*rho{i}*e1' + e2*rho{i}*e2' + e3*rho{i}*e3';
  end
  
endfunction