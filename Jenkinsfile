pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clonar el repositorio de tu aplicación desde tu sistema de control de versiones
                git 'https://github.com/Aggasth/python-app.git'
                // Cambiar 'URL_DEL_REPOSITORIO' por la URL real de tu repositorio
            }
        }

        stage('Instalar Dependencias') {
            steps {
                // Instalar las dependencias de tu aplicación si las tienes
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Aplicación') {
            steps {
                // Ejecutar tu aplicación en Python
                sh 'python app.py'
            }
        }
    }
}
