pipeline {
    agent any 
    stages{
        stage('Clone') {
            steps {
                git branch: 'main',
                    credentialsId: '82e71a1f-de83-4d80-a9e8-edb40490a04c',
                    url: 'https://github.com/dat-nguyentan1/neurond-developer-assistant.git'
            }
        }
    }
}