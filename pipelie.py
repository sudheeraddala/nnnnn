pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
git 'https://github.com/sudheeraddala/project1111.git'
            }
        }
        stage('Build') {
            steps {
                // Your build commands here
            }
        }
        stage('Test') {
            steps {
                // Your test commands here
            }
        }
        stage('Deploy') {
            steps {
                // Your deployment commands here
            }
        }
    }
}
