pipeline {
    agent any
    
    environment {
        BACKEND_URL = 'http://app-backend:8000'
        FRONTEND_URL = 'http://app-frontend:5173'
        VITE_BACKEND_URL = 'http://app-backend:8000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        
        stage('Start Application') {
            steps {
                echo 'Starting application containers...'
                script {
                    sh '''
                        cd application/infra
                        docker-compose down || true
                        docker-compose up -d app-backend app-frontend
                        sleep 15
                        
                        echo "Checking if services are healthy..."
                        docker ps
                    '''
                }
            }
        }
        
        stage('Run Integration Tests') {
            steps {
                echo 'Running integration tests...'
                sh '''
                    cd labs/06_07_08_test_framework
                    . /var/jenkins_home/.venv/bin/activate
                    pytest test/integration \
                        --junitxml=integration-report.xml \
                        --html=integration-report.html \
                        --self-contained-html \
                        -v
                '''
            }
        }
        
        stage('Run E2E Tests') {
            steps {
                echo 'Running E2E tests...'
                sh '''
                    cd labs/06_07_08_test_framework
                    . /var/jenkins_home/.venv/bin/activate
                    pytest test/e2e \
                        --browser chromium \
                        --junitxml=e2e-report.xml \
                        --html=e2e-report.html \
                        --self-contained-html \
                        -v
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Publishing test results...'
            
            junit '**/integration-report.xml, **/e2e-report.xml'
            
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'labs/06_07_08_test_framework',
                reportFiles: 'integration-report.html',
                reportName: 'Integration Tests'
            ])
            
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'labs/06_07_08_test_framework',
                reportFiles: 'e2e-report.html',
                reportName: 'E2E Tests'
            ])
            
            echo 'Cleaning up...'
            sh 'cd application/infra && docker-compose down || true'
        }
        
        success {
            echo '✓✓✓ ALL TESTS PASSED! ✓✓✓'
        }
        
        failure {
            echo '✗ Some tests failed. Check the reports.'
        }
    }
}