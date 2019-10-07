# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample

import flatbuffers

class Weapon(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWeapon(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Weapon()
        x.Init(buf, n + offset)
        return x

    # Weapon
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Weapon
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Weapon
    def Damage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def WeaponStart(builder): builder.StartObject(2)
def WeaponAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def WeaponAddDamage(builder, damage): builder.PrependInt16Slot(1, damage, 0)
def WeaponEnd(builder): return builder.EndObject()
