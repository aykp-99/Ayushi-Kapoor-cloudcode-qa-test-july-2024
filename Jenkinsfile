pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                git 'https://github.com/yourusername/my-python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests
                script {
                    sh 'pytest'
                }
            }
        }

        stage('Package') {
            steps {
                // Package your application (optional)
                echo 'Packaging application...'
            }
        }
    }

    post {
        always {
            // Clean up or notify
            echo 'Cleaning up...'
        }
        success {
            // Notify on success
            echo 'Pipeline succeeded!'
        }
        failure {
            // Notify on failure
            echo 'Pipeline failed!'
        }
    }
}
 
