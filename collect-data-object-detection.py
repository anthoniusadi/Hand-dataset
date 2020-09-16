import cv2
import numpy as np
import os
#! create folder
if not os.path.exists("hand"):
    os.makedirs("hand")
    os.makedirs("hand/thomas")
    os.makedirs("hand/tongam")
    os.makedirs("hand/meisy")
    os.makedirs("hand/cbnw")
    os.makedirs("hand/aries")
    os.makedirs("hand/hendrik")
    os.makedirs("hand/viany")
    os.makedirs("hand/edwin")
    os.makedirs("hand/novi")
    os.makedirs("hand/silfany")
    
    
    
    
directory = 'hand/'
cap = cv2.VideoCapture(2)
i = 0
while True:
    _,frame = cap.read()

    frame = cv2.flip(frame,1)
    img = frame.copy()
    i+=1
    #! count jumlah tangan pada setiap folder
    count = {
        'tangan_thomas': len(os.listdir(directory+'thomas')),
        'tangan_meisy': len(os.listdir(directory+'meisy')),
        'tangan_tongam': len(os.listdir(directory+'tongam')),
        'tangan_cbnw': len(os.listdir(directory+'cbnw')),
        'tangan_aries': len(os.listdir(directory+'aries')),
        'tangan_hendrik': len(os.listdir(directory+'hendrik')),
        'tangan_viany': len(os.listdir(directory+'viany')),
        'tangan_edwin': len(os.listdir(directory+'edwin')),
        'tangan_novi': len(os.listdir(directory+'novi')),
        'tangan_silfany': len(os.listdir(directory+'silfany'))
        
        
    }
    #! tampilkan jumlah tangan pada setiap folder 
    cv2.putText(frame,"image count: ",(10,100),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80),1)
    cv2.putText(frame,'thomas(PRESS T) : '+str(count['tangan_thomas']),(10,120),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'meisy(PRESS M) : '+str(count['tangan_meisy']),(10,140),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'tongam(PRESS O) :'+str(count['tangan_tongam']),(10,160),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'cbnw(PRESS C) :'+str(count['tangan_cbnw']),(10,180),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'aries(PRESS A) :'+str(count['tangan_aries']),(10,200),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'hendrik(PRESS H) :'+str(count['tangan_hendrik']),(10,220),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'viany(PRESS V) :'+str(count['tangan_viany']),(10,240),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'edwin(PRESS E) :'+str(count['tangan_edwin']),(10,260),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'novi(PRESS N) :'+str(count['tangan_novi']),(10,280),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    cv2.putText(frame,'silfany(PRESS S) :'+str(count['tangan_silfany']),(10,300),cv2.FONT_HERSHEY_PLAIN,1,(0,255,80))
    

    
    cv2.imshow('frame',frame)
    cv2.imshow('img',img)
    interrupt = cv2.waitKey(10)
    #! ESC to break the program
    if interrupt & 0xFF == 27:
        break
    #! save untuk setiap nama(folder) dengan tekan huruf
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'thomas/'+'thom'+str(count['tangan_thomas'])+'.jpg',img)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'meisy/'+'meis'+str(count['tangan_meisy'])+'.jpg',img)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'tongam/'+'tong'+str(count['tangan_tongam'])+'.jpg',img)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'cbnw/'+'cbn'+str(count['tangan_cbnw'])+'.jpg',img)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'aries/'+'ar'+str(count['tangan_aries'])+'.jpg',img)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'hendrik/'+'hen'+str(count['tangan_hendrik'])+'.jpg',img)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'viany/'+'via'+str(count['tangan_viany'])+'.jpg',img)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'edwin/'+'edw'+str(count['tangan_edwin'])+'.jpg',img)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'novi/'+'nov'+str(count['tangan_novi'])+'.jpg',img)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'silfany/'+'sil'+str(count['tangan_silfany'])+'.jpg',img)

cap.release()
cv2.destroyAllWindows()