#Script to select by location to export shapefiles
import os
import arcpy

#Set inputs***************************************************************************************************

#Input folder of reference shapefiles
arcpy.env.workspace = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\GIS_Data\SF_SHPs"

#Shapefile used to select reference shapefiles
search_shp = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\GIS_Data\Point_of_Interest.shp"

#Set location for output of geoprocessing tools
output_folder = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Output_Folder"

#Search distance
search_dist = "1 MILE"

#*************************************************************************************************************

#Make variable to isolate starting point shapefile name
loc_analysis_name = search_shp.split('\\')[-1]

#Make variable to create new folder
location_analysis_fld = os.path.join(output_folder, 'Location_Analysis_' + loc_analysis_name[:-4])

#Use os library to create a new folder to export our selected shapefiles
print('Creating output folder')
os.mkdir(location_analysis_fld)

#Set overwrite output to true so we can overwrite feature layers we create
arcpy.env.overwriteOutput = True

#Get list of the shapefiles that we want to select from
shp_list = arcpy.ListFeatureClasses()

for shp in shp_list:
    print('Selecting shps near', shp)
    #Create temporary feature layer
    arcpy.MakeFeatureLayer_management(shp, "flyr")
    
    #Select feature layer by distance to input point
    arcpy.SelectLayerByLocation_management ("flyr", "WITHIN_A_DISTANCE", search_shp, search_dist)
    
    #Export the selected features to a shapefile in the output folder
    arcpy.FeatureClassToFeatureClass_conversion("flyr", location_analysis_fld, shp[:-4] + '_' + loc_analysis_name)
