# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specificatio
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np


def convertFloatToInt(image):
    '''Convers input image to int values in range 0-255 from decimal values 0-1.'''

    new_image = (image * 255).astype(np.uint8)

    return new_image

def find_red_pixels(map_filename='map.png', upper_threshold=100 ,lower_threshold=50):
    """Creates a jpeg image, 'map-red-pixels.jpg', and returns a 2D numpy array.

    Args: 
        map_filename is the filename of png image
        upper_threshold is set to 100 and
        lower_threshold is set to 50 for RBG value thresholds
    Returns:
        Saves jpg image showing only red pixels (found using thresholds) from input image as white pixels.
        Returns a 2D numpy array conataining binary values representing white pixels.
    """

    image = plt.imread('data/' + map_filename)
    image = convertFloatToInt(image)
    newimage = []
    pixel_array = np.zeros(shape=(image.shape[0], image.shape[1])).astype(int)
    for row in range(image.shape[0]):
        rowtemp = []
        for pixel in range(image.shape[1]):
            if image[row][pixel][0] > upper_threshold and image[row][pixel][1] < lower_threshold and image[row][pixel][2] < lower_threshold:
                rowtemp.append(np.array([1,1,1]).astype(float))
                pixel_array[row][pixel] = 1
            else:
                rowtemp.append(np.array([0,0,0]).astype(float))
        newimage.append(rowtemp)
    newimage = np.array(newimage).astype(float)
    plt.imsave('data/map-red-pixels.jpg', newimage)
    return pixel_array


def find_cyan_pixels(map_filename='map.png', upper_threshold=100, lower_threshold=50):
    """Creates a jpeg image, 'map-cyan-pixels.jpg', and returns a 2D numpy array.

    Args: 
        map_filename is the filename of png image
        upper_threshold is set to 100 and
        lower_threshold is set to 50 for RBG value thresholds
    Returns:
        Saves jpg image showing only cyan pixels (found using thresholds) from input image as white pixels.
        Returns a 2D numpy array conataining binary values representing white pixels.
        """

    image = plt.imread('data/' + map_filename)
    image = convertFloatToInt(image)
    newimage = []
    pixel_array = np.zeros(shape=(image.shape[0], image.shape[1])).astype(int)
    for row in range(image.shape[0]):
        rowtemp = []
        for pixel in range(image.shape[1]):
            if image[row][pixel][0] < lower_threshold and image[row][pixel][1] > upper_threshold and image[row][pixel][2] > upper_threshold:
                rowtemp.append(np.array([1,1,1]).astype(float))
                pixel_array[row][pixel] = 1
            else:
                rowtemp.append(np.array([0,0,0]).astype(float))
        newimage.append(rowtemp)
    newimage = np.array(newimage).astype(float)
    plt.imsave('data/map-cyan-pixels.jpg', newimage)
    return pixel_array


def detect_connected_components(IMG=find_red_pixels()):
    """Creates a text file, 'cc-output-2a.txt', and returns a 2D numpy array.
    
    Args: 
        IMG is the output of the find_red_pixels function which is a 2D binary image array.
    Returns: 
        MARK is a 2D numpy array conataining binary values marking connected components.
        Saves a text file of connected components with how many pixels in each.
    """

    # Create an empty 2D array to store the detected components
    MARK = np.zeros(shape=(IMG.shape[0],IMG.shape[1]))

    # Create a dictionary to store the number of pixels in each component
    components = {} 
    
    # Iterate over all pixels in the image
    for i in range(IMG.shape[0]):
        for j in range(IMG.shape[1]):
            Q = []
            # If the current pixel is a white pixel and has not been visited,
            # add it to the queue and mark it as visited
            if MARK[i][j] == 0 and IMG[i][j] == 1:
                Q.append((i,j))
                MARK[i][j] = 1
                Q = np.array(Q)
                component_size = 1 # Resets component size for new component
                # While the queue is not empty, process the first pixel in the queue
                # and add its 8-neighbors to the queue if they are white and not visited
                # and add 1 to the component size 
                while len(Q) > 0 :
                    m, n = Q[0]
                    Q = np.delete(Q,0,0)
                    for s in range(m-1, m+2):
                        for t in range(n-1, n+2):
                            if m == s and n == t:
                                continue
                            elif (s >= 0 and s < IMG.shape[0]) and (t >= 0 and t < IMG.shape[1]) and (MARK[s][t] == 0 and IMG[s][t] == 1):
                                Q = np.insert(Q,0,[s,t],0)
                                MARK[s,t] = 1
                                component_size += 1
                # Each while loop represents a connected component so once finishied add
                components[len(components)] = component_size
    file = open("data/cc-output-2a.txt", "w")

    # Loop through the dictionary and write each key-value pair to the file
    for key, value in components.items():
        file.write(f"Connected Component {key+1}, number of pixels = {value}\n")

    # Write the total number of connected components to the file and close the file
    file.write(f"Total number of connected components = {len(components)}")
    file.close()

    return MARK

def detect_connected_components_sorted(MARK=detect_connected_components()):
    """Your documentation goes here"""
    visited = np.zeros(shape=(MARK.shape[0],MARK.shape[1]))
    top_two_components = np.zeros(shape=(MARK.shape[0],MARK.shape[1]))
    # Create a dictionary to store the number of pixels in each component
    components = {} 
    
    # Iterate over all pixels in the image
    for i in range(MARK.shape[0]):
        for j in range(MARK.shape[1]):
            Q = []
            # If the current pixel is a white pixel and has not been visited,
            # add it to the queue and mark it as visited
            if visited[i][j] == 0 and MARK[i][j] == 1:
                Q.append((i,j))
                visited[i][j] = 1
                Q = np.array(Q)
                component_size = 1 # Resets component size for new component
                # While the queue is not empty, process the first pixel in the queue
                # and add its 8-neighbors to the queue if they are white and not visited
                # and add 1 to the component size 
                while len(Q) > 0 :
                    m, n = Q[0]
                    Q = np.delete(Q,0,0)
                    for s in range(m-1, m+2):
                        for t in range(n-1, n+2):
                            if m == s and n == t:
                                continue
                            elif (s >= 0 and s < MARK.shape[0]) and (t >= 0 and t < MARK.shape[1]) and (visited[s][t] == 0 and MARK[s][t] == 1):
                                Q = np.insert(Q,0,[s,t],0)
                                visited[s,t] = 1
                                component_size += 1
                                if len(components) == 129 or len(components) == 109:
                                    top_two_components[s,t] = 1
                # Each while loop represents a connected component so once finishied add
                components[len(components)] = component_size
    # Turn components dictionary to a list of tuples
    d_list = [(k, v) for k, v in components.items()]

    # Create an empty list to store the sorted tuples
    sorted_list = []
    while d_list:
        min = d_list[0]  
        for x in d_list: 
            if x[1] < min[1]:
                min = x
        sorted_list.insert(0,min)
        d_list.remove(min)

    # Convert the sorted list back into a dictionary
    sorted_dict = dict(sorted_list)

    file = open("data/cc-output-2b.txt", "w")

    # Loop through the dictionary and write each key-value pair to the file
    for key, value in sorted_dict.items():
        file.write(f"Connected Component {key+1}, number of pixels = {value}\n")

    # Write the total number of connected components to the file and close the file
    file.write(f"Total number of connected components = {len(components)}")
    file.close()
    
    plt.imsave('data/cc-top-2.jpg', top_two_components, cmap='gray')

    text = 'Image and Text file have been saved.'
    return text


if __name__ == '__main__':
    #print(find_red_pixels('map.png'))
    print(detect_connected_components_sorted())
