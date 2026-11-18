# Importez un module
import mon_module
resultat = mon_module.ma_fonction()

from mon_module import ma_fonction # importer des éléments spécifiques d'un module
resultat = ma_fonction()

# Créez et importez un package
import mon_package.mon_module # utiliser un module d'un package
resultat = mon_package.mon_module.ma_fonction()

