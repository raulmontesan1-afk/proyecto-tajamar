print("APP TAREAS")
from ui import msg_bienvenida, msg_salida_bucle_eventos, msg_input
from tareas import añadir_tarea

def main():
    print(msg_bienvenida)
    tareas = []

while True:
    print(msg_salida_bucle_eventos)
    titulo_tarea = input(msg_input)
    if titulo_tarea.upper() in ("STOP", "PARA", "PARAR", "S"):
        break
    añadir_tarea(tareas, titulo_tarea.title())
    print(tareas)  # TODO: Esto tiene que verse mas bonito
    
if __name__ == "__main__":
     main()
    