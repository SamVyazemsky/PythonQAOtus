pipeline {
 agent any
 
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
