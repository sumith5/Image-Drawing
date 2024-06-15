# Image-Drawing
Converting Electronics symbol images to the Drawings using Turtle library

<img width="300" alt="image" src="https://github.com/sumith5/Image-Drawing/assets/172884071/b4d813dc-cad6-4eb2-90f1-4102815fd4c9">

There isn’t an easy method to process images and draw symbols using the turtle library directly. So, I devised a logic to first pre-process the image and extract its outline. Then, I created a function to determine the nearest neighbor in a set of points. This allows the turtle to efficiently follow these positions on the canvas, enabling fast and accurate drawing.

I have written code not only to process and draw single image. The code process multiple images and combines image processing (extracting outlines) and Turtle graphics for drawing the outlined images at specified positions on the screen.

 Visit the following blog for Explanation : https://medium.com/@sumithearra/image-processing-with-turtle-for-electronic-symbols-drawing-3792c9a9f2d8

 Also read the following Blog for using Multithreading concepts with the turtle :
https://medium.com/@sumithearra/how-turtle-graphics-and-multithreading-interact-4f176e5703e0
