import win32com.client
import win32com.client.gencache as win32
import pythoncom

# speaker = win32com.client.Dispatch('ProductionControls.EquipmentStates')
# ocx_classid = '{9B118E36-CFF7-11D2-8132-00600803A49B}'
ocx_classid = '{206ECCA4-03F3-4EAE-90D0-E63790684611}'
ocx = win32.GetClassForProgID(ocx_classid)
o = ocx()
print(ocx)
# ocx.StartControls()


class Test:
    pass
test = Test()
print(test)
