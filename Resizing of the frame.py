import cv2
cap=cv2.VideoCapture(0)
print("Initial Camera dimensions are:")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# CAP_PROP_FRAME_WIDTH has a code 3
# CAP_PROP_FRAME_HEIGHT has a code 4
cap.set(3,240)  # the camera sets this according to its resolution i.e.1024 in this case...
cap.set(4,720)
print("New camera dimensions are:")
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while True:
    ret,frame = cap.read()
    if ret==False:
        print("Something wrong...trying again...")
        continue
    cv2.imshow("Colored frame",frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.imshow("gray frame",gray)
    key_press=cv2.waitKey(1)&0xff
    if key_press==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()