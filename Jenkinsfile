pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pipenv install --dev'
            }
        }
        stage('Test') {
            steps {
                sh 'pipenv run python main.py'
            }
        }
    }
}