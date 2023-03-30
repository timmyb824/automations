pipeline {
  agent any
//   environment {
//     AWS_ACCESS_KEY_ID = credentials('aws-access-key')
//     AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
//     TF_VAR_region = "us-west-2"
//   }
  stages {
    stage('Checkout code') {
        steps {
            checkout scm
        }
    }
    stage('Terraform Init') {
      steps {
        dir('/terraform/cloudflare') {
          sh 'terraform init'
        }
      }
    }
    stage('Terraform Plan') {
      steps {
        dir('/terraform/cloudflare') {
          sh 'terraform plan'
        }
      }
    }
    stage('Terraform Apply') {
      steps {
        script {
          try {
            dir('/terraform/cloudflare') {
              sh 'terraform apply' // -auto-approve'
            }
            slackSend channel: '#alerts', color: 'good', message: "Terraform deployment succeeded."
          } catch (Exception e) {
            slackSend channel: '#alerts', color: 'danger', message: "Terraform deployment failed: ${e.getMessage()}"
            throw e
          }
        }
      }
    }
  }
}
