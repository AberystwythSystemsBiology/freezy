from enum import Enum


class EntityToStorageType(Enum):
    STBO = "Sample to Box"
    STDR = "Sample to Drawer"
    DTSH = "Drawer to Shelf"
    STST = "Shelf to Storage"
    STSI = "Storage to Site"

class DrawerSizes(Enum):
    L = "Large"
    S = "Small"