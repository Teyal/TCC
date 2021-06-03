function rho = bloch_sphere(x, y, z)
  base_matrices
  i = 1;
  rho = {};
  for r = transpose([x(:) y(:) z(:)])
    rho{i++} = (eye(2)+r(1)*X+r(2)*Y+r(3)*Z)/2;
  end
end