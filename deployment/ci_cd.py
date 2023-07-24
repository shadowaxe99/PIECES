```python
import os
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = os.environ.get('JENKINS_URL')
    jenkins_username = os.environ.get('JENKINS_USERNAME')
    jenkins_password = os.environ.get('JENKINS_PASSWORD')
    server = Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)
    return server

def create_job(job_name, config):
    server = get_server_instance()
    if not server.has_job(job_name):
        server.create_job(job_name, config)
        print(f'Job {job_name} created')
    else:
        print(f'Job {job_name} already exists')

def build_job(job_name):
    server = get_server_instance()
    if server.has_job(job_name):
        job = server.get_job(job_name)
        job.invoke(build_params={"token": os.environ.get('JENKINS_BUILD_TOKEN')})
        print(f'Job {job_name} started')
    else:
        print(f'Job {job_name} does not exist')

def main():
    # Define your Jenkins job configuration here
    config = """
    <project>
        <actions/>
        <description></description>
        <keepDependencies>false</keepDependencies>
        <properties/>
        <scm class='hudson.scm.NullSCM'/>
        <canRoam>true</canRoam>
        <disabled>false</disabled>
        <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
        <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
        <triggers/>
        <concurrentBuild>false</concurrentBuild>
        <builders>
            <hudson.tasks.Shell>
                <command>echo 'Hello, Jenkins!'</command>
            </hudson.tasks.Shell>
        </builders>
        <publishers/>
        <buildWrappers/>
    </project>
    """
    job_name = 'AI_Travel_Booker_CI_CD'
    create_job(job_name, config)
    build_job(job_name)

if __name__ == "__main__":
    main()
```