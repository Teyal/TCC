function [xx, yy, zz] = valor_esperado(rho)
  base_matrices
  
  xx = [];
  yy = [];
  zz = [];
  for i = 1 : length(rho)
    xx = [xx trace(X*rho{i})];
    yy = [yy trace(Y*rho{i})];
    zz = [zz trace(Z*rho{i})];
  end
endfunction