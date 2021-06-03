function rho = amplitude_damping(rho, gamma)
  e0 = [1             0;
        0 sqrt(1-gamma)];
  e1 = [0   sqrt(gamma);
        0             0];
        z
  for i = 1 : length(rho)
    rho{i} = e0*rho{i}*e0' + e1*rho{i}*e1';
  endfor
endfunction
