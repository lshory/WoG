pipeline {
    agent any
        environment {
		    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
            PATH = "$PATH:/usr/local/bin"
	    }

    stages {
        stage('checkout') {
            steps {
                echo 'Clone Git Project Start'
                git url: 'https://github.com/lshory/WoG.git', branch: 'main',
                credentialsId: 'github_creds'
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
                sh "pip3 install selenium"
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
                echo '$DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
            }
            }
        stage('push image') {
            steps {
                sh 'docker tag liorshory/world_of_games liorshory/world_of_games'
                sh 'docker push liorshory/world_of_games'
            }
            }                        
        }   
}