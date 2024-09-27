import time

import cv2, sys, numpy, os


def recognize():
    print("wtf")
    size = 4
    haar_file = 'haarcascade_frontalface_default.xml'
    datasets = 'faces'
    # Part 1: Create fisherRecognizer
    print('Recognizing Face Please Be in sufficient Lights...')
    name = "none"
    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(datasets):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1
    (width, height) = (130, 100)

    # Create a Numpy array from the two lists above
    (images, labels) = [numpy.array(lis) for lis in [images, labels]]
    # OpenCV trains a model from the images
    # NOTE FOR OpenCV2: remove '.face'
    model = recognizer = cv2.face.LBPHFaceRecognizer.create()
    model.train(images, labels)

    # Part 2: Use fisherRecognizer on camera stream
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)
    t_end = time.time() + 2
    didTake = 0
    while time.time() < t_end:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            # Try to recognize the face
            prediction = model.predict(face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if prediction[1] < 500:
                cv2.putText(im, '% s - %.0f' %
                            (names[prediction[0]], prediction[1]), (x - 10, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                name = names[prediction[0]]
            else:
                cv2.putText(im, 'not recognized',
                            (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                name = "not recognized"
        cv2.imshow('OpenCV', im)
        if (not name.__eq__('none')) & didTake == 0:
            cv2.imwrite('image' + '.png', im)
            didTake = 1
        key = cv2.waitKey(10)
        if key == 27:
            break
    return name
