pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SHREYASNAIR129/Fraud-Detection.git']]])
            }
        }
        stage("build"){
            steps{
                git 'https://github.com/SHREYASNAIR129/Fraud-Detection.git'
            }
        }
        stage("loading_data"){
            steps{
                sh label: '', script: 'python3 dataLoading.py'
            }
        }
        stage("data_preprocessing"){
            steps{
                sh label: '', script: 'python3 dataPreprocessing.py'
            }
        }
        stage("model_building_and_metrics"){
            steps{
                sh label: '', script: 'python3 modelSelection.py'
            }
        }
    }
}