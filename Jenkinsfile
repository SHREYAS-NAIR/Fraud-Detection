pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SHREYAS-NAIR/Fraud-Detection.git']]])
            }
        }
        stage("build"){
            steps{
                git 'https://github.com/SHREYAS-NAIR/Fraud-Detection.git'
            }
        }
        stage("installing_requirements"){
            steps{
                sh label: '', script: 'python3 installingRequirements.py'
            }
        }
        stage("loading_data"){
            steps{
                sh label: '', script: 'python3 dataLoading.py'
            }
        }
        stage("data_analysis"){
            steps{
                sh label: '', script: 'python3 dataAnalysis.py'
            }
        }
        stage("data_preprocessing"){
            steps{
                sh label: '', script: 'python3 dataPreprocessing.py'
            }
        }
        stage("data_visualization"){
            steps{
                sh label: '', script: 'python3 dataVisualization.py'
            }
        }
        stage("feature_engineering"){
            steps{
                sh label: '', script: 'python3 featureEngineering.py'
            }
        }
        stage("feature_selection"){
            steps{
                sh label: '', script: 'python3 featureSelection.py'
            }
        }
        stage("data_spliting"){
            steps{
                sh label: '', script: 'python3 dataSpliting.py'
            }
        }
        stage("model_selection"){
            steps{
                sh label: '', script: 'python3 modelSelection.py'
            }
        }
    }
}