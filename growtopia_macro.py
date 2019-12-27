import pyautogui, subprocess
import time
import threading
import sys

def abc():
    while True:
        global isBreaking
        y = input('종료할려면 a라고 입력')
        if y == 'a':
            print('a')
            isBreaking = False
        else:
            print('다시 입력해주세요.')

a = subprocess.check_output('tasklist /FI "IMAGENAME eq Growtopia.exe', universal_newlines=True)
isBreaking = True


if '정보: 실행 중인 작업 중 지정된 조건에 일치하는 작업이 없습니다.' in a:
    pyautogui.alert('Growtopia를 실행해 주세요')
else:
    pyautogui.alert('블럭 자동 파괴 매크로가 실행됩니다.')

howRepeat = pyautogui.prompt('몇번이나 반복할껀지 지정해주세요(넉넉하게 잡아주세요).')

breakNum = pyautogui.prompt('한번에 부술 블럭 수를 입력해주세요 \n 이 프로그램은 핀볼 전용입니다.')

pyautogui.alert('부술 블럭 좌표를 지정합니다. 3초안에 커서를 그쪽으로 놓아주세요.')
time.sleep(3)
breakBlockX, breakBlockY = pyautogui.position()

pyautogui.alert('인벤토리 안 손 좌표를 지정합니다. 3초안에 커서를 그쪽으로 놓아주세요.')
time.sleep(3)
handX, handY = pyautogui.position()

pyautogui.alert('인벤토리 안 사용할 블럭 위치를 지정합니다. 3초안에 커서를 그쪽으로 놓아주세요.')
time.sleep(3)
blockX, blockY = pyautogui.position()

pyautogui.alert('매크로를 3초후 시작합니다.\n강제로 종료할려면 커맨드창에 a라고 입력후 엔터를 쳐주세요.')
time.sleep(3)

ab = 0

t1 = threading.Thread(target=abc)
t1.daemon = True 
t1.start()

while isBreaking and ab < int(howRepeat):
    pyautogui.moveTo(blockX, blockY)
    pyautogui.click()

    for i in range(int(breakNum)):
        pyautogui.moveTo(breakBlockX, breakBlockY)
        pyautogui.click()
        pyautogui.keyDown('left')
        time.sleep(0.06)
        pyautogui.keyUp('left')

    pyautogui.moveTo(handX, handY)
    pyautogui.click()

    for g in range(int(breakNum) + 1):
        pyautogui.moveTo(breakBlockX, breakBlockY)
        pyautogui.click(clicks=8,  interval=0.25)

        pyautogui.keyDown('right')
        time.sleep(0.055)
        pyautogui.keyUp('right')

    ab = ab + 1