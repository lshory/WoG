pipeline {
    agent any
        environment {
		    DOCKERHUB_CREDENTIALS = credentials('test')
	    }

    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/lshory/WoG.git'
                echo 'Clone Git Project Done'
                }
            }   
        stage('build docker image') {
            steps {
                sh 'docker-compose build'
                echo "Build Docker Image completed"
            }
            }
        stage('docker run') {
            steps {
                sh 'docker-compose up -d'
                echo "Container Running"
            }
            }
        stage('test') {
            steps {
                sh 'python3 e2e.py'
                echo "Test PASSED"
            }
            }
        stage('terminate') {
            steps {
                sh 'docker stop WoG'
                echo "Container Stopped"
            }
            }
        stage('delete container') {
            steps {
                sh 'docker rm WoG'
                echo "Container Removed"
            }
            }
        stage('docker login') {
            steps {
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
            }
            }
        stage('push image') {
            steps {
                sh 'docker push liorshory/world_of_games'
            }
            }                        
        }   
}