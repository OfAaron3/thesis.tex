from lightweaver.fal import Falc82 as f82
import lightweaver as lw
import matplotlib.pyplot as plt

t=lw.fal.Falc82().temperature
rho=lw.DefaultAtomicAbundance.massPerH*lw.Amu*lw.fal.Falc82().nHTot
#p=((f82().nHTot+f82().ne)*1.380650e-34*t)/10

fig, ax=plt.subplots(tight_layout=True)
ax2=ax.twinx()

ax.semilogy(f82().z/1e3, t, c='C0')
ax.set_xlabel('Height [km]')
ax.set_ylabel('Temperature [K]')#, c='C0')
ax2.semilogy([0,0],[10e-13,10e-13], c='C0', label='Temperature')
ax2.semilogy(f82().z/1e3, rho, c='C1', label='Mass Density')
ax2.set_ylabel('Mass Density [kg$~$m$^{-3}$]')#, c='C1')
plt.title("Temperature and Mass Density Structure of the Solar Atmosphere")
plt.legend(loc='upper center')
plt.show()
