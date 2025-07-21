pipeline {
    agent any
    tools {
        dockerTool 'docker'
    }
    stages {
        stage('Build frontend') {
            steps {
                sh' docker build -t frontend:latest -f frontend/Dockerfile .'
            }
        }
        stage('Build backend'){
            steps{
                sh 'docker build -t backend:latest -f booking-service/Dockerfile .'
            }
        }
    }
}