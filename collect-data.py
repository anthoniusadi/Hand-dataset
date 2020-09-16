import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/RGB")

    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/train/6")
    os.makedirs("data/train/7")
    os.makedirs("data/train/8")
    os.makedirs("data/train/9")
    os.makedirs("data/train/10")
    os.makedirs("data/train/n")
    

    os.makedirs("data/RGB/1")
    os.makedirs("data/RGB/2")
    os.makedirs("data/RGB/3")
    os.makedirs("data/RGB/4")
    os.makedirs("data/RGB/5")
    os.makedirs("data/RGB/6")
    os.makedirs("data/RGB/7")
    os.makedirs("data/RGB/8")
    os.makedirs("data/RGB/9")
    os.makedirs("data/RGB/10")
    os.makedirs("data/RGB/n")
###data test
    
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/test/6")
    os.makedirs("data/test/7")
    os.makedirs("data/test/8")
    os.makedirs("data/test/9")
    os.makedirs("data/test/10")
    os.makedirs("data/test/n")

# Train or test 
mode = 'train'
directory = 'data/'+mode+'/'

mode2 = 'RGB'
directory2 = 'data/'+mode2+'/'


cap = cv2.VideoCapture(2)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'six': len(os.listdir(directory+"/6")),
             'seven': len(os.listdir(directory+"/7")),
             'eight': len(os.listdir(directory+"/8")),
             'nine': len(os.listdir(directory+"/9")),
             'ten': len(os.listdir(directory+"/10")),
             'none': len(os.listdir(directory+"/n"))
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "SIX : "+str(count['six']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "SEVEN : "+str(count['seven']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "EIGHT : "+str(count['eight']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "NINE : "+str(count['nine']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TEN : "+str(count['ten']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "NONE : "+str(count['none']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # Coordinates of the ROI
    x1 = int(0.6*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.4*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]

    roi = cv2.resize(roi, (224, 224)) 
 
    cv2.imshow("Frame", frame)
    image_rgb = roi
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ##!gmm algorithm
    ##_, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
        cv2.imwrite(directory2+'1/'+str(count['one'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
        cv2.imwrite(directory2+'2/'+str(count['two'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
        cv2.imwrite(directory2+'3/'+str(count['three'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
        cv2.imwrite(directory2+'4/'+str(count['four'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
        cv2.imwrite(directory2+'5/'+str(count['five'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', roi)
        cv2.imwrite(directory2+'6/'+str(count['six'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', roi)
        cv2.imwrite(directory2+'7/'+str(count['seven'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', roi)
        cv2.imwrite(directory2+'8/'+str(count['eight'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', roi)
        cv2.imwrite(directory2+'9/'+str(count['nine'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'10/'+str(count['ten'])+'.jpg', roi)
        cv2.imwrite(directory2+'10/'+str(count['ten'])+'.jpg', image_rgb)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'n/'+str(count['none'])+'.jpg', roi)
        cv2.imwrite(directory2+'n/'+str(count['none'])+'.jpg', image_rgb)
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
