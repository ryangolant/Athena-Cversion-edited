import astropy.constants as c
import astropy.units as u
import numpy as np

def set_units(dunit=None,lunit=None,vunit=None,cgs=False,muH=1.4271):
    if dunit is None:
        dunit=muH*c.m_p/u.cm**3
    if vunit is None:
        vunit=1.0*u.km/u.s
    if lunit is None:
        lunit=c.pc

    units = {}
    units['muH'] = muH*c.m_p.cgs
    units['density'] = dunit.to('Msun/pc^3')
    units['velocity'] = vunit.to('km/s')
    units['length'] = lunit.to('pc')
    units['time'] = (lunit/vunit).to('Myr')
    units['pressure'] = (dunit*vunit**2).to('erg/cm**3')
    units['energy_density'] = (dunit*vunit**2).to('erg/cm**3')
    units['gravitational_potential'] = (vunit**2).to('km**2/s**2')
    units['number_density'] = (dunit/units['muH']).cgs
    units['magnetic_field'] = (np.sqrt(4*np.pi*dunit*vunit**2).cgs.value*u.Gauss).to('microGauss')
    units['temperature'] = 1.0*u.K
    units['mass'] = (dunit*lunit**3).to('Msun')
    units['Gcode'] = (c.G/dunit*(vunit/lunit)**2).cgs
    units['energy_flux'] = (units['mass']/units['time']**3).cgs

    if cgs:
        for k in units:
            units[k] = units[k].cgs

    return units
