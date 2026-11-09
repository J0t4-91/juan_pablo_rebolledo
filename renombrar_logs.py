
from pathlib import Path

# Carpeta donde se encuentran los archivos de registro
carpeta = Path("logs")

# Nombre que tendrán los archivos
nombre = "nombre_apellido"

# Verificar que exista la carpeta
if not carpeta.is_dir():
    print("No se encontró la carpeta de logs.")
else:
    # Filtrar los archivos con extensión .log
    archivos = sorted(
        archivo for archivo in carpeta.iterdir()
        if archivo.is_file()
        and archivo.suffix.lower() == ".log"
    )

    if not archivos:
        print("No se encontraron archivos .log.")
    else:
        # Evitar conflictos con nombres existentes
        temporales = []

        for numero, archivo in enumerate(archivos, start=1):
            temporal = carpeta / f"__temporal_{numero}.tmp"

            if temporal.exists():
                raise FileExistsError(temporal)

            archivo.rename(temporal)
            temporales.append((temporal, archivo.name))

        # Renombrar con numeración incremental
        for numero, (temporal, original) in enumerate(
            temporales, start=1
        ):
            nuevo = carpeta / f"{nombre}_{numero}.log"
            temporal.rename(nuevo)
            print(f"{original} -> {nuevo.name}")

        print("Proceso finalizado correctamente.")
