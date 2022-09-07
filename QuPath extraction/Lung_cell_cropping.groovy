import ij.IJ
import ij.ImagePlus
import qupath.imagej.images.servers.ImagePlusServer
import qupath.imagej.images.servers.ImagePlusServerBuilder
import qupath.lib.images.servers.ImageServer
import qupath.lib.regions.RegionRequest
import qupath.lib.scripting.QP

import java.awt.image.BufferedImage

def imageData = getCurrentImageData()

ImageServer<BufferedImage> serverOriginal = QP.getCurrentImageData().getServer()
ImagePlusServer server = ImagePlusServerBuilder.ensureImagePlusWholeSlideServer(serverOriginal)
String path = server.getPath()
String serverName = serverOriginal.getShortServerName()

def targetImageHeightMicrons = 74.0
def size = 200 as int

String cell_class = 'MIXED_STROMA'
String image_number = '25'
String cell_coordinates_name =  cell_class + '_' + image_number


def folderPath = '/home/igf/Bioinformatyka/magisterka/original_annotated_images/Lung_cropped_cells/' + cell_class + '/'

double margin = 1.00

List<String> list = new ArrayList<String>();
new File('/home/igf/Bioinformatyka/magisterka/original_annotated_images/Lung_cells_coordinates/' + cell_coordinates_name + '.txt').eachLine { line ->
	    List<String> lst = new ArrayList<String>();
	    line_elements = line.split(';')
	    lst = line_elements[0][8..-2].split(', Point: ')
	    
	    
	    
	    
	    
	    List<Double> top     = [lst[0].split(', ')[0].toDouble(), lst[0].split(', ')[1].toDouble()]
	    List<Double> bottom    = [lst[0].split(', ')[0].toDouble(), lst[0].split(', ')[1].toDouble()]
	    List<Double> left      = [lst[0].split(', ')[0].toDouble(), lst[0].split(', ')[1].toDouble()]
	    List<Double> right     = [lst[0].split(', ')[0].toDouble(), lst[0].split(', ')[1].toDouble()]
	    
	    
	    for (l_string in lst) {
	    
	        def l = l_string.split(', ')
	        if (bottom[1] < l[1].toDouble()) {bottom = [l[0].toDouble(), l[1].toDouble()]}
	        if (top[1] > l[1].toDouble()) {top = [l[0].toDouble(), l[1].toDouble()]}
	        if (right[0] < l[0].toDouble()) {right = [l[0].toDouble(), l[1].toDouble()]}
	        if (left[0] > l[0].toDouble()) {left = [l[0].toDouble(), l[1].toDouble()]}
	    }
	    
	        
	    double y_coord = top[1] - margin
	    double x_coord = left[0] - margin
	    
    	    double y_size = (bottom[1] + margin) - (top[1] - margin)
	    double x_size = (right[0] + margin) - (left[0] - margin)
	    	    
	    RegionRequest request = RegionRequest.createInstance(path, 1, x_coord as int, y_coord as int, x_size as int, y_size as int, 0, 0)
            ImagePlus imp = server.readImagePlusRegion(request).getImage(false)
String name = String.format("%s (d=%.2f, x=%d, y=%d, w=%d, h=%d, z=%d, class=%s).%s", serverName, 1.0,x_coord as int, y_coord as int, x_size as int, y_size as int, 0, cell_class, 'tiff')
            
File file = new File(folderPath, name)
IJ.save(imp, file.getAbsolutePath())
	    
	}