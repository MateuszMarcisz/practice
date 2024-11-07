import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')  # Read image and transform it into a NumPy array.

img_rescaled = img / 255

red_channel = 'Use slicing to extract the red channel'
green_channel = 'Use slicing to extract the green channel'
blue_channel = 'Use slicing to extract the blue channel'

if __name__ == '__main__':
    print('Green channel: ')
    print(red_channel)
    print('\nRed channel: ')
    print(green_channel)
    print('\nBlue channel: ')
    print(blue_channel)


