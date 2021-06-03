function plot_bloch (rho) #TODO add default argument with color
  [fx, fy, fz] = expected_value(rho);
  n = sqrt(size(fx))(2);
  for i = 1:n
    for j = 1:n
    fxi(i,j) = fx(i+(j-1)*n);
    fyi(i,j) = fy(i+(j-1)*n); 
    fzi(i,j) = fz(i+(j-1)*n);  
    end
  end
  surf(fxi, fyi, fzi);
  axis equal
  xlabel("x")
  ylabel("y")
  zlabel("z")
  axis([-1 1 -1 1 -1 1])
end