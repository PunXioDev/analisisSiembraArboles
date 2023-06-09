def crearTabla(dataFrame, nombreTabla):
    archivoHTML = dataFrame.to_html()  # AQUI TENGO EL DATAFRAME VERSION HTML
    archivo = open(f'./tablas/{nombreTabla}.html', "w", encoding="UTF-8")  # TENGO HTML VACIO
    archivo.write('''
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8" />
                        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                        <title>Tablas</title>
                        <link
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
                        crossorigin="anonymous"
                        />
                    </head>
                    <body>
                        <main class="container-fluid">
                ''')  # AGREGO EL ESTILO A LOS DATOS
    archivo.write(archivoHTML)
    archivo.write('''
                        </main>
                    </body>
                    </html>
                  ''')
    archivo.close()  # CIERRO EL ARCHIVO HTML
