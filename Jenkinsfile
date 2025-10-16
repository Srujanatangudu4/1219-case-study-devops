pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image for App"
                bat "docker build -t ss:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"
                bat 'docker login -u srujanatangudu4 -p Srujana@2004'
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub"
                bat "docker tag expense-tracker:v1 srujanatangudu4/ss:v1"
                bat "docker push srujanatangudu4/ss:v1"
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post {
        success {
            echo 'Deployment Successful ✅'
        }
        failure {
            echo 'Deployment Failed ❌'
        }
    }
}




