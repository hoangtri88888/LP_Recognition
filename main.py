print('heloooooooooo')
import cv2
print('1')
from pathlib import Path
print('2')
# from google.colab.patches import cv2_imshow
import argparse
print('3')
import time
from PIL import Image
print('4')
from src.lp_recognition import E2E
print('5')

print('hello')

def get_arguments():
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image_path', help='8.jpg', default='./samples/4.jpg')

    return arg.parse_args()


args = get_arguments()
img_path = Path(args.image_path)

# read image
img = cv2.imread(str(img_path))

# start
start = time.time()

# load model
print('load E2E')
model = E2E()

# recognize license plate
print('load predict')
image = model.predict(img)

# end
end = time.time()

print('Thời gian hoàn thành ĐM NGhĩa %.2f s' % (end - start))
print("ghi kết quả ra file result.jpg")
im = Image.fromarray(image)
# show image
im.show()
im.save("result.jpg")
# cv2.imshow("xử lý xong",image)
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     exit(0)


# cv2.destroyAllWindows()
