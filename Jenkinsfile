pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar tu repositorio desde Git si es necesario
                // sh 'git clone '
                echo 'Clonado!'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install pymongo'
            }
        }
        stage('Ejecutar Aplicació') {
            steps {
                sh 'python aplicacion.py'
            }
        }
    }
}
