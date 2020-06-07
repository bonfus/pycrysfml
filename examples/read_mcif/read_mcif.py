# coding: utf-8
try:
    from pycrsfml import Cfml_Io_Formats, Cfml_Atom_Typedef
except (ImportError, ModuleNotFoundError):
    import sys
    sys.path.append('../../src')
    from pycrsfml import Cfml_Io_Formats, Cfml_Atom_Typedef

cell, spg, atoms = Cfml_Io_Formats.readn_set_magnetic_structure_mcif('ScMnO3.mcif')

print(cell)
for i in range(atoms.natoms):
    print(atoms.atom[i])
