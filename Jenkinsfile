pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                export PIPENV_VENV_IN_PROJECT=1
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