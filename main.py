import pyautogui
import keyboard
import time

# Esperar 3 segundos antes de comenzar a pulsar la tecla "F"
time.sleep(3)

print("Manteniendo 'F' presionada. Presiona 'G' para detener.")

def mantener_f_presionada():
    pyautogui.keyDown('f')  # Presiona y mantiene "F" sin soltar
    while True:
        if keyboard.is_pressed('g'):  # Si se presiona "G", soltar "F"
            pyautogui.keyUp('f')  # Suelta la tecla "F"
            print("Detenido.")
            break
        time.sleep(0.1)  # Este sleep es para no saturar el ciclo con la verificación

try:
    mantener_f_presionada()
except KeyboardInterrupt:
    pyautogui.keyUp('f')  # Asegurarse de que la tecla "F" se suelte si se detiene el script
    print("Script detenido manualmente.")
