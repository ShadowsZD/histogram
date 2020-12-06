# histogram
Histogram comparsion assignment

Program made using python, with the following libs:
cv2 for image treatment and comparsions
numpy for some operations on the image
glob to deal with files
argparse to make command line arguments

Execution:
The program needs to be executed on a folder with the sample images for testing.
At the end of execution, the program will print the overall accuracy for each method of histogram comparsion used.
You can specify the -o flag to make it produce csv outputs with the result of each comparsion for the methods applied in it.
The accuracy is calculated by dividing the matches by total number of comparsion.
We get the number of matches by verifying if the image with the best number (higher or lower, depending on method), excluding itself, is its pair.
For it to work correctly, images that are pairs should be named with the same name and extensions, but different digits (img1.png, img2.png).
The number of comparsions, is the number of times we compare the original histogram, to the best one to see if it is the pair or not.
