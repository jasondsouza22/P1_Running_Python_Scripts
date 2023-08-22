import arcpy

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P1_Running_Python_Scripts\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

# Performing buffer operations
#arcpy.analysis.Buffer("Wilson_Schools","Wilson_Schools_Buffer","500 meters")

arcpy.analysis.Buffer("Wilson_Schools","Wilson_Schools_Buffer_600","600 meters")
print("Process Completed")
