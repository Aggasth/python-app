pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar tu repositorio desde Git si es necesario
                sh 'git clone https://github.com/Aggasth/python-app.git'
                echo 'Ya existe el repositorio clonado'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install pymongo'
            }
        }
        stage('Ejecutar Aplicación') {
            steps {
                sh 'python3 aplicacion.py'
            }
        }
    }
}
