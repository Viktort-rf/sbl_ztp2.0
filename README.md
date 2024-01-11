Для того, чтобы ZTP на устройстве начал работать, необходимо выполнить factory reset. Для этого на устройстве надо дать команды:

    mes24хх:
        delete startup-config

    qsw46хх:
        boot startup-config null
