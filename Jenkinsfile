pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install pytest'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m pytest -v'
      }   
    }
  }
}
