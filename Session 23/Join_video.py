import cv2
import numpy as np

org = cv2.VideoCapture('face.mp4')

_, org_image = org.read()

fourcc = cv2.VideoWriter_fourcc(*"XVID")

try:
    (h, w) = org_image.shape[:2]
except:
    w = 1280
    h = 720

w = w * 3
h = h * 3
video = cv2.VideoWriter("joined_titled.avi", fourcc, 20, (w, h), True)

org_nstab = cv2.VideoCapture('output_not_stabilized.mp4')
org_stab = cv2.VideoCapture('output_stabilized.mp4')
text1 = "Original"
text2 = "Unstablised"
text3 = "Stabilised"





while True:
    _, orgns_img = org_nstab.read()
    _, orgs_img = org_stab.read()
    _, org_image = org.read()


    image = np.zeros((h, w, 3), dtype="uint8")

    # image[:,:,:] = org_image
    org_image = cv2.resize(org_image, (w//3, h//3))
    orgns_img = cv2.resize(orgns_img, (w//3, h//3))
    orgs_img = cv2.resize(orgs_img, (w//3, h//3))

    image[h//3:2*h//3, 0:w//3, :] = org_image[0:org_image.shape[0],:,:]
    image[h//3:2*h//3, (w//3):(2*(w//3)), :] = orgns_img
    image[h//3:2*h//3, 2*w//3:w, :] = orgs_img

    cv2.putText(image, text1, (w//3//2-25, h//3 - 25), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3,cv2.LINE_AA)
    cv2.putText(image, text2, (w//3//2-25+w//3, h//3 - 25), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3,cv2.LINE_AA)
    cv2.putText(image, text3, (3*w//3//2-25+w//3, h//3 - 25), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3,cv2.LINE_AA)

    cv2.imshow("joined",image)
    video.write(image)
    key = cv2.waitKey(10) & 0xFF