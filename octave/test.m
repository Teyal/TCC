rho = new_bloch();

##rho = erros/depolarization(rho, 0.7);
##rho = amplitude_damping(rho, 0.5);
plot_bloch (rho);


#rho = bit_flip_animated(rho,0.4);
#rho = bit_phase_flip_animated(rho,0.4);
#rho = phase_flip_animated(rho, 0.4);

