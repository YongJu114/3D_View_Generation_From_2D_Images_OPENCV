#=======================================================================
#     AUTHOR: YANG YONG
#     DATE: 3/9/2019
#     TIME: 9:7(SYDNEY)
#     CORE OF THIS PROJECT IS MATHMATICAL IDEA AND USE DATA STRUCTURE
#     DEVELOPMENT LANGUAGE: PYTHON
#     DEVELOPMENT LIBRARY: OPENCV
#     CODE DESCRIPTION:
#       1. ENTER THE NUMBER OF PICTURES
#       2. THE NUMBER OF PIXELS OF THE TRAGET PICTURE IS DETERMINED
#       3. COMPLETE TARGET PICTURE  
#
#========================================================================

#==================================: 1 :=================================
import cv2
import glob


def process(t, al):
    i = 0
    
    for pathy in glob.glob("images/*.jpg"):
        img = cv2.imread(pathy, 0)
        rows, cols = img.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),al,1) 
        img = cv2.warpAffine(img,M,(cols,rows))
        res[i:i+1, 0:cols] = img[t:t+1, 0:cols]
        i += 1
    cv2.imshow("result1", res)
    

print("#################=========|  LOADING PICTURE  |========##############")
print("#################=========|  LOADING SUCCESSFULLY  |========##############")



# imga = cv2.imread("image/1.jpg", 0)
# #==================================: 2 :=================================
# r, c = imga.shape
x = 0
for pty in glob.glob("images\*.jpg"):
    n = cv2.imread(pty, 0)
    x = x + 1
r, c = n.shape
res = n[0:x, 0:c]
#==================================: 3 :=================================



def main():
    for pty in glob.glob("images\*.jpg"):
        n = cv2.imread(pty, 0)
        break
    r, c = n.shape
    t = int(r/2)
    l = t
    aa = 0
    atemp = 0
    stemp = t
    while(True):
        k = cv2.waitKey(1)
        process(t, aa)
        if k & 0xFF == ord('w'):
            t = (t + 1)%r
        if k & 0xFF == ord('s'):
            stemp = (stemp + 1)%l
            t = l - stemp

        if k & 0xFF == ord('d'):
            atemp = (atemp + 1)%360
            aa = 360 - atemp
            
        if k & 0xFF == ord('a'):
            aa = (aa + 1)%360
        if k & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
#======================================| END |===================================================


