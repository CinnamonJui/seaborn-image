import inspect

from palettable.cartocolors.sequential import *
from palettable.cmocean.sequential import *
from palettable.colorbrewer.sequential import *
from palettable.scientific.sequential import *

_CMAP_QUAL = {
    "acton": Acton_20,
    "davos": Davos_20,
    "devon": Devon_20,
    "oslo": Oslo_20,
    "tokyo": Tokyo_20,
    "nuuk": Nuuk_20,
    "lapaz": LaPaz_20,
    "lajolla": LaJolla_20,
    "imola": Imola_20,
    "blue": Blues_9_r,
    "bugn": BuGn_9_r,
    "gnbu": GnBu_9_r,
    "bupu": BuPu_9_r,
    "green": Greens_9_r,
    "purple": Purples_9_r,
    "orrd": OrRd_9_r,
    "grey_r": Greys_9,
    "gray_r": Greys_9,
    "orange": Oranges_9_r,
    "pubu": PuBu_9_r,
    "pubugn": PuBuGn_9_r,
    "purd": PuRd_9_r,
    "rdpu": RdPu_9_r,
    "red": Reds_9_r,
    "ylgn": YlGn_9_r,
    "ylgnbu": YlGnBu_9_r,
    "ylorbr": YlOrBr_9_r,
    "ylorrd": YlOrRd_9_r,
    "deep": Deep_20_r,
    "dense": Dense_20_r,
    "gray": Gray_20,
    "ice": Ice_20,
    "haline": Haline_20,
    "solar": Solar_20,
    "thermal": Thermal_20,
    "tempo": Tempo_20_r,
    "ocean": Tempo_20_r,
    "speed": Speed_20_r,
    "ocean-green": Speed_20_r,
    "brown": Turbid_20_r,
    "blugrn": BluGrn_7,
    "grnblu": BluGrn_7_r,
    "mint": Mint_7_r,
    "darkmint": DarkMint_7_r,
    "emerald": Emrld_7_r,
    "magenta": Magenta_7_r,
    "teal": Teal_7_r,
    "teal-green": TealGrn_7_r,
    "sunset-dark": SunsetDark_7_r,
    "sunset": Sunset_7_r,
}
