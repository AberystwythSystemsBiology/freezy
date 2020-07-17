from enum import Enum


class EntityToStorageType(Enum):
    STBO = "Sample to Box"
    STDR = "Sample to Drawer"
    BODR = "Box to Drawer"
    DTSH = "Drawer to Shelf"
    STST = "Shelf to Storage"
    STSI = "Storage to Site"

class ColdStorageType(Enum):
    FRE = "Freezer"
    FRI = "Fridge"

class DrawerSizes(Enum):
    L = "Large"
    S = "Small"