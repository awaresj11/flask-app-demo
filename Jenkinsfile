@Library("shared") _
pipeline {
    agent any

    stages {
        stage('hello') {
            steps {
                script{
                    hello()
                }
            }
        }
        stage('Code Copy') {
            steps {
                clone("https://github.com/awaresj11/flask-app-demo.git" , "master")
            }
        }
        stage('Build') {
            steps {
                docker_build("demo-flask-app","latest")
            }
        }
        stage('Test') {
            steps {
                echo 'this is testing a code..'
            }
        }
        stage('Deploy') {
            steps {
               
                deploy('docker-compose.yml')
                
            }
        }
         
    }
}
