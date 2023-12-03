
from flask import Flask, Response      # flask 통신을 이용하기 위한 모듈 불러오기
import face_recognition  # 얼굴 인식 모듈 불러오기
Import cv2   # 카메라 캡처를 위한 opencv 모듈 불러오기
Import numpy as np
Import glob   #  경로로부터 이미지를 불러오기 위해 선언
From lcd import *    # lcd.py에서 문자를 출력하기 위한 모듈 불러오기
From buzzer import *   # buzzer.py에서 지정된 소리를 출력하기 위한 모듈 불러오기
from led import *   # led.py에서 지정된 색깔을 출력하기 위한 모듈 불러오기

Led_pins = [18, 19, 21]   # led board 핀 선언
GPIO.setmode(GPIO.BOARD)   # GPIO를 board 모드로 설정, GPIO 번호가 아닌 board 번호로 핀 설정

GPIO.setup(led_pins[0], GPIO.OUT)  # led_pin의 R을 출력 모드로 설정
GPIO.setup(led_pins[1], GPIO.OUT)  # led_pin의 G을 출력 모드로 설정
GPIO.setup(led_pins[2], GPIO.OUT)  # led_pin의 B을 출력 모드로 설정

def face_encoding():        # 저장된 이미지를 불러와서 분석, 분석한 결과값을 리스트에 넣고 반환
    known_face_encodings=[]    # encoding한 값을 저장하기 위한 리스트 선언
    known_face_names=[]     # 등록된 이름 값을 저장하기 위한 리스트 선언
    # Load a sample picture and learn how to recognize it.    
    hyomin=glob.glob(＂./data/hyomin/*.jpg＂)     # 경로에 저장된 이미지 데이터를 모두 불러옴
    for I in hyomin:        # hyomin 리스트 내의 이미지 경로에 대하여 
        hyomin_image = face_recognition.load_image_file(i)        # 이미지를 로드함
        hyomin_face_encoding = face_recognition.face_encodings(hyomin_image)[0]  # 이미지를 encoding함
        known_face_encodings.append(hyomin_face_encoding)        # encoding한 이미지를 known_face_encodings 리스트에 append 해 줌
        known_face_names.append(“hyomin”)   # known_face_names 리스트에 “hyomin” 값을 append 해 줌
    
    return known_face_encodings,known_face_names   # 인코딩과 이름 값을 저장한 리스트를 반환함

    
    # frame을 가져와 가공 및 반환 하는 함수
    # 이미지를 분석하여 반환한 리스트를 가지고 얼굴 인식 알고리즘을 시작
    def gen_frames():  # generate frame by frame from camera

        while True:

            # Capture frame-by-frame

            success, frame = camera.read()  # 카메라 frame과 성공 여부를 반환
            
            # frame 읽기를 성공했으면 else문 실패했으면 while문을 종료
            if (not success):

                break

            else:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # ¼ 프레임으로 축소해서 처리 속도를 빠르게 함

                #Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1] # 얼굴 인식에서는 RGB를 사용하므로 BGR 이미지를 RGB로 바꿔줌


                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame) # 촬영한 비디오 프레임에서 얼굴 각 부위(눈, 코, 입)의 위치를 찾음             
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) # 찾은 얼굴 위치값과 비디오 프레임을 모두 인코딩함

                face_names = []           # 출력한 결과 값을 담기 위한 리스트 선언     
                for face_encoding in face_encodings:                    # face_encodings 내의 요소들에 대해
                                       
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)   # 찾은 얼굴과 등록된 얼굴 encoding 값을 비교함                 
                    name = "Unknown"   # 등록된 얼굴이 없으면 unknown 값이 할당됨      
                                       
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)  
                    # 등록된 얼굴에서의 얼굴 위치와 촬영된 프레임에서의 얼굴 위치를 비교하여 거리를 측정함            
                    best_match_index = np.argmin(face_distances)     # 등록된 얼굴에서 가장 가까운 곳에 있는 얼굴을 비교함           
                    if matches[best_match_index]:                        
                        name = known_face_names[best_match_index]      # 등록된 얼굴과 촬영된 얼굴을 비교하여 매치되면 등록된 이름을 name 변수에 할당함            
                    face_names.append(name)                    # name 변수 값을 face_names 리스트에 append 해 줌
                    lcd.clear()                               # lcd 초기화
                
                if "hyomin" in face_names:    # 매치하여 할당된 name 변수 중 “hyomin”이 있으면 등록된 얼굴에 대한 반응 함수가 실행됨                   
                    buzzer_in()                             # 긍정적인 부저 소리 출력
                    led_green(led_pins)             # 초록색 led 출력
                    lcd_known()                           # lcd에 “come in” 문구 출력
                    sleep(2)                                   # 2초 동안 쉼
                    lcd_clear()                               # lcd 초기화
                    led_yellow(led_pins)            # 노란색 led 출력            
                
                elif "Unknown" in face_names:      # 매치하여 할당된 name 변수가 “unknown”이면 등록되지 않은 얼굴에 대한 반응 함수가 실행됨            
                    buzzer_out()                   # 부정적인 부저 소리 출력
                    led_red(led_pins)          # 빨간색 led 출력
                    lcd_unknown()               # lcd에 “you’re unknown” 문구 출력
                    sleep(2)                           # 2초 동안 쉼
                    lcd_clear()                      # lcd 초기화
                    led_yellow(led_pins)    # 노란색 led 출력                           

                # 영상처리 결과 이미지 출력
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # ¼ 로 줄였던 이미지를 다시 4배로 복원함                   
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # 갑지한 얼굴 부부에 박스를 그림
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # 감지한 얼굴의 바운딩 박스 위에 라벨을 달아줌
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1) # 라벨을 문자로 넣어줌



                ret, buffer = cv2.imencode('.jpg', frame) # 박스와 라벨을 단 프레임을 인코딩함

                frame = buffer.tobytes()      # 인코딩한 이미지 정보를 numpy 형태에서 byte 형태로 바꿔 줌
                yield (b'--frame\r\n'                       
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')     # 이미지 정보를 주어진 경로로 보내줌                      


    app = Flask(__name__)    # flask 객체를 app 에 할당
    @app.route('/video_feed')     # flask 통신을 통해 보낼 경로의 주소의 옵션을 설정해 줌

    def video_feed():   # 해당 경로로 요청이 올 때 실행할 함수를 선언해 줌     
     
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')   
        #  함수 실행에 대한 응답으로 gen_frames 함수를 통해 인코딩한 이미지를 반환함

    app.run(host='0.0.0.0', port=8080)     # 플라스크 서버와 포트를 선언, 연결된 경로로 어플리케이션(함수)를 실행함
