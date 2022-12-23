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
         ('', '', 'facts.kfb'):
           [1671837096.394322, 'facts.fbc'],
         ('', '', 'questions.kqb'):
           [1671837096.3993146, 'questions.qbc'],
         ('', '', 'rules.krb'):
           [1671837096.4142733, 'rules_bc.py'],
        },
        compiler_version)

