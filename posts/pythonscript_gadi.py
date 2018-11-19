# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# pythonscript.py
# Created on: 2018-09-05 09:20:28.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: pythonscript <Road_buffer> <Cities_buffer_distance> <US_Boundaries> 
# Description: 
# ---------------------------------------------------------------------------

#### Importing the library (to know where commands come from) (Gadi) 

# Import arcpy module 
import arcpy


#### These buffers are calculating the same distance--10 miles(Gadi) 


# Script arguments
Road_buffer = arcpy.GetParameterAsText(0)
if Road_buffer == '#' or not Road_buffer:
    Road_buffer = "10 Miles" # provide a default value if unspecified

Cities_buffer_distance = arcpy.GetParameterAsText(1)
if Cities_buffer_distance == '#' or not Cities_buffer_distance:
    Cities_buffer_distance = "10 Miles" # provide a default value if unspecified

US_Boundaries = arcpy.GetParameterAsText(2)
if US_Boundaries == '#' or not US_Boundaries:
    US_Boundaries = "us_boundaries" # provide a default value if unspecified

#### Paths to various files. \\ is the default but / would work as well (Gadi) 
	
# Local variables:
us_cities = "us_cities"
Buffered_Cities = "C:\\Users\\gadidreyfuss\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer"
us_roads = "us_roads"
Buffered_Roads = "C:\\Users\\gadidreyfuss\\Documents\\ArcGIS\\Default.gdb\\us_roads_Buffer"
Buffered_Cities_and_Roads = "C:\\Users\\gadidreyfuss\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer_Intersect"
Clipped = "C:\\Users\\gadidreyfuss\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer_Intersect_C"


#### Like the back end development, this is for the "work" of the script (Gadi) 


# Process: Buffer the cities
arcpy.Buffer_analysis(us_cities, Buffered_Cities, Cities_buffer_distance, "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Buffer the roads
arcpy.Buffer_analysis(us_roads, Buffered_Roads, Road_buffer, "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis("C:\\Users\\gadidreyfuss\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer #;C:\\Users\\gadidreyfuss\\Documents\\ArcGIS\\Default.gdb\\us_roads_Buffer #", Buffered_Cities_and_Roads, "ALL", "", "INPUT")

# Process: Clip
arcpy.Clip_analysis(Buffered_Cities_and_Roads, US_Boundaries, Clipped, "")
