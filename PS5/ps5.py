# Problem Set 5
# Name: Tuo Sun
# Collaborators: Sen Dai
# Time: 3:00

from PIL import Image
import numpy
import math


def generate_matrix(color):
	"""
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns: 
        matrix: a transformation matrix corresponding to 
                deficiency in that color
    """
	# You do not need to understand this function.
	if color == 'red':
		c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
	elif color == 'green':
		c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
	elif color == 'blue':
		c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
	elif color == 'none':
		c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
	return c


def matrix_multiply(m1, m2):
	"""
    Multiplies the input matrices.  
    Inputs:
        m1,m2: input matrices
    Returns: 
        result: the matrix product of m1 and m2
        in a list of floats 
    """

	product = numpy.matmul(m1, m2)
	if type(product) == numpy.int64:
		return float(product)
	else:
		result = list(product)
		return result


def convert_image_to_pixels(image):
	"""
    Takes an image (must be inputted as a string 
    with proper file attachment ex: .jpg, .png)
    and converts to a list of tuples representing pixels.  
    Each pixel is a tuple containing (R,G,B) values.  
    
    Returns the list of tuples.
   
    Inputs: 
        image: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values in form (R,G,B) such as 
                 [(0,0,0),(255,255,255),(38,29,58)...]
    """
	im = Image.open(image)
	return list(im.getdata())  # getdata returns tuple format


def convert_pixels_to_image(pixels, size):
	"""
    Creates an Image object from a given set of RGB tuples.

    Inputs:
        pixels: a list of pixels such as the output of 
                convert_image_to_pixels.
        size: a tuple of (width,height) representing 
              the dimensions of the desired image. Assume 
              that size is a valid input such that 
              size[0] * size[1] == len(pixels).
    returns: 
        img: Image object made from list of pixels
    """
	im = Image.new('RGB', size)  # create a new image container
	im.putdata(pixels)  # import array pixels data into the container
	return im


def apply_filter(pixels, color):
	"""
    pixels: a list of pixels in RGB form, such as [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing the color
    deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication  
    """
	m = generate_matrix(color)  # get the matrix for modifying
	new_pixels = []
	for pixel in matrix_multiply(pixels, m):
		# get each arraylist in modified array
		[r, g, b] = pixel  # get RGB float
		new_pixels.append((math.floor(r), math.floor(g), math.floor(b)))
	# insert the RGB tuple
	return new_pixels


def reveal_binary_image(filename):
	"""
    Extracts the hidden image in the least significant bit
    of each pixel in the specified image.
    Inputs:
       filename: string, input file to be processed
    returns:
       result: an Image object containing the hidden image
    """
	new_array = []
	im = Image.open(filename)
	pixels = convert_image_to_pixels(filename)  # get grayscale array
	for pixel in pixels:  # get tuple of grayscale
		new_array.append(255 * (pixel & 1))  # get hidden 1 least significant bits
	out = Image.new('L', im.size)  # create a new image container in L mode
	out.putdata(new_array)  # import array pixels data into the container
	return out


def reveal_RGB_image(filename):
	"""
    Extracts the hidden image in the 2 least significant bits
    of each pixel in the specified color image.
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
	new_array = [[], [], []]
	im = Image.open(filename)
	pixels = convert_image_to_pixels(filename)  # get RGB array
	for pixel in pixels:  # get tuple of RGB
		for x in range(3):  # get R, G, B lists
			new_array[x].append(85 * (pixel[x] & 3))  # change 0-3 to 0-255
		# get hidden 2 least significant bits
	final_array = list(zip(new_array[0], new_array[1], new_array[2]))
	# create a new image container in RGB mode,
	# and import array pixels data into the container
	return convert_pixels_to_image(final_array, im.size)


def main():
	pass

	# UNCOMMENT the following 7 lines to test part 1

	pixels = convert_image_to_pixels('test2.png')
	print(len(pixels))
	image = apply_filter(pixels, 'none')
	im = convert_pixels_to_image(image, (225, 224))
	im.show()
	new_image = apply_filter(pixels, 'red')
	im2 = convert_pixels_to_image(new_image, (225, 224))
	im2.show()

	# No tests for part 2. Try to find the secret images!

	im = reveal_binary_image('hidden1.bmp')
	im.show()
	im.save('revealed1.jpg')

	im = reveal_RGB_image('hidden2.bmp')
	im.show()
	im.save('revealed2.jpg')


if __name__ == '__main__':
	main()
