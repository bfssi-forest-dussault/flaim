
pipeline {
  agent {
    docker {
        image 'python:3.7-slim-buster'
        args '--user 0:0'  // https://stackoverflow.com/questions/51648534/unable-to-pip-install-in-docker-image-as-agent-through-jenkins-declarative-pipel
    }
  }

  environment {
    // https://jenkins.io/doc/book/using/using-credentials/#configuring-credentials
    SECRET_KEY = credentials('flaim-secret-key')
    FLAIM_DB_USER = credentials('flaim-db-user')
    FLAIM_DB_PASSWORD = credentials('flaim-db-password')
    REDIS_PASSWORD = credentials('flaim-redis-password')
    DEBUG = 'on'
  }


  stages {
    stage('build') {
      steps {
        sh '''
        pip install -r requirements/local.txt
        systemctl start postgresql
        '''
      }
    }
    stage('test') {
      steps {
        sh 'pytest'
      }
    }
  }
}
