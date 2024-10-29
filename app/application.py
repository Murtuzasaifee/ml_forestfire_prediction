import os
import subprocess

# Start the Streamlit app on the default Elastic Beanstalk port
if __name__ == "__main__":
    # Elastic Beanstalk assigns a port for the application
    port = os.environ.get('PORT', '8080')
    # Run the Streamlit app (pointing to app.py)
    subprocess.run(["streamlit", "run", "app/app.py", "--server.port", port, "--server.headless", "true"])
