import os
import cv2

save_data = 'dataset/'
os.makedirs(save_data, exist_ok=True)

num_class = 28
data_size = 100

gesture = {idx: val for idx, val in enumerate('abcdefghijklmnopqrstuvwxyz')}
gesture[26] = 'space'
gesture[27] = 'clear'

cap = cv2.VideoCapture(0)

for i in range(num_class):
    path = save_data + f'{gesture[i]}/'
    os.makedirs(path, exist_ok=True)
    print(f'{i+1}번째 데이터 수집 준비')

    # 준비
    while True:
        ret, frame = cap.read()
        if not ret:
            print("오류")
            break
        cv2.putText(
            frame,
            text='press Q',
            org=(100, 50),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_AA
        )
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == ord('q'):
            print('수집 시작')
            break

    # 이미지 수집
    for j in range(data_size):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(path + f'{j}.jpg', frame)

cap.release()
cv2.destroyAllWindows()
