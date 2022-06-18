# invisibility-cloak
This project is developed using python OpenCV and NumPy Libraries. This is inspired from Harry Potter's Invisiblity Cloak. 
 *using a webcam, captured the live feed of the person and the background.
first captured the background so that if the cloth comes in it shows the background.
then set the values for the cloak.
making 2 masks and applying them to the frame.
the mask generated, determines the region in the frame corresponding to the detected color. The mask is then refined and then used for segmenting out the cloth from the frame.
