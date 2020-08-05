groups_folder_path = './cnn_sample/'
categories = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "A", "C", "D", "E", "F", "H", "J","K", "L", "M",
              "N", "R", "S", "T", "X", "Y", "Z"]
num_classes = len(categories)

image_w = 28
image_h = 28
X = []
Y = []
  
for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'
  
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            print(image_dir+filename)
            img = cv2.imread(image_dir+filename)
            img = cv2.resize(img, None, fx=image_w/img.shape[0], fy=image_h/img.shape[1])
            X.append(img/256)
            Y.append(label)
 
X = np.array(X)
Y = np.array(Y)