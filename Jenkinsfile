pipeline{
    agent any
    stages{
        stage('git clone project') {
            steps {
                sh '''
                git init
                git clone https://github.com/ghanshyam95s/python-apps.git
                '''
            }
        }

        stage('creating docker image') {
            steps {
                sh '''
                cd python-apps
                docker build -t fastapi-app:8081 .
                '''
            }
        }
        stage("running docker image as container") {
            steps {
                sh "docker run --name fast_c_8081 -d -p 8081:8081 fastapi-app:8081"
            }
        }
    }
}