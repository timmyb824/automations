pipeline {
  agent any
  environment {
    // AWS_ACCESS_KEY_ID = credentials('aws-access-key')
    // AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
    // TF_VAR_region = "us-west-2"
    TF_CLI_CONFIG_FILE = "/var/jenkins_home/.terraformrc"
    TFC_TOKEN = credentials('terraform-cloud-token')
  }
  tools {
    terraform 'terraform latest'
  }
  stages {
    stage('Checkout code') {
        steps {
            checkout scm
        }
    }
    stage('Write CLI Config') {
      steps {
        writeFile file: '/var/jenkins_home/.terraformrc', text: """
          credentials "app.terraform.io" {
            token = "${TFC_TOKEN}"
          }
        """
      }
    }
    stage('Terraform Init') {
      steps {
        dir('terraform/cloudflare') {
          sh 'terraform init -backend-config="token=${TFC_TOKEN}"'
        }
      }
    }
    stage('Terraform Plan') {
      steps {
        dir('terraform/cloudflare') {
          sh 'terraform plan'
        }
      }
    }
    stage('Terraform Apply') {
      steps {
        script {
          try {
            dir('terraform/cloudflare') {
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
