pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio desde Git
                sh 'git init https://github.com/Aggasth/python-app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Instalar dependencias
                sh 'python3 -m pip install pymongo names'
            }
        }
        stage('Run Application') {
            steps {
                sh 'python3 aplicacion.py'
            }
        }
    }
}
