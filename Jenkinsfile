pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/vishukanase/your-flask-repo.git', branch: 'main'
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests yet. Add pytest if needed.'
                // Uncomment below line if you add tests
                // sh './$VENV_DIR/bin/python -m pytest'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup ./$VENV_DIR/bin/python $FLASK_APP > flask.log 2>&1 &'
                echo 'Flask app started in background.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
