pipeline {
    agent any 
    stages{
        stage('Clone') {
            steps {
                withCredentials([gitUsernamePassword(credentialsId: '82e71a1f-de83-4d80-a9e8-edb40490a04c', gitToolName: 'Default')]) {
                    git 'https://github.com/dat-nguyentan1/neurond-developer-assistant.git'
                    }
            }
        }
    }
}