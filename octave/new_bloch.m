function rho = new_bloch()
  [rx,ry,rz] = sphere(20);
  rho = bloch_sphere(rx,ry,rz);
endfunction
