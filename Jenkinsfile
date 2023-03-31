pipeline {
  agent any
  environment {
    // AWS_ACCESS_KEY_ID = credentials('aws-access-key')
    // AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
    // TF_VAR_region = "us-west-2"
    TF_CLI_CONFIG_FILE = "/var/jenkins_home/.terraformrc"
    TFC_TOKEN = credentials('terraform-cloud-token')
    DOMAIN = env.DOMAIN
    ZONE_ID = env.ZONE_ID
    IP_ADDRESS = env.IP_ADDRESS
  }
  tools {
    terraform 'terraform latest'
  }
  stages {
    stage('Checkout code') {
      agent {
        label 'jenkins-slave'
      }
        steps {
            checkout scm
        }
    }
    stage('Write CLI Config') {
      agent {
        label 'jenkins-slave'
      }
      steps {
        writeFile file: '/var/jenkins_home/.terraformrc', text: """
          credentials "app.terraform.io" {
            token = "${TFC_TOKEN}"
          }
        """
      }
    }
    stage('Terraform Init') {
      agent {
        label 'jenkins-slave'
      }
      steps {
        dir('terraform/cloudflare') {
          sh 'terraform init'
        }
      }
    }
    stage('Terraform Plan') {
      podTemplate {
        node('jenkins-slave') {
      steps {
        dir('terraform/cloudflare') {
          sh "terraform plan -var 'domain=${DOMAIN}' -var 'zone_id=${ZONE_ID}' -var 'ip_address=${IP_ADDRESS}'"
        }
      }
    }
  }
}
    stage('Terraform Apply') {
      podTemplate {
        node('jenkins-slave') {
      steps {
        script {
          try {
            dir('terraform/cloudflare') {
              sh "terraform apply -var 'domain=${DOMAIN}' -var 'zone_id=${ZONE_ID}' -var 'ip_address=${IP_ADDRESS}'"
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
  }
}
