pipeline {
    agent any
    stages {
        stage('Read and Print temp.txt') {
            steps {
                script {
                    // Read the contents of temp.txt and print to console
                    def fileContent = readFile 'temp.txt'
                    echo "Contents of temp.txt:\n${fileContent}"
                }
            }
        }
    }
}
