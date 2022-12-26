# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_rules.krb'):
           [1672063604.3890188, 'bc_rules_bc.py'],
         ('', '', 'facts.kfb'):
           [1672063604.3994815, 'facts.fbc'],
        },
        compiler_version)

