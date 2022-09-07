setImageType('BRIGHTFIELD_H_E');
setColorDeconvolutionStains('{"Name" : "H&E default", "Stain 1" : "Hematoxylin", "Values 1" : "0.65111 0.70119 0.29049 ", "Stain 2" : "Eosin", "Values 2" : "0.2159 0.8012 0.5581 ", "Background" : " 255 255 255 "}');

import qupath.lib.objects.PathObjects
import qupath.lib.roi.ROIs
import qupath.lib.regions.ImagePlane

def imageData = getCurrentImageData()
def plane = getCurrentViewer().getImagePlane()
def server = imageData.getServer()
print server

int i = 0

// Create an empty text file
String coordinates_file_name = 'LUNG_TISSUE_9'
def path = buildFilePath(PROJECT_BASE_DIR, coordinates_file_name + '.txt')
def file = new File(path)
file.text = ''

runPlugin('qupath.imagej.detect.cells.WatershedCellDetection', '{"detectionImageBrightfield": "Hematoxylin OD",  "requestedPixelSizeMicrons": 0.5,  "backgroundRadiusMicrons": 8.0,  "medianRadiusMicrons": 0.0,  "sigmaMicrons": 2,  "minAreaMicrons": 10.0,  "maxAreaMicrons": 400.0,  "threshold": 0.12,  "maxBackground": 2.0,  "watershedPostProcess": false,  "cellExpansionMicrons": 5.0,  "includeNuclei": true,  "smoothBoundaries": true,  "makeMeasurements": true}');
      
//runPlugin('qupath.imagej.detect.cells.WatershedCellDetection', '{"detectionImageBrightfield": "Hematoxylin OD",  "backgroundRadius": 35.0,  "medianRadius": 0.0,  "sigma": 3.0,  "minArea": 50.0,  "maxArea": 1000.0,  "threshold": 0.4,  "maxBackground": 2.0,  "watershedPostProcess": true,  "cellExpansion": 5.0,  "includeNuclei": true,  "smoothBoundaries": true,  "makeMeasurements": true}');
    
    
// Loop through all objects & write the points to the file
    
    for (cell in getDetectionObjects()) {
        def detect = cell.getROI()
        //def dupa = detect.getPolygonPoints()
        //print detect.getClass()
        //print detect.getAllPoints()
        //print detect.getBoundsHeight()
        //print detect.getPolygonPoints()
        file << detect.getAllPoints() << System.lineSeparator()
        }
    