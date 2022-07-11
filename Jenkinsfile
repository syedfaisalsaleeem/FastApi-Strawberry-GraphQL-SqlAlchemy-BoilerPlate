pipeline {
    agent {label 'linux'}
    stages {
        stage('verify tooling') {
            steps {
                sh '''
                    docker info
                    docker version
                    docker-compose version
                    curl --version
                    '''
            }
        }
        stage('Start container'){
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
                sh 'docker ps'
            }
        }
        stage('Run tests') {
            steps {
                sh 'curl http://localhost:80/'
            }
        }
    }

}