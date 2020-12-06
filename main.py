import cv2
import numpy as np
from scipy import stats
import math
import glob
import argparse
from matplotlib import pyplot as plt

def createHist(file, histograms, images):
    img = cv2.imread(file)
    #use this if plotting to get correct colors
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    hist = cv2.calcHist([img], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    histograms[file] = hist
    images[file] = img


def run():

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", action="store_true")

    arguments = parser.parse_args()
    output = arguments.o

    print(flag_value)

    OPENCV_METHODS = (
        ("Correlation", cv2.HISTCMP_CORREL),
        ("Chi-Squared", cv2.HISTCMP_CHISQR),
        ("Intersection", cv2.HISTCMP_INTERSECT),
        ("Bhattacharyya", cv2.HISTCMP_BHATTACHARYYA)
    )

    histograms = {}
    images = {}

    #Populatings histograms and file dictionary
    for file in glob.glob("*.png"):
        createHist(file, histograms, images)
    
    comparsions = len(images)

    matrix_result = np.zeros((comparsions+1,comparsions+1), dtype=object)

    list_of_files = []
    for filename in histograms:
        list_of_files.append(filename)

    matrix_result[0,:] = ['img'] + list_of_files
    matrix_result[:,0] = ['img'] + list_of_files

    final_result = matrix_result
    matches = 0

    for (methodName, method) in OPENCV_METHODS:
        i = 1
        matches = 0
        for (img, hist) in histograms.items():
            results = {}
            reverse = False

            if methodName in ("Correlation", "Intersection"):
                reverse = True
            
            for (img_compare, hist_compare) in histograms.items():
                d = cv2.compareHist(histograms[img], hist_compare, method)
                results[img_compare] = d

            test_match = sorted([(x, y) for (y, x) in results.items()], reverse = reverse)
            if (test_match[1][1][:-5] == test_match[0][1][:-5]):
                matches = matches + 1

            results = [(y) for (x,y) in results.items()]
            final_result[i,1:] = results

            i = i + 1

        if(output):
            np.savetxt(methodName + '_output.csv', final_result, delimiter=';', fmt='%s')
        print("Accuracy of " + methodName + ": {:.2%}".format(matches/comparsions))

if __name__ == "__main__":
    run()